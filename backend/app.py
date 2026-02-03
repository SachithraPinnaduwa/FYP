import os
import sys
import threading
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add parent directory to path for advanced_gen imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend import AdaptivePrompter, CodeAnalyzer

app = Flask(__name__)
CORS(app)

# Config via environment variables
MODEL_NAME = os.environ.get("MODEL_NAME", "lora_model")
MAX_SEQ_LENGTH = int(os.environ.get("MAX_SEQ_LENGTH", "2048"))
LOAD_IN_4BIT = os.environ.get("LOAD_IN_4BIT", "True").lower() in ("1", "true", "yes")
DEVICE = os.environ.get("DEVICE", "cuda")

# Lazy-loaded model/tokenizer
_model_lock = threading.Lock()
model = None
tokenizer = None


def load_model():
    global model, tokenizer
    with _model_lock:
        if model is None or tokenizer is None:
            try:
                from unsloth import FastLanguageModel
            except Exception as e:
                raise RuntimeError("Failed to import unsloth. Ensure it's installed.") from e

            model, tokenizer = FastLanguageModel.from_pretrained(
                model_name=MODEL_NAME,
                max_seq_length=MAX_SEQ_LENGTH,
                dtype=None,
                load_in_4bit=LOAD_IN_4BIT,
            )
            # Move to inference mode helper if available
            try:
                FastLanguageModel.for_inference(model)
            except Exception:
                pass


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/generate-tests", methods=["POST"])
def generate_tests():
    data = request.get_json(force=True)
    code = data.get("code")
    description = data.get("description", "")
    max_new_tokens = int(data.get("max_new_tokens", 512))

    if not code:
        return jsonify({"error": "Missing 'code' field in JSON body."}), 400

    # Ensure model is loaded
    try:
        load_model()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    complex_input = f"Problem Description:\n{description}\n\nCode to Test:\n{code}"

    messages = [
        {
            "role": "user",
            "content": (
                "Write a comprehensive Python unit test suite for the provided code.\n\n"
                f"{complex_input}"
            ),
        }
    ]

    try:
        input_ids = tokenizer.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=True,
            return_tensors="pt",
        )

        # Move tensors to device if possible
        import torch
        device = torch.device("cuda" if DEVICE == "cuda" and torch.cuda.is_available() else "cpu")
        input_ids = input_ids.to(device)

        attention_mask = input_ids.ne(tokenizer.pad_token_id).long()

        with torch.no_grad():
            outputs = model.generate(
                input_ids=input_ids,
                attention_mask=attention_mask,
                max_new_tokens=max_new_tokens,
                eos_token_id=tokenizer.eos_token_id,
                pad_token_id=tokenizer.eos_token_id,
            )

        generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
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
    
    if not code:
        return jsonify({"error": "Missing 'code' field in JSON body."}), 400
    
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
    
    if not code:
        return jsonify({"error": "Missing 'code' field in JSON body."}), 400
    
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
    
    if not code:
        return jsonify({"error": "Missing 'code' field in JSON body."}), 400
    
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
            "role": "user",
            "content": prompt_result.final_prompt,
        }
    ]
    
    try:
        input_ids = tokenizer.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=True,
            return_tensors="pt",
        )
        
        import torch
        device = torch.device("cuda" if DEVICE == "cuda" and torch.cuda.is_available() else "cpu")
        input_ids = input_ids.to(device)
        
        attention_mask = input_ids.ne(tokenizer.pad_token_id).long()
        
        with torch.no_grad():
            outputs = model.generate(
                input_ids=input_ids,
                attention_mask=attention_mask,
                max_new_tokens=max_new_tokens,
                eos_token_id=tokenizer.eos_token_id,
                pad_token_id=tokenizer.eos_token_id,
            )
        
        generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        response = {
            "tests": generated,
            "structure_summary": prompt_result.structure_summary,
            "intentions": prompt_result.intentions.to_dict(),
        }
        
        if include_debug:
            response["prompt_used"] = prompt_result.final_prompt
        
        return jsonify(response)
        
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
    
    if not code:
        return jsonify({"error": "Missing 'code' field in JSON body."}), 400
    
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
