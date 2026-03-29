import requests
import re
import json

class APISimplePromptGenerator:
    def __init__(self, backend_url="http://127.0.0.1:5000"):
        print(f"Loading Simple Prompt Generator API ({backend_url})...")
        self.backend_url = backend_url
        self.endpoint = f"{self.backend_url}/generate-tests"

    def generate_tests(self, code: str, problem_description: str = "") -> str:
        payload = {
            "code": code,
            "description": problem_description,
            "max_new_tokens": 1024
        }
        try:
            response = requests.post(self.endpoint, json=payload, timeout=120)
            response.raise_for_status()
            data = response.json()
            response_text = data.get("tests", "")
            
            # Extract code from markdown blocks if present
            code_blocks = re.findall(r'```(?:python)?\n(.*?)\n```', response_text, re.DOTALL)
            if code_blocks:
                response_text = "\n\n".join(code_blocks).strip()
            
            return response_text
        except Exception as e:
            print(f"Error calling simple API: {e}")
            return ""

class APIAdaptivePromptGenerator:
    def __init__(self, backend_url="http://127.0.0.1:5000"):
        print(f"Loading Adaptive Prompt Generator API ({backend_url})...")
        self.backend_url = backend_url
        self.endpoint = f"{self.backend_url}/generate-tests-adaptive"

    def generate_tests(self, code: str, problem_description: str = "") -> str:
        payload = {
            "code": code,
            "description": problem_description,
            "max_new_tokens": 1024
        }
        try:
            response = requests.post(self.endpoint, json=payload, timeout=120)
            response.raise_for_status()
            data = response.json()
            response_text = data.get("tests", "")
            
            # Extract code from markdown blocks if present
            code_blocks = re.findall(r'```(?:python)?\n(.*?)\n```', response_text, re.DOTALL)
            if code_blocks:
                response_text = "\n\n".join(code_blocks).strip()
            
            return response_text
        except Exception as e:
            print(f"Error calling adaptive API: {e}")
            return ""