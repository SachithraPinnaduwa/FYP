from llama_cpp import Llama
import re
import os
from pathlib import Path

class GGUFModelGenerator:
    def __init__(self, model_path="gguf_model/unsloth.q4_k_m.gguf"):
        print("Loading GGUF Model via llama-cpp-python...")
        # Resolve path relative to the FYP directory
        base_dir = Path(__file__).resolve().parent.parent.parent
        full_path = base_dir / model_path
        
        if not full_path.exists():
            raise FileNotFoundError(f"Model file not found at {full_path}")
            
        self.llm = Llama(
            model_path=str(full_path),
            n_ctx=2048,
            n_gpu_layers=-1,
            verbose=False # Set to True for debugging if needed
        )

    def generate_tests(self, code: str, problem_description: str = "") -> str:
        messages = [
            {"role": "system", "content": "You are a helpful coding assistant that writes Python unit tests."},
            {"role": "user", "content": f"Write a comprehensive Python unit test suite for this code.\n\nProblem Description:\n{problem_description}\n\nCode to Test:\n{code}"}
        ]
        
        output = self.llm.create_chat_completion(
            messages=messages,
            max_tokens=2048,
            temperature=0.7,
            top_p=0.9
        )
        
        try:
            response_text = output["choices"][0]["message"]["content"].strip()
            # Try to extract python code block
            code_blocks = re.findall(r'```(?:python)?\n(.*?)\n```', response_text, re.DOTALL)
            if code_blocks:
                response_text = "\n\n".join(code_blocks).strip()
        except Exception:
            response_text = ""
            
        return response_text