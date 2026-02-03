"""
Intention Generator Module (Part B - Off-the-Shelf LLM)

Uses an off-the-shelf LLM (Google Gemini or Ollama) to analyze code and generate
test intentions/strategies without actually writing the tests.

This separates the "what to test" (this module) from
"how to write tests" (the fine-tuned model).

Supports two LLM providers:
- Google Gemini API (cloud)
- Ollama API (local)
"""

import os
import json
import re
from typing import List, Optional, Dict, Any
from dataclasses import dataclass, field
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


@dataclass
class TestIntention:
    """A single test intention/strategy."""
    category: str  # e.g., "edge_case", "normal_case", "error_handling"
    description: str  # e.g., "Test division by zero"
    priority: str = "medium"  # high, medium, low
    inputs: Optional[str] = None  # Suggested input values
    expected_behavior: Optional[str] = None  # What should happen
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "category": self.category,
            "description": self.description,
            "priority": self.priority,
            "inputs": self.inputs,
            "expected_behavior": self.expected_behavior,
        }


@dataclass
class IntentionPlan:
    """Collection of test intentions for a piece of code."""
    intentions: List[TestIntention] = field(default_factory=list)
    coverage_goals: List[str] = field(default_factory=list)
    mock_suggestions: List[str] = field(default_factory=list)
    boundary_values: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "intentions": [i.to_dict() for i in self.intentions],
            "coverage_goals": self.coverage_goals,
            "mock_suggestions": self.mock_suggestions,
            "boundary_values": self.boundary_values,
        }
    
    def to_prompt_format(self) -> str:
        """Convert to a format suitable for the test generation prompt."""
        lines = []
        
        if self.intentions:
            lines.append("Test Intentions:")
            for i, intention in enumerate(self.intentions, 1):
                lines.append(f"  {i}. [{intention.category.upper()}] {intention.description}")
                if intention.inputs:
                    lines.append(f"     - Suggested inputs: {intention.inputs}")
                if intention.expected_behavior:
                    lines.append(f"     - Expected: {intention.expected_behavior}")
        
        if self.coverage_goals:
            lines.append("\nCoverage Goals:")
            for goal in self.coverage_goals:
                lines.append(f"  - {goal}")
        
        if self.mock_suggestions:
            lines.append("\nMocking Suggestions:")
            for mock in self.mock_suggestions:
                lines.append(f"  - {mock}")
        
        if self.boundary_values:
            lines.append("\nBoundary Values to Test:")
            for bv in self.boundary_values:
                lines.append(f"  - {bv}")
        
        return '\n'.join(lines)


class IntentionGenerator:
    """
    Generates test intentions using an off-the-shelf LLM.
    
    Supports two providers:
    - Google Gemini API (cloud-based)
    - Ollama API (local models)
    
    Uses a cheap/fast model to analyze code and determine what
    aspects need to be tested, without writing the actual tests.
    """
    
    # System prompt for the planner
    SYSTEM_PROMPT = """You are an expert test planning assistant. Your job is to analyze Python code and identify what needs to be tested.

You will be given Python code and possibly its structure analysis. Your task is to:
1. Identify critical test cases (normal, edge cases, error handling)
2. Suggest boundary values to test
3. Identify any external dependencies that might need mocking
4. Prioritize test cases by importance

Output your analysis as JSON with the following structure:
{
    "intentions": [
        {
            "category": "normal_case|edge_case|error_handling|boundary|integration",
            "description": "What to test",
            "priority": "high|medium|low",
            "inputs": "Suggested input values",
            "expected_behavior": "What should happen"
        }
    ],
    "coverage_goals": ["List of code paths/branches to cover"],
    "mock_suggestions": ["External dependencies to mock"],
    "boundary_values": ["Specific boundary values to test"]
}

Focus on WHAT to test, not HOW to write the test code. Be specific and actionable.
Limit to 5-7 most important test intentions to avoid overwhelming the test generator."""

    def __init__(
        self,
        model: str = "gemini-2.0-flash",
        api_key: Optional[str] = None,
        temperature: float = 0.3,  # Lower for more focused analysis
        max_tokens: int = 1024,
        provider: Optional[str] = None,  # "google" or "ollama"
        ollama_host: Optional[str] = None,
    ):
        """
        Initialize the intention generator.
        
        Args:
            model: The model to use for planning
            api_key: Google API key (uses GEMINI_API_KEY env var if not provided)
            temperature: Sampling temperature (lower = more focused)
            max_tokens: Maximum tokens to generate
            provider: LLM provider ("google" or "ollama"), uses LLM_PROVIDER env var if not set
            ollama_host: Ollama server URL (uses OLLAMA_HOST env var if not provided)
        """
        self.model = model
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.provider = provider or os.environ.get("LLM_PROVIDER", "google").lower()
        self.ollama_host = ollama_host or os.environ.get("OLLAMA_HOST", "http://localhost:11434")
        self._client = None
        self._ollama_client = None
        
        # Validate provider
        if self.provider not in ("google", "ollama"):
            print(f"Warning: Unknown provider '{self.provider}', defaulting to 'google'")
            self.provider = "google"
        
        if self.provider == "google" and not self.api_key:
            print("Warning: No Gemini API key found. Set GEMINI_API_KEY in .env file.")
        
        print(f"IntentionGenerator initialized with provider: {self.provider}, model: {self.model}")
    
    def _get_google_client(self):
        """Lazy initialization of Google Gemini client."""
        if self._client is None:
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                self._client = genai.GenerativeModel(
                    self.model,
                    system_instruction=self.SYSTEM_PROMPT,
                )
            except ImportError:
                raise ImportError(
                    "Please install google-generativeai: pip install google-generativeai"
                )
        return self._client
    
    def _get_ollama_client(self):
        """Lazy initialization of Ollama client."""
        if self._ollama_client is None:
            try:
                from ollama import Client
                self._ollama_client = Client(host=self.ollama_host)
            except ImportError:
                raise ImportError(
                    "Please install ollama: pip install ollama"
                )
        return self._ollama_client
    
    def _generate_with_google(self, prompt: str) -> str:
        """Generate response using Google Gemini API."""
        client = self._get_google_client()
        
        generation_config = {
            "temperature": self.temperature,
            "max_output_tokens": self.max_tokens,
            "response_mime_type": "application/json",
        }
        
        response = client.generate_content(
            prompt,
            generation_config=generation_config,
        )
        
        return response.text
    
    def _generate_with_ollama(self, prompt: str) -> str:
        """Generate response using Ollama API."""
        client = self._get_ollama_client()
        
        # Build messages with system prompt
        messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {"role": "user", "content": prompt + "\n\nRespond with valid JSON only."},
        ]
        
        response = client.chat(
            model=self.model,
            messages=messages,
            options={
                "temperature": self.temperature,
                "num_predict": self.max_tokens,
            },
        )
        
        return response.message.content
    
    def generate_intentions(
        self,
        code: str,
        structure_summary: Optional[str] = None,
        problem_description: Optional[str] = None,
    ) -> IntentionPlan:
        """
        Generate test intentions for the given code.
        
        Args:
            code: The Python source code to analyze
            structure_summary: Optional pre-analyzed code structure
            problem_description: Optional description of what the code does
            
        Returns:
            IntentionPlan containing test strategies
        """
        # Build the analysis prompt
        prompt_parts = []
        
        if problem_description:
            prompt_parts.append(f"## Problem Description\n{problem_description}")
        
        if structure_summary:
            prompt_parts.append(f"## Code Structure Analysis\n{structure_summary}")
        
        prompt_parts.append(f"## Code to Analyze\n```python\n{code}\n```")
        prompt_parts.append(
            "\nAnalyze this code and provide a JSON test plan. "
            "Focus on critical test cases, edge cases, and error handling."
        )
        
        prompt = '\n\n'.join(prompt_parts)
        
        try:
            # Use the appropriate provider
            if self.provider == "ollama":
                response_text = self._generate_with_ollama(prompt)
            else:
                response_text = self._generate_with_google(prompt)
            
            # Parse the response
            return self._parse_response(response_text)
            
        except Exception as e:
            print(f"Warning: Intention generation failed: {e}")
            # Return fallback intentions
            return self._generate_fallback_intentions(code)
    
    def _parse_response(self, response_text: str) -> IntentionPlan:
        """Parse the LLM response into an IntentionPlan."""
        try:
            # Try to extract JSON from the response
            json_match = re.search(r'\{[\s\S]*\}', response_text)
            if json_match:
                data = json.loads(json_match.group())
            else:
                data = json.loads(response_text)
            
            plan = IntentionPlan()
            
            # Parse intentions
            for item in data.get("intentions", []):
                intention = TestIntention(
                    category=item.get("category", "normal_case"),
                    description=item.get("description", ""),
                    priority=item.get("priority", "medium"),
                    inputs=item.get("inputs"),
                    expected_behavior=item.get("expected_behavior"),
                )
                plan.intentions.append(intention)
            
            plan.coverage_goals = data.get("coverage_goals", [])
            plan.mock_suggestions = data.get("mock_suggestions", [])
            plan.boundary_values = data.get("boundary_values", [])
            
            return plan
            
        except json.JSONDecodeError as e:
            print(f"Warning: Failed to parse JSON response: {e}")
            # Try to extract intentions from plain text
            return self._parse_text_response(response_text)
    
    def _parse_text_response(self, text: str) -> IntentionPlan:
        """Fallback parser for non-JSON responses."""
        plan = IntentionPlan()
        
        # Look for numbered items
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Match patterns like "1. Test..." or "- Test..."
            if re.match(r'^[\d\-\*\.]+\s*', line):
                description = re.sub(r'^[\d\-\*\.]+\s*', '', line)
                if description:
                    # Try to categorize based on keywords
                    category = "normal_case"
                    if any(kw in description.lower() for kw in ["edge", "boundary", "limit"]):
                        category = "edge_case"
                    elif any(kw in description.lower() for kw in ["error", "exception", "invalid", "fail"]):
                        category = "error_handling"
                    elif any(kw in description.lower() for kw in ["zero", "empty", "null", "none"]):
                        category = "boundary"
                    
                    plan.intentions.append(TestIntention(
                        category=category,
                        description=description,
                    ))
        
        return plan
    
    def _generate_fallback_intentions(self, code: str) -> IntentionPlan:
        """Generate basic intentions when LLM fails."""
        plan = IntentionPlan()
        
        # Basic heuristic-based intentions
        plan.intentions = [
            TestIntention(
                category="normal_case",
                description="Test with typical valid inputs",
                priority="high",
            ),
            TestIntention(
                category="edge_case",
                description="Test with empty/zero/minimal inputs",
                priority="high",
            ),
            TestIntention(
                category="error_handling",
                description="Test with invalid inputs that should raise exceptions",
                priority="medium",
            ),
        ]
        
        # Add more specific intentions based on code analysis
        if "def " in code:
            # Check for division
            if "/" in code or "divide" in code.lower():
                plan.intentions.append(TestIntention(
                    category="error_handling",
                    description="Test division by zero",
                    priority="high",
                    inputs="divisor = 0",
                    expected_behavior="Should raise ZeroDivisionError",
                ))
            
            # Check for list/array operations
            if "list" in code.lower() or "[" in code:
                plan.intentions.append(TestIntention(
                    category="edge_case",
                    description="Test with empty list",
                    priority="medium",
                    inputs="[]",
                ))
            
            # Check for string operations
            if "str" in code.lower() or '""' in code or "''" in code:
                plan.intentions.append(TestIntention(
                    category="edge_case",
                    description="Test with empty string",
                    priority="medium",
                    inputs='""',
                ))
        
        plan.coverage_goals = [
            "All function branches should be covered",
            "All exception handlers should be triggered",
        ]
        
        return plan


class MockIntentionGenerator:
    """
    Mock intention generator for testing without API access.
    """
    
    def __init__(self, model: str = "mock"):
        self.model = model
    
    def generate_intentions(
        self,
        code: str,
        structure_summary: Optional[str] = None,
        problem_description: Optional[str] = None,
    ) -> IntentionPlan:
        """Generate mock intentions based on simple code analysis."""
        plan = IntentionPlan()
        
        # Basic pattern matching for common test scenarios
        intentions = [
            TestIntention(
                category="normal_case",
                description="Test with standard positive inputs",
                priority="high",
            ),
            TestIntention(
                category="edge_case",
                description="Test boundary conditions",
                priority="high",
            ),
            TestIntention(
                category="error_handling",
                description="Test error handling paths",
                priority="medium",
            ),
        ]
        
        plan.intentions = intentions
        plan.coverage_goals = ["Achieve 80% code coverage"]
        
        return plan


if __name__ == "__main__":
    # Example usage
    sample_code = '''
def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def factorial(n: int) -> int:
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    return n * factorial(n - 1)
'''
    
    # Use mock generator for testing
    generator = MockIntentionGenerator()
    plan = generator.generate_intentions(sample_code)
    print(plan.to_prompt_format())
