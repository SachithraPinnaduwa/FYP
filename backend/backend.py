import ast
import os
import re
import sys
import threading
import time
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Configure logging to go to a file
logging.basicConfig(
    filename='backend_generation.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Add parent directory to path for advanced_gen imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend import AdaptivePrompter, CodeAnalyzer

app = Flask(__name__)
CORS(app)


# =============================================================================
# Input Validation Helpers
# =============================================================================

def _looks_like_prose(line: str) -> bool:
    """
    Heuristic: return True when a line looks like natural-language prose
    rather than Python source code.
    """
    stripped = line.strip()

    # Common Python line starters – treat as code immediately
    python_starters = (
        'def ', 'class ', 'import ', 'from ', 'return ', 'if ', 'else:',
        'elif ', 'for ', 'while ', 'try:', 'except', 'finally:', 'with ',
        'pass', 'raise ', 'yield ', 'assert ', 'lambda ', 'async ', 'await ',
        'print(', '@', 'self.', 'cls.', '#', '"""', "'''", '"', "'",
    )
    for starter in python_starters:
        if stripped.startswith(starter):
            return False

    # Lines containing operators / brackets are almost certainly code
    if re.search(r'[=\(\)\[\]\{\}:,\+\-\*\/\%\&\|\^<>!]', stripped):
        return False

    # 3+ consecutive purely-alphabetic words → likely prose
    words = stripped.split()
    if len(words) >= 3:
        alpha_words = sum(1 for w in words if re.match(r'^[a-zA-Z]+$', w))
        if alpha_words / len(words) > 0.7:
            return True

    return False


def validate_code_input(code: str):
    """
    Validate that *code* is non-empty, syntactically valid Python, and
    contains actual code rather than plain text.

    Returns:
        (True, "")               – input is acceptable
        (False, error_message)   – input is rejected; message explains why
    """
    # 1. Empty / blank input
    if not code or not code.strip():
        return False, "Input code is empty. Please provide Python code to test."

    # 2. Syntax check
    try:
        tree = ast.parse(code)
    except SyntaxError as exc:
        line_num = exc.lineno or 0
        lines = code.split('\n')
        offending = lines[line_num - 1].strip() if 0 < line_num <= len(lines) else ""
        if offending and _looks_like_prose(offending):
            return False, (
                f"The input appears to contain non-Python text on line {line_num}: "
                f'"{offending[:80]}". Please provide valid Python code only.'
            )
        return False, (
            f"Syntax error on line {line_num}: {exc.msg}. "
            "Please fix the code and try again."
        )

    # 3. Ensure there is at least one meaningful Python construct
    #    (Any real bare prose outside a string would have already failed ast.parse above.)
    has_functions = any(
        isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) for n in ast.walk(tree)
    )
    has_classes = any(isinstance(n, ast.ClassDef) for n in ast.walk(tree))
    has_imports = any(
        isinstance(n, (ast.Import, ast.ImportFrom)) for n in ast.walk(tree)
    )
    has_assignments = any(
        isinstance(n, (ast.Assign, ast.AugAssign, ast.AnnAssign))
        for n in ast.iter_child_nodes(tree)
    )

    if not (has_functions or has_classes or has_imports or has_assignments):
        # All top-level statements are bare string/constant expressions → plain text
        body = list(ast.iter_child_nodes(tree))
        if body and all(
            isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant)
            for n in body
        ):
            return False, (
                "The input contains only plain text strings, not Python code. "
                "Please provide actual Python functions, classes, or statements to test."
            )
        return False, (
            "No testable Python constructs (functions, classes, imports, or assignments) "
            "were found. Please provide Python code that can be unit-tested."
        )

    return True, ""

# Config via environment variables
MODEL_NAME = os.environ.get("MODEL_NAME", "../gguf_model/unsloth.q4_k_m.gguf")
MAX_SEQ_LENGTH = int(os.environ.get("MAX_SEQ_LENGTH", "2048"))
DEVICE = os.environ.get("DEVICE", "cuda")

# Lazy-loaded model
_model_lock = threading.Lock()
model = None

def load_model():
    global model
    with _model_lock:
        if model is None:
            try:
                from llama_cpp import Llama
            except ImportError as e:
                raise RuntimeError("Failed to import llama_cpp. Ensure llama-cpp-python is installed.") from e

            # Load the GGUF model using llama.cpp
            model_path = MODEL_NAME
            if not os.path.exists(model_path):
                # fallback for testing
                model_path = os.path.join(os.path.dirname(__file__), "..", "gguf_model", "unsloth.q4_k_m.gguf")
                
            model = Llama(
                model_path=model_path,
                n_ctx=MAX_SEQ_LENGTH,
                n_gpu_layers=-1 if DEVICE == "cuda" else 0,
                verbose=False
            )


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/generate-tests", methods=["POST"])
def generate_tests():
    data = request.get_json(force=True)
    code = data.get("code")
    description = data.get("description", "")
    max_new_tokens = int(data.get("max_new_tokens", 512))
    log_generation = data.get("log_generation", False)

    valid, err = validate_code_input(code)
    if not valid:
        return jsonify({"error": err}), 400

    # Ensure model is loaded
    try:
        load_model()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    complex_input = f"Problem Description:\n{description}\n\nCode to Test:\n{code}"

    messages = [
        {
            "role": "system",
            "content": "You are a helpful coding assistant that writes Python unit tests. Output ONLY valid Python test code. Do NOT output any explanations or conversational text. Start your response directly with the import statements."
        },
        {
            "role": "user",
            "content": (
                "Write a comprehensive Python unit test suite for this code.\n"
                "Requirements:\n"
                "1. Use the unittest framework (import unittest)\n"
                "2. Generate ONLY Python code\n\n"
                f"{complex_input}"
            ),
        }
    ]

    if log_generation:
        start_time = time.time()
        logger.info("Starting test generation (basic). Input code and description omitted for privacy.")

    try:
        response = model.create_chat_completion(
            messages=messages,
            max_tokens=max_new_tokens,
            temperature=0.2, # Optional, use for testing
        )
        
        if log_generation:
            generation_time = time.time() - start_time
            logger.info(f"Test generation (basic) completed in {generation_time:.2f} seconds. Generated code omitted for privacy.")
        
        generated = response["choices"][0]["message"]["content"]
        return jsonify({"tests": generated})

    except Exception as e:
        return jsonify({"error": f"Generation failed: {e}"}), 500


# =============================================================================
# Adaptive Prompting Endpoints (Static Analysis Only)
# =============================================================================

# Lazy-loaded adaptive prompter
_adaptive_prompter = None
_adaptive_lock = threading.Lock()


def get_adaptive_prompter():
    """Get or create the AdaptivePrompter instance (uses static analysis only)."""
    global _adaptive_prompter
    with _adaptive_lock:
        if _adaptive_prompter is None:
            _adaptive_prompter = AdaptivePrompter()
    return _adaptive_prompter


@app.route("/analyze-code", methods=["POST"])
def analyze_code():
    """
    Analyze Python code structure using static analysis (no AI).
    
    Request body:
        {
            "code": "def foo(): ..."
        }
    
    Returns:
        {
            "structure": {...},
            "summary": "..."
        }
    """
    data = request.get_json(force=True)
    code = data.get("code")

    valid, err = validate_code_input(code)
    if not valid:
        return jsonify({"error": err}), 400

    try:
        analyzer = CodeAnalyzer()
        structure = analyzer.analyze(code)
        summary = analyzer.get_structure_summary(structure)
        
        return jsonify({
            "structure": structure.to_dict(),
            "summary": summary,
        })
    except ValueError as e:
        return jsonify({"error": f"Parse error: {e}"}), 400
    except Exception as e:
        return jsonify({"error": f"Analysis failed: {e}"}), 500


@app.route("/generate-intentions", methods=["POST"])
def generate_intentions():
    """
    Generate test intentions using static code analysis (no AI required).
    
    Request body:
        {
            "code": "def foo(): ...",
            "description": "optional problem description"
        }
    
    Returns:
        {
            "intentions": {...},
            "prompt_format": "..."
        }
    """
    data = request.get_json(force=True)
    code = data.get("code")
    description = data.get("description", "")

    valid, err = validate_code_input(code)
    if not valid:
        return jsonify({"error": err}), 400

    try:
        prompter = get_adaptive_prompter()
        result = prompter.get_intentions_only(code, description)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"Intention generation failed: {e}"}), 500


@app.route("/generate-tests-adaptive", methods=["POST"])
def generate_tests_adaptive():
    """
    Generate tests using the full Adaptive Prompting pipeline.
    
    Pipeline:
    1. Static analysis (ast) -> code structure
    2. Static analysis (ast) -> test intentions (no AI required)
    3. Prompt construction -> optimized prompt
    4. Fine-tuned model -> test code generation
    
    Request body:
        {
            "code": "def foo(): ...",
            "description": "optional problem description",
            "max_new_tokens": 512  // optional
        }
    
    Returns:
        {
            "tests": "generated test code",
            "structure_summary": "...",
            "intentions": {...},
            "prompt_used": "..."
        }
    """
    data = request.get_json(force=True)
    code = data.get("code")
    description = data.get("description", "")
    max_new_tokens = int(data.get("max_new_tokens", 512))
    include_debug = data.get("include_debug", False)
    log_generation = data.get("log_generation", False)

    valid, err = validate_code_input(code)
    if not valid:
        return jsonify({"error": err}), 400

    # Ensure model is loaded
    try:
        load_model()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    # Step 1-3: Create adaptive prompt
    try:
        prompter = get_adaptive_prompter()
        prompt_result = prompter.create_adaptive_prompt(code, description)
    except Exception as e:
        return jsonify({"error": f"Prompt construction failed: {e}"}), 500
    
    # Step 4: Generate tests with fine-tuned model
    messages = [
        {
            "role": "system",
            "content": "You are a helpful coding assistant that writes Python unit tests."
        },
        {
            "role": "user",
            "content": prompt_result.final_prompt,
        }
    ]
    
    if log_generation:
        start_time = time.time()
        logger.info("Starting test generation (adaptive). Input code, description, and intentions omitted for privacy.")

    try:
        response = model.create_chat_completion(
            messages=messages,
            max_tokens=max_new_tokens,
            temperature=0.2, # Optional, use for testing
        )
        
        if log_generation:
            generation_time = time.time() - start_time
            logger.info(f"Test generation (adaptive) completed in {generation_time:.2f} seconds. Generated code omitted for privacy.")
        
        generated = response["choices"][0]["message"]["content"]
        
        response_data = {
            "tests": generated,
            "structure_summary": prompt_result.structure_summary,
            "intentions": prompt_result.intentions.to_dict(),
        }
        
        if include_debug:
            response_data["prompt_used"] = prompt_result.final_prompt
        
        return jsonify(response_data)
        
    except Exception as e:
        return jsonify({"error": f"Generation failed: {e}"}), 500


@app.route("/generate-prompt-only", methods=["POST"])
def generate_prompt_only():
    """
    Generate the adaptive prompt without running the model.
    
    Useful for debugging or when you want to inspect the prompt
    before sending it to the model.
    
    Request body:
        {
            "code": "def foo(): ...",
            "description": "optional problem description"
        }
    
    Returns:
        {
            "prompt": "the constructed prompt",
            "structure_summary": "...",
            "intentions": {...}
        }
    """
    data = request.get_json(force=True)
    code = data.get("code")
    description = data.get("description", "")

    valid, err = validate_code_input(code)
    if not valid:
        return jsonify({"error": err}), 400

    try:
        prompter = get_adaptive_prompter()
        result = prompter.create_adaptive_prompt(code, description)

        return jsonify({
            "prompt": result.final_prompt,
            "structure_summary": result.structure_summary,
            "intentions": result.intentions.to_dict(),
        })
    except Exception as e:
        return jsonify({"error": f"Prompt generation failed: {e}"}), 500


if __name__ == "__main__":
    # For local debugging only. Use a WSGI server in production.
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
