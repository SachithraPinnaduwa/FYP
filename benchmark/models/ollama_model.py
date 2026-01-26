"""
Ollama model runner for test generation.
Uses Ollama API for local model inference.
"""

import os
import sys
from typing import Optional
from pathlib import Path
import requests
import json


class OllamaTestGenerator:
    """
    Test generator using Ollama API with local models.
    """
    
    def __init__(
        self,
        model: str = "codellama",
        base_url: str = "http://localhost:11434",
        temperature: float = 0.7,
        max_tokens: int = 2048
    ):
        """
        Initialize the Ollama test generator.
        
        Args:
            model: The Ollama model to use (codellama, deepseek-coder, etc.)
            base_url: Base URL for Ollama API
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
        """
        self.model = model
        self.base_url = base_url.rstrip('/')
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.api_url = f"{self.base_url}/api/generate"
        
    def _check_connection(self) -> bool:
        """Check if Ollama is running and accessible."""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False
    
    def generate_tests(
        self,
        code: str,
        problem_description: str = "",
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
    ) -> str:
        """
        Generate unit tests for the given code using Ollama.
        
        Args:
            code: The Python code to generate tests for
            problem_description: Optional description of what the code does
            max_tokens: Maximum number of tokens to generate
            temperature: Sampling temperature
            
        Returns:
            Generated test code as a string
        """
        # Check if Ollama is running
        if not self._check_connection():
            raise ConnectionError(
                f"Cannot connect to Ollama at {self.base_url}.\n"
                "Make sure Ollama is running: ollama serve\n"
                "Install Ollama from: https://ollama.ai/"
            )
        
        max_tokens = max_tokens or self.max_tokens
        temperature = temperature if temperature is not None else self.temperature
        
        # Build the prompt
        if problem_description:
            context = f"Problem Description:\n{problem_description}\n\nCode to Test:\n{code}"
        else:
            context = f"Code to Test:\n{code}"
        
        prompt = f"""You are an expert Python test engineer. 
Your task is to write comprehensive unit tests for the provided Python code.

Guidelines:
1. Use the unittest framework (import unittest)
2. Test normal cases, edge cases, and error cases
3. Use descriptive test method names
4. Include assertions that verify expected behavior
5. Test exception handling where appropriate
6. Include a main block to run the tests

Return ONLY the Python test code, no explanations.

Write a comprehensive Python unit test suite for the following code:

{context}

Generate complete, runnable test code using unittest."""

        # Prepare the request
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens,
            }
        }
        
        try:
            # Make the API request
            response = requests.post(
                self.api_url,
                json=payload,
                timeout=120  # Longer timeout for generation
            )
            response.raise_for_status()
            
            result = response.json()
            generated_text = result.get("response", "")
            
            if not generated_text:
                raise ValueError("Empty response from Ollama")
            
            test_code = self._extract_test_code(generated_text)
            return test_code
            
        except requests.exceptions.Timeout:
            raise TimeoutError(
                f"Request to Ollama timed out. The model '{self.model}' might be too slow.\n"
                "Try a faster model or increase the timeout."
            )
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error communicating with Ollama: {e}")
    
    def _extract_test_code(self, text: str) -> str:
        """
        Extract the test code from the model's response.
        
        Args:
            text: Model response text
            
        Returns:
            Extracted test code
        """
        # Look for code blocks
        if "```python" in text:
            parts = text.split("```python")
            if len(parts) > 1:
                code_part = parts[-1]
                if "```" in code_part:
                    code_part = code_part.split("```")[0]
                return code_part.strip()
        
        if "```" in text:
            parts = text.split("```")
            if len(parts) >= 2:
                return parts[1].strip()
        
        return text.strip()


def generate_tests_for_file(
    source_file: str,
    output_file: str,
    model: str = "codellama",
    problem_description: str = "",
    base_url: str = "http://localhost:11434"
) -> str:
    """
    Generate tests for a Python source file using Ollama and save to output file.
    
    Args:
        source_file: Path to the Python file to test
        output_file: Path to save the generated tests
        model: Ollama model to use
        problem_description: Optional description of the code
        base_url: Base URL for Ollama API
        
    Returns:
        Generated test code
    """
    # Read source code
    with open(source_file, 'r') as f:
        source_code = f.read()
    
    # Generate tests
    generator = OllamaTestGenerator(model=model, base_url=base_url)
    test_code = generator.generate_tests(source_code, problem_description)
    
    # Save to file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        f.write(test_code)
    
    print(f"Ollama-generated tests saved to {output_file}")
    return test_code


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate unit tests using Ollama")
    parser.add_argument("--source", required=True, help="Source file to generate tests for")
    parser.add_argument("--output", required=True, help="Output file for generated tests")
    parser.add_argument("--model", default="codellama", help="Ollama model to use")
    parser.add_argument("--description", default="", help="Problem description")
    parser.add_argument("--base-url", default="http://localhost:11434", help="Ollama base URL")
    
    args = parser.parse_args()
    
    generate_tests_for_file(
        args.source,
        args.output,
        args.model,
        args.description,
        args.base_url
    )
