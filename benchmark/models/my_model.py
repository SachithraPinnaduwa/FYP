"""
Your fine-tuned model runner for test generation.
Uses the LoRA adapter trained in working_model.ipynb
"""

import os
import sys
import torch
from pathlib import Path
from typing import Optional
import json


class YourModelTestGenerator:
    """
    Test generator using your fine-tuned Qwen2.5-Coder model with LoRA adapters.
    """
    
    def __init__(
        self,
        model_path: str = "lora_model",
        max_seq_length: int = 2048,
        load_in_4bit: bool = True,
        device: str = "cuda"
    ):
        """
        Initialize the test generator with the fine-tuned model.
        
        Args:
            model_path: Path to the LoRA adapter directory
            max_seq_length: Maximum sequence length
            load_in_4bit: Whether to load in 4-bit quantization
            device: Device to run on ('cuda' or 'cpu')
        """
        self.model_path = model_path
        self.max_seq_length = max_seq_length
        self.load_in_4bit = load_in_4bit
        self.device = device
        self.model = None
        self.tokenizer = None
        
    def load_model(self):
        """Load the fine-tuned model with LoRA adapters."""
        from unsloth import FastLanguageModel
        
        self.model, self.tokenizer = FastLanguageModel.from_pretrained(
            model_name=self.model_path,
            max_seq_length=self.max_seq_length,
            dtype=None,  # Auto-detect
            load_in_4bit=self.load_in_4bit,
        )
        FastLanguageModel.for_inference(self.model)
        print(f"Model loaded from {self.model_path}")
        
    def generate_tests(
        self,
        code: str,
        problem_description: str = "",
        max_new_tokens: int = 1024,
        temperature: float = 0.7,
        top_p: float = 0.9,
    ) -> str:
        """
        Generate unit tests for the given code.
        
        Args:
            code: The Python code to generate tests for
            problem_description: Optional description of what the code does
            max_new_tokens: Maximum number of tokens to generate
            temperature: Sampling temperature
            top_p: Top-p sampling parameter
            
        Returns:
            Generated test code as a string
        """
        if self.model is None:
            self.load_model()
        
        # Build the input prompt
        if problem_description:
            complex_input = f"Problem Description:\n{problem_description}\n\nCode to Test:\n{code}"
        else:
            complex_input = f"Code to Test:\n{code}"
        
        messages = [
            {
                "role": "user",
                "content": (
                    "Write a comprehensive Python unit test suite for the provided code.\n\n"
                    f"{complex_input}"
                )
            }
        ]
        
        input_ids = self.tokenizer.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=True,
            return_tensors="pt"
        ).to(self.device)
        
        attention_mask = input_ids.ne(self.tokenizer.pad_token_id).long()
        
        outputs = self.model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=max_new_tokens,
            eos_token_id=self.tokenizer.eos_token_id,
            pad_token_id=self.tokenizer.eos_token_id,
            temperature=temperature,
            top_p=top_p,
            do_sample=True,
        )
        
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Extract only the generated test code (after the prompt)
        test_code = self._extract_test_code(generated_text)
        
        return test_code
    
    def _extract_test_code(self, text: str) -> str:
        """
        Extract the test code from the model's full output.
        
        Args:
            text: Full model output including prompt
            
        Returns:
            Extracted test code
        """
        # Look for code blocks
        if "```python" in text:
            # Extract code between ```python and ```
            parts = text.split("```python")
            if len(parts) > 1:
                code_part = parts[-1]
                if "```" in code_part:
                    code_part = code_part.split("```")[0]
                return code_part.strip()
        
        # Look for common test patterns
        lines = text.split('\n')
        test_lines = []
        in_test = False
        
        for line in lines:
            if 'import unittest' in line or 'import pytest' in line or 'def test_' in line or 'class Test' in line:
                in_test = True
            if in_test:
                test_lines.append(line)
        
        if test_lines:
            return '\n'.join(test_lines)
        
        # Return everything after "assistant" marker if present
        if "assistant" in text.lower():
            parts = text.lower().split("assistant")
            return text[len(text) - len(parts[-1]):].strip()
        
        return text


def generate_tests_for_file(
    source_file: str,
    output_file: str,
    model_path: str = "lora_model",
    problem_description: str = ""
) -> str:
    """
    Generate tests for a Python source file and save to output file.
    
    Args:
        source_file: Path to the Python file to test
        output_file: Path to save the generated tests
        model_path: Path to the LoRA model
        problem_description: Optional description of the code
        
    Returns:
        Generated test code
    """
    # Read source code
    with open(source_file, 'r') as f:
        source_code = f.read()
    
    # Generate tests
    generator = YourModelTestGenerator(model_path=model_path)
    test_code = generator.generate_tests(source_code, problem_description)
    
    # Save to file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        f.write(test_code)
    
    print(f"Generated tests saved to {output_file}")
    return test_code


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate unit tests using fine-tuned model")
    parser.add_argument("--source", required=True, help="Source file to generate tests for")
    parser.add_argument("--output", required=True, help="Output file for generated tests")
    parser.add_argument("--model-path", default="lora_model", help="Path to LoRA model")
    parser.add_argument("--description", default="", help="Problem description")
    
    args = parser.parse_args()
    
    generate_tests_for_file(
        args.source,
        args.output,
        args.model_path,
        args.description
    )
