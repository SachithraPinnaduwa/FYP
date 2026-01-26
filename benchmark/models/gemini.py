"""
Gemini Baseline model runner for test generation.
Uses Google's Gemini models via API for comparison.
"""

import os
import sys
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class GeminiTestGenerator:
    """
    Test generator using Google's Gemini models as a baseline.
    """
    
    def __init__(
        self,
        model: str = "gemini-2.5-flash",
        api_key: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2048
    ):
        """
        Initialize the Gemini test generator.
        
        Args:
            model: The Gemini model to use (gemini-1.5-pro, gemini-1.5-flash, etc.)
            api_key: Google API key (uses GEMINI_API_KEY env var if not provided)
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
        """
        self.model = model
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.client = None
        
        if not self.api_key:
            print("Warning: No Gemini API key found. Set GEMINI_API_KEY in .env file.")
    
    def _get_client(self):
        """Lazy initialization of Gemini client."""
        if self.client is None:
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                self.client = genai.GenerativeModel(self.model)
            except ImportError:
                raise ImportError("Please install google-generativeai: pip install google-generativeai")
        return self.client
    
    def generate_tests(
        self,
        code: str,
        problem_description: str = "",
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
    ) -> str:
        """
        Generate unit tests for the given code using Gemini.
        
        Args:
            code: The Python code to generate tests for
            problem_description: Optional description of what the code does
            max_tokens: Maximum number of tokens to generate
            temperature: Sampling temperature
            
        Returns:
            Generated test code as a string
        """
        client = self._get_client()
        
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
        
        # Configure generation parameters
        generation_config = {
            "temperature": temperature,
            "max_output_tokens": max_tokens,
        }
        
        response = client.generate_content(
            prompt,
            generation_config=generation_config
        )
        
        generated_text = response.text
        test_code = self._extract_test_code(generated_text)
        
        return test_code
    
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


class MockGeminiTestGenerator:
    """
    Mock Gemini generator for testing without API access.
    Generates template-based tests.
    """
    
    def __init__(self, model: str = "gemini-mock"):
        self.model = model
    
    def generate_tests(
        self,
        code: str,
        problem_description: str = "",
        **kwargs
    ) -> str:
        """Generate mock tests based on code analysis."""
        
        # Simple analysis of the code
        lines = code.split('\n')
        functions = []
        classes = []
        
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('def ') and '(' in stripped:
                func_name = stripped[4:stripped.index('(')]
                functions.append(func_name)
            elif stripped.startswith('class ') and ':' in stripped:
                class_name = stripped[6:stripped.index('(') if '(' in stripped else stripped.index(':')]
                classes.append(class_name.strip())
        
        # Generate template tests
        test_code = '''"""Auto-generated unit tests (Gemini baseline mock)"""
import unittest
import sys
sys.path.insert(0, '..')

'''
        
        # Add imports based on what we found
        if classes or functions:
            test_code += "# Import the module under test\n"
            test_code += "# from subjects.module_name import *\n\n"
        
        # Generate test class
        test_code += "class TestGeneratedByGemini(unittest.TestCase):\n"
        test_code += "    '''Auto-generated test cases'''\n\n"
        
        for func in functions:
            test_code += f"    def test_{func}_basic(self):\n"
            test_code += f"        '''Test {func} with basic input'''\n"
            test_code += f"        # TODO: Add test for {func}\n"
            test_code += f"        self.assertTrue(True)  # Placeholder\n\n"
        
        for cls in classes:
            test_code += f"    def test_{cls.lower()}_creation(self):\n"
            test_code += f"        '''Test {cls} instantiation'''\n"
            test_code += f"        # TODO: Add test for {cls}\n"
            test_code += f"        self.assertTrue(True)  # Placeholder\n\n"
        
        if not functions and not classes:
            test_code += "    def test_placeholder(self):\n"
            test_code += "        '''Placeholder test'''\n"
            test_code += "        self.assertTrue(True)\n\n"
        
        test_code += '''
if __name__ == '__main__':
    unittest.main()
'''
        
        return test_code


def generate_tests_for_file(
    source_file: str,
    output_file: str,
    model: str = "gemini-1.5-pro",
    problem_description: str = "",
    use_mock: bool = False
) -> str:
    """
    Generate tests for a Python source file using Gemini and save to output file.
    
    Args:
        source_file: Path to the Python file to test
        output_file: Path to save the generated tests
        model: Gemini model to use
        problem_description: Optional description of the code
        use_mock: Whether to use mock generator (for testing without API)
        
    Returns:
        Generated test code
    """
    # Read source code
    with open(source_file, 'r') as f:
        source_code = f.read()
    
    # Generate tests
    if use_mock:
        generator = MockGeminiTestGenerator(model=model)
    else:
        generator = GeminiTestGenerator(model=model)
    
    test_code = generator.generate_tests(source_code, problem_description)
    
    # Save to file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        f.write(test_code)
    
    print(f"Gemini-generated tests saved to {output_file}")
    return test_code


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate unit tests using Gemini")
    parser.add_argument("--source", required=True, help="Source file to generate tests for")
    parser.add_argument("--output", required=True, help="Output file for generated tests")
    parser.add_argument("--model", default="gemini-1.5-pro", help="Gemini model to use")
    parser.add_argument("--description", default="", help="Problem description")
    parser.add_argument("--mock", action="store_true", help="Use mock generator")
    
    args = parser.parse_args()
    
    generate_tests_for_file(
        args.source,
        args.output,
        args.model,
        args.description,
        args.mock
    )
