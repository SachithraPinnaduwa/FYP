"""
Adaptive Prompter Module (Pipeline Orchestrator)

Implements the complete Adaptive Prompting pipeline:
1. Static Analysis (CodeAnalyzer) - Extract code structure
2. Static Intention Generation (StaticIntentionGenerator) - Determine what to test  
3. Prompt Construction - Merge into optimized prompt format
4. Ready for Fine-Tuned Model - Output for test generation

This module coordinates the "Structure + Intentions = Better Prompts" strategy.
All analysis is done using static code analysis - no AI/LLM required for prompt construction.
"""

import json
from typing import Optional, Dict, Any
from dataclasses import dataclass, field

from .code_analyzer import CodeAnalyzer, ModuleInfo
from .static_intention_generator import StaticIntentionGenerator, IntentionPlan


@dataclass
class AdaptivePromptResult:
    """Result of the adaptive prompting pipeline."""
    # Raw components
    code: str
    structure: ModuleInfo
    intentions: IntentionPlan
    
    # Constructed prompt
    final_prompt: str
    
    # Metadata
    structure_summary: str = ""
    problem_description: str = ""
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "code": self.code,
            "structure": self.structure.to_dict(),
            "intentions": self.intentions.to_dict(),
            "final_prompt": self.final_prompt,
            "structure_summary": self.structure_summary,
            "problem_description": self.problem_description,
        }


class AdaptivePrompter:
    """
    Main pipeline for Adaptive Prompting.
    
    Uses static analysis for both code structure extraction and 
    test intention generation. No external AI/LLM required.
    """
    
    # Prompt template for the fine-tuned model
    PROMPT_TEMPLATE = """You are an expert Python test engineer. Write comprehensive unit tests for the provided code.

## Code Structure
{structure_summary}

## Test Strategy
{intentions}

## Code to Test
```python
{code}
```

{problem_section}

## Requirements
1. Use the unittest framework (import unittest)
2. Follow the test intentions above as your guide
3. Include setup/teardown if needed
4. Test all identified edge cases and error conditions
5. Use descriptive test method names that reflect the intention
6. Include assertions that verify expected behavior

Generate complete, runnable Python test code:"""

    SIMPLE_PROMPT_TEMPLATE = """Write a comprehensive Python unit test suite for the provided code.

## Code Structure
{structure_summary}

## Test Intentions
{intentions}

## Code to Test
```python
{code}
```

{problem_section}

Generate complete unittest code:"""

    def __init__(self):
        """
        Initialize the adaptive prompter.
        """
        self.code_analyzer = CodeAnalyzer()
        self.intention_generator = StaticIntentionGenerator()
    
    def create_adaptive_prompt(
        self,
        code: str,
        problem_description: str = "",
        use_detailed_template: bool = True,
    ) -> AdaptivePromptResult:
        """
        Create an optimized prompt using the full adaptive pipeline.
        
        Pipeline:
        1. Parse code with ast to extract structure
        2. Use static analysis to generate test intentions
        3. Merge into final optimized prompt
        
        Args:
            code: The Python source code to generate tests for
            problem_description: Optional description of what the code does
            use_detailed_template: Use detailed vs simple template
            
        Returns:
            AdaptivePromptResult with all components and final prompt
        """
        # Step 1: Static Analysis
        try:
            structure = self.code_analyzer.analyze(code)
            structure_summary = self.code_analyzer.get_structure_summary(structure)
        except ValueError as e:
            # Handle parse errors gracefully
            structure = ModuleInfo()
            structure_summary = f"[Parse Error: {e}. Treating as opaque code block.]"
        
        # Step 2: Generate Test Intentions (using static analysis)
        intentions = self.intention_generator.generate_intentions(
            code=code,
            structure_summary=structure_summary,
            problem_description=problem_description,
        )
        
        # Step 3: Construct Final Prompt
        template = self.PROMPT_TEMPLATE if use_detailed_template else self.SIMPLE_PROMPT_TEMPLATE
        
        problem_section = ""
        if problem_description:
            problem_section = f"## Problem Description\n{problem_description}"
        
        final_prompt = template.format(
            structure_summary=structure_summary,
            intentions=intentions.to_prompt_format(),
            code=code,
            problem_section=problem_section,
        )
        
        return AdaptivePromptResult(
            code=code,
            structure=structure,
            intentions=intentions,
            final_prompt=final_prompt,
            structure_summary=structure_summary,
            problem_description=problem_description,
        )
    
    def create_prompt_for_chat(
        self,
        code: str,
        problem_description: str = "",
    ) -> list:
        """
        Create chat-format messages for the fine-tuned model.
        
        Args:
            code: The Python source code
            problem_description: Optional description
            
        Returns:
            List of message dicts suitable for chat template
        """
        result = self.create_adaptive_prompt(code, problem_description)
        
        messages = [
            {
                "role": "user",
                "content": result.final_prompt,
            }
        ]
        
        return messages
    
    def analyze_only(self, code: str) -> Dict[str, Any]:
        """
        Perform only static analysis without intention generation.
        
        Useful for debugging or when you want to inspect
        the extracted structure.
        
        Args:
            code: The Python source code
            
        Returns:
            Dictionary with structure information
        """
        structure = self.code_analyzer.analyze(code)
        summary = self.code_analyzer.get_structure_summary(structure)
        
        return {
            "structure": structure.to_dict(),
            "summary": summary,
        }
    
    def get_intentions_only(
        self,
        code: str,
        problem_description: str = "",
    ) -> Dict[str, Any]:
        """
        Generate only test intentions without full prompt construction.
        
        Useful for debugging or when you want to review
        intentions before generating tests. Uses static analysis only.
        
        Args:
            code: The Python source code
            problem_description: Optional description
            
        Returns:
            Dictionary with intention plan
        """
        structure = self.code_analyzer.analyze(code)
        summary = self.code_analyzer.get_structure_summary(structure)
        
        intentions = self.intention_generator.generate_intentions(
            code=code,
            structure_summary=summary,
            problem_description=problem_description,
        )
        
        return {
            "intentions": intentions.to_dict(),
            "prompt_format": intentions.to_prompt_format(),
        }


class AdaptivePromptBuilder:
    """
    Utility class for building custom adaptive prompts.
    
    Allows more fine-grained control over prompt construction.
    """
    
    def __init__(self):
        self.sections = []
    
    def add_structure(self, structure_summary: str) -> 'AdaptivePromptBuilder':
        """Add code structure section."""
        if structure_summary:
            self.sections.append(f"## Code Structure\n{structure_summary}")
        return self
    
    def add_intentions(self, intentions: IntentionPlan) -> 'AdaptivePromptBuilder':
        """Add test intentions section."""
        self.sections.append(f"## Test Strategy\n{intentions.to_prompt_format()}")
        return self
    
    def add_code(self, code: str) -> 'AdaptivePromptBuilder':
        """Add the code to test."""
        self.sections.append(f"## Code to Test\n```python\n{code}\n```")
        return self
    
    def add_description(self, description: str) -> 'AdaptivePromptBuilder':
        """Add problem description."""
        if description:
            self.sections.append(f"## Problem Description\n{description}")
        return self
    
    def add_custom_section(self, title: str, content: str) -> 'AdaptivePromptBuilder':
        """Add a custom section."""
        self.sections.append(f"## {title}\n{content}")
        return self
    
    def build(self, include_instructions: bool = True) -> str:
        """Build the final prompt."""
        prompt_parts = []
        
        if include_instructions:
            prompt_parts.append(
                "You are an expert Python test engineer. "
                "Write comprehensive unit tests for the provided code."
            )
        
        prompt_parts.extend(self.sections)
        
        if include_instructions:
            prompt_parts.append(
                "\n## Requirements\n"
                "1. Use the unittest framework\n"
                "2. Follow the test intentions as your guide\n"
                "3. Test all identified edge cases and error conditions\n"
                "4. Generate complete, runnable test code"
            )
        
        return '\n\n'.join(prompt_parts)


# Convenience functions
def create_adaptive_prompt(
    code: str,
    problem_description: str = "",
) -> str:
    """
    Quick function to create an adaptive prompt.
    
    Args:
        code: Python source code
        problem_description: Optional description
        
    Returns:
        The constructed prompt string
    """
    prompter = AdaptivePrompter()
    result = prompter.create_adaptive_prompt(code, problem_description)
    return result.final_prompt


if __name__ == "__main__":
    # Example usage
    sample_code = '''
class Calculator:
    """A simple calculator class."""
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b
    
    def divide(self, a: float, b: float) -> float:
        """Divide a by b."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    
    def factorial(self, n: int) -> int:
        """Calculate factorial of n."""
        if n < 0:
            raise ValueError("n must be non-negative")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
'''
    
    # Create adaptive prompt
    prompter = AdaptivePrompter()
    result = prompter.create_adaptive_prompt(
        code=sample_code,
        problem_description="A calculator with basic arithmetic operations",
    )
    
    print("=== Structure Summary ===")
    print(result.structure_summary)
    print("\n=== Test Intentions ===")
    print(result.intentions.to_prompt_format())
    print("\n=== Final Prompt (truncated) ===")
    print(result.final_prompt[:1000] + "...")
