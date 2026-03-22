import json
import logging
import re
from typing import Optional, Callable, List, Dict, Any
from .static_intention_generator import TestIntention, IntentionPlan

logger = logging.getLogger(__name__)

class LLMIntentionGenerator:
    """
    Generates test intentions using an LLM.
    """
    def __init__(self, chat_completion_fn: Callable[[List[Dict[str, str]]], str]):
        self.chat_completion_fn = chat_completion_fn

    def generate_intentions(
        self,
        code: str,
        structure_summary: Optional[str] = None,
        problem_description: Optional[str] = None,
    ) -> IntentionPlan:
        system_prompt = (
            "You are an expert test engineer. Analyze the provided Python code and output test requirements in "
            "strictly valid JSON format. Provide the response as a JSON object with the following keys:\n"
            '1. "intentions": A list of objects with "category" ("normal_case", "edge_case", "error_handling"), '
            '"description" (string), "priority" ("high", "medium", "low"), "inputs" (string suggestions), '
            '"expected_behavior" (string), and "target_function" (string).\n'
            '2. "coverage_goals": A list of strings.\n'
            '3. "boundary_values": A list of strings representing inputs.\n'
            '4. "mock_suggestions": A list of strings (optional, can be empty).'
        )

        user_content = f"Code to Test:\n```python\n{code}\n```\n"
        if problem_description:
            user_content += f"Problem Description:\n{problem_description}\n"
        if structure_summary:
            user_content += f"Structure Summary:\n{structure_summary}\n"

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ]

        logger.info("Requesting LLM to generate test intentions.")
        try:
            response_text = self.chat_completion_fn(messages)
            return self._parse_response(response_text)
        except Exception as e:
            logger.error(f"Error generating intentions from LLM: {e}")
            return IntentionPlan()  # Return empty plan on failure

    def _parse_response(self, text: str) -> IntentionPlan:
        plan = IntentionPlan()
        
        # Try to find JSON in the output
        json_match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', text, re.DOTALL)
        if json_match:
            json_text = json_match.group(1)
        else:
            json_text = text

        try:
            data = json.loads(json_text)
            
            intentions_data = data.get("intentions", [])
            for it in intentions_data:
                plan.intentions.append(TestIntention(
                    category=it.get("category", "normal_case"),
                    description=it.get("description", "Test case"),
                    priority=it.get("priority", "medium"),
                    inputs=it.get("inputs", ""),
                    expected_behavior=it.get("expected_behavior", ""),
                    target_function=it.get("target_function", "")
                ))
            
            plan.coverage_goals = data.get("coverage_goals", [])
            plan.boundary_values = data.get("boundary_values", [])
            plan.mock_suggestions = data.get("mock_suggestions", [])

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON from LLM: {e}\nRaw output:\n{text}")

        return plan
