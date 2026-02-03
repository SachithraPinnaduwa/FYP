"""
Static Intention Generator Module

Generates test intentions using comprehensive static analysis only.
No AI/LLM required - pure AST-based analysis.

Analyzes:
- Function/method signatures and types
- Control flow (if/else, loops, try/except)
- Data flow patterns
- Boundary conditions
- Error handling patterns
- Common code patterns (division, list ops, string ops, etc.)
- Docstrings and examples
- Dependencies and external calls
"""

import ast
import re
from typing import List, Optional, Dict, Any, Set, Tuple
from dataclasses import dataclass, field


@dataclass
class TestIntention:
    """A single test intention/strategy."""
    category: str  # e.g., "edge_case", "normal_case", "error_handling"
    description: str  # e.g., "Test division by zero"
    priority: str = "medium"  # high, medium, low
    inputs: Optional[str] = None  # Suggested input values
    expected_behavior: Optional[str] = None  # What should happen
    target_function: Optional[str] = None  # Which function this targets
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "category": self.category,
            "description": self.description,
            "priority": self.priority,
            "inputs": self.inputs,
            "expected_behavior": self.expected_behavior,
            "target_function": self.target_function,
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
                target = f" ({intention.target_function})" if intention.target_function else ""
                lines.append(f"  {i}. [{intention.category.upper()}]{target} {intention.description}")
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


class StaticIntentionGenerator:
    """
    Generates test intentions using comprehensive static analysis.
    
    Analyzes code structure, control flow, and patterns to determine
    what needs to be tested without requiring any AI/LLM.
    """
    
    # Common patterns that indicate specific test needs
    DIVISION_OPS = {'/', '//', '%'}
    COMPARISON_OPS = {'<', '>', '<=', '>=', '==', '!='}
    COLLECTION_TYPES = {'list', 'dict', 'set', 'tuple', 'List', 'Dict', 'Set', 'Tuple'}
    STRING_METHODS = {'split', 'strip', 'replace', 'find', 'index', 'join', 'format', 'lower', 'upper'}
    FILE_METHODS = {'open', 'read', 'write', 'close'}
    NETWORK_MODULES = {'requests', 'urllib', 'http', 'socket', 'aiohttp'}
    DB_MODULES = {'sqlite3', 'psycopg2', 'mysql', 'sqlalchemy', 'pymongo'}
    
    def __init__(self):
        self._current_function: Optional[str] = None
        self._exceptions_raised: Set[str] = set()
        self._external_calls: Set[str] = set()
        self._has_recursion: bool = False
        self._loop_vars: Set[str] = set()
        self._conditional_branches: int = 0
        self._parameters_info: Dict[str, List[Tuple[str, Optional[str], Optional[str]]]] = {}
        
    def generate_intentions(
        self,
        code: str,
        structure_summary: Optional[str] = None,
        problem_description: Optional[str] = None,
    ) -> IntentionPlan:
        """
        Generate test intentions using static analysis.
        
        Args:
            code: The Python source code to analyze
            structure_summary: Optional pre-analyzed code structure (used for context)
            problem_description: Optional description of what the code does
            
        Returns:
            IntentionPlan containing test strategies
        """
        plan = IntentionPlan()
        
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            # Handle parse errors gracefully
            plan.intentions.append(TestIntention(
                category="error_handling",
                description="Code has syntax errors - fix before testing",
                priority="high",
            ))
            return plan
        
        # Reset analysis state
        self._reset_state()
        
        # Analyze the AST
        self._analyze_tree(tree)
        
        # Generate intentions based on analysis
        self._generate_function_intentions(tree, plan)
        self._generate_class_intentions(tree, plan)
        self._generate_control_flow_intentions(tree, plan)
        self._generate_error_handling_intentions(tree, plan)
        self._generate_data_type_intentions(tree, plan)
        self._generate_edge_case_intentions(tree, plan)
        self._generate_mock_suggestions(tree, plan)
        self._generate_coverage_goals(tree, plan)
        self._generate_boundary_values(tree, plan)
        
        # Enhance with problem description if provided
        if problem_description:
            self._enhance_with_description(problem_description, plan)
        
        # Sort by priority and deduplicate
        plan.intentions = self._prioritize_and_dedupe(plan.intentions)
        
        return plan
    
    def _reset_state(self):
        """Reset analysis state for new code."""
        self._current_function = None
        self._exceptions_raised = set()
        self._external_calls = set()
        self._has_recursion = False
        self._loop_vars = set()
        self._conditional_branches = 0
        self._parameters_info = {}
    
    def _analyze_tree(self, tree: ast.AST):
        """First pass: gather information about the code."""
        for node in ast.walk(tree):
            # Track exceptions raised
            if isinstance(node, ast.Raise):
                if node.exc:
                    if isinstance(node.exc, ast.Call):
                        if isinstance(node.exc.func, ast.Name):
                            self._exceptions_raised.add(node.exc.func.id)
                        elif isinstance(node.exc.func, ast.Attribute):
                            self._exceptions_raised.add(node.exc.func.attr)
                    elif isinstance(node.exc, ast.Name):
                        self._exceptions_raised.add(node.exc.id)
            
            # Track function calls
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Attribute):
                    self._external_calls.add(node.func.attr)
                elif isinstance(node.func, ast.Name):
                    self._external_calls.add(node.func.id)
            
            # Count conditional branches
            if isinstance(node, (ast.If, ast.IfExp)):
                self._conditional_branches += 1
            
            # Track loop variables
            if isinstance(node, ast.For):
                if isinstance(node.target, ast.Name):
                    self._loop_vars.add(node.target.id)
    
    def _generate_function_intentions(self, tree: ast.AST, plan: IntentionPlan):
        """Generate intentions based on function analysis."""
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                func_name = node.name
                
                # Skip private/dunder methods for now unless they're special
                if func_name.startswith('_') and not func_name.startswith('__'):
                    continue
                
                # Analyze parameters
                params = self._extract_params(node)
                self._parameters_info[func_name] = params
                
                # Check for recursion
                if self._is_recursive(node, func_name):
                    plan.intentions.append(TestIntention(
                        category="edge_case",
                        description=f"Test recursion base case and termination",
                        priority="high",
                        target_function=func_name,
                        expected_behavior="Should terminate without stack overflow",
                    ))
                    plan.intentions.append(TestIntention(
                        category="edge_case",
                        description=f"Test with input that causes deep recursion",
                        priority="medium",
                        target_function=func_name,
                        expected_behavior="May raise RecursionError for very deep calls",
                    ))
                
                # Generate param-based intentions
                for param_name, param_type, default in params:
                    if param_name == 'self':
                        continue
                    
                    if param_type:
                        self._generate_type_specific_intentions(
                            plan, func_name, param_name, param_type, default
                        )
                    else:
                        # No type hint - suggest testing multiple types
                        plan.intentions.append(TestIntention(
                            category="normal_case",
                            description=f"Test '{param_name}' with various valid input types",
                            priority="medium",
                            target_function=func_name,
                        ))
                
                # Check return type
                if node.returns:
                    return_type = ast.unparse(node.returns) if hasattr(ast, 'unparse') else str(node.returns)
                    plan.intentions.append(TestIntention(
                        category="normal_case",
                        description=f"Verify return value matches expected type: {return_type}",
                        priority="high",
                        target_function=func_name,
                        expected_behavior=f"Should return {return_type}",
                    ))
                
                # Check for docstring examples
                docstring = ast.get_docstring(node)
                if docstring:
                    examples = self._extract_doctest_examples(docstring)
                    if examples:
                        plan.intentions.append(TestIntention(
                            category="normal_case",
                            description=f"Test documented examples from docstring",
                            priority="high",
                            target_function=func_name,
                            inputs="; ".join(examples[:3]),
                        ))
    
    def _generate_class_intentions(self, tree: ast.AST, plan: IntentionPlan):
        """Generate intentions based on class analysis."""
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_name = node.name
                
                # Check for __init__
                has_init = any(
                    isinstance(m, ast.FunctionDef) and m.name == '__init__'
                    for m in node.body
                )
                
                if has_init:
                    plan.intentions.append(TestIntention(
                        category="normal_case",
                        description=f"Test {class_name} instantiation with valid parameters",
                        priority="high",
                        target_function=f"{class_name}.__init__",
                    ))
                    plan.intentions.append(TestIntention(
                        category="error_handling",
                        description=f"Test {class_name} instantiation with invalid parameters",
                        priority="medium",
                        target_function=f"{class_name}.__init__",
                    ))
                
                # Check for state-modifying methods
                modifying_methods = []
                for m in node.body:
                    if isinstance(m, ast.FunctionDef) and not m.name.startswith('_'):
                        # Check if method modifies self
                        if self._modifies_self(m):
                            modifying_methods.append(m.name)
                
                if modifying_methods:
                    plan.intentions.append(TestIntention(
                        category="integration",
                        description=f"Test state consistency after calling: {', '.join(modifying_methods)}",
                        priority="medium",
                        target_function=class_name,
                    ))
                
                # Check for inheritance
                if node.bases:
                    base_names = [ast.unparse(b) if hasattr(ast, 'unparse') else 'base' for b in node.bases]
                    plan.intentions.append(TestIntention(
                        category="normal_case",
                        description=f"Test inherited behavior from: {', '.join(base_names)}",
                        priority="medium",
                        target_function=class_name,
                    ))
    
    def _generate_control_flow_intentions(self, tree: ast.AST, plan: IntentionPlan):
        """Generate intentions based on control flow analysis."""
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                func_name = node.name
                if func_name.startswith('_') and not func_name.startswith('__'):
                    continue
                
                # Analyze control flow within function
                branches = self._count_branches(node)
                loops = self._count_loops(node)
                
                if branches > 1:
                    plan.intentions.append(TestIntention(
                        category="branch_coverage",
                        description=f"Test all {branches} conditional branches",
                        priority="high",
                        target_function=func_name,
                        expected_behavior="Each branch should be covered by at least one test",
                    ))
                
                if loops > 0:
                    plan.intentions.append(TestIntention(
                        category="edge_case",
                        description=f"Test loop boundary conditions (zero iterations, one iteration, many)",
                        priority="high",
                        target_function=func_name,
                    ))
                
                # Check for early returns
                early_returns = self._count_early_returns(node)
                if early_returns > 0:
                    plan.intentions.append(TestIntention(
                        category="branch_coverage",
                        description=f"Test conditions that trigger early return",
                        priority="medium",
                        target_function=func_name,
                    ))
    
    def _generate_error_handling_intentions(self, tree: ast.AST, plan: IntentionPlan):
        """Generate intentions based on error handling patterns."""
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                func_name = node.name
                if func_name.startswith('_') and not func_name.startswith('__'):
                    continue
                
                # Find raised exceptions
                exceptions = self._find_raised_exceptions(node)
                for exc_name, condition in exceptions:
                    plan.intentions.append(TestIntention(
                        category="error_handling",
                        description=f"Test that {exc_name} is raised correctly",
                        priority="high",
                        target_function=func_name,
                        inputs=condition if condition else None,
                        expected_behavior=f"Should raise {exc_name}",
                    ))
                
                # Find try/except blocks
                try_blocks = self._find_try_blocks(node)
                for exc_types in try_blocks:
                    for exc_type in exc_types:
                        plan.intentions.append(TestIntention(
                            category="error_handling",
                            description=f"Test exception handler for {exc_type}",
                            priority="medium",
                            target_function=func_name,
                            expected_behavior=f"Should handle {exc_type} gracefully",
                        ))
    
    def _generate_data_type_intentions(self, tree: ast.AST, plan: IntentionPlan):
        """Generate intentions based on data type usage."""
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                func_name = node.name
                if func_name.startswith('_') and not func_name.startswith('__'):
                    continue
                
                # Check for division operations
                if self._has_operation(node, ast.Div) or self._has_operation(node, ast.FloorDiv) or self._has_operation(node, ast.Mod):
                    plan.intentions.append(TestIntention(
                        category="error_handling",
                        description="Test division by zero",
                        priority="high",
                        target_function=func_name,
                        inputs="divisor = 0",
                        expected_behavior="Should raise ZeroDivisionError or handle gracefully",
                    ))
                
                # Check for indexing operations
                if self._has_subscript(node):
                    plan.intentions.append(TestIntention(
                        category="edge_case",
                        description="Test with empty collection (index out of bounds)",
                        priority="high",
                        target_function=func_name,
                        inputs="empty list/dict",
                        expected_behavior="Should handle empty input or raise IndexError/KeyError",
                    ))
                    plan.intentions.append(TestIntention(
                        category="edge_case",
                        description="Test with negative indices",
                        priority="medium",
                        target_function=func_name,
                    ))
                
                # Check for string operations
                if self._has_string_methods(node):
                    plan.intentions.append(TestIntention(
                        category="edge_case",
                        description="Test with empty string",
                        priority="medium",
                        target_function=func_name,
                        inputs='""',
                    ))
                    plan.intentions.append(TestIntention(
                        category="edge_case",
                        description="Test with special characters (unicode, whitespace)",
                        priority="low",
                        target_function=func_name,
                    ))
                
                # Check for numeric operations that might overflow
                if self._has_numeric_operations(node):
                    plan.intentions.append(TestIntention(
                        category="boundary",
                        description="Test with large numbers",
                        priority="medium",
                        target_function=func_name,
                        inputs="Very large positive/negative integers",
                    ))
                    plan.intentions.append(TestIntention(
                        category="boundary",
                        description="Test with floating point edge cases",
                        priority="low",
                        target_function=func_name,
                        inputs="float('inf'), float('-inf'), float('nan')",
                    ))
    
    def _generate_edge_case_intentions(self, tree: ast.AST, plan: IntentionPlan):
        """Generate edge case intentions."""
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                func_name = node.name
                if func_name.startswith('_') and not func_name.startswith('__'):
                    continue
                
                params = self._extract_params(node)
                
                for param_name, param_type, default in params:
                    if param_name == 'self':
                        continue
                    
                    # None handling
                    if default is None and param_type != 'None':
                        plan.intentions.append(TestIntention(
                            category="edge_case",
                            description=f"Test with {param_name}=None",
                            priority="medium",
                            target_function=func_name,
                            inputs=f"{param_name}=None",
                            expected_behavior="Should handle None or raise TypeError",
                        ))
                    
                    # Check for Optional type
                    if param_type and 'Optional' in param_type:
                        plan.intentions.append(TestIntention(
                            category="normal_case",
                            description=f"Test {param_name} with None (Optional type)",
                            priority="high",
                            target_function=func_name,
                            inputs=f"{param_name}=None",
                        ))
    
    def _generate_mock_suggestions(self, tree: ast.AST, plan: IntentionPlan):
        """Generate suggestions for what to mock."""
        imports = set()
        external_calls = set()
        
        for node in ast.walk(tree):
            # Collect imports
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module.split('.')[0])
            
            # Collect external calls
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Attribute):
                    external_calls.add(node.func.attr)
        
        # Check for network calls
        for mod in self.NETWORK_MODULES:
            if mod in imports:
                plan.mock_suggestions.append(f"Mock network calls from {mod}")
        
        # Check for database calls
        for mod in self.DB_MODULES:
            if mod in imports:
                plan.mock_suggestions.append(f"Mock database operations from {mod}")
        
        # Check for file operations
        if 'open' in external_calls or any(m in external_calls for m in self.FILE_METHODS):
            plan.mock_suggestions.append("Mock file I/O operations")
        
        # Check for time/date
        if 'datetime' in imports or 'time' in imports:
            plan.mock_suggestions.append("Mock datetime/time for deterministic tests")
        
        # Check for random
        if 'random' in imports:
            plan.mock_suggestions.append("Mock random for reproducible tests")
        
        # Check for os/sys
        if 'os' in imports:
            plan.mock_suggestions.append("Mock os module for filesystem operations")
        if 'sys' in imports:
            plan.mock_suggestions.append("Consider mocking sys module if testing CLI behavior")
    
    def _generate_coverage_goals(self, tree: ast.AST, plan: IntentionPlan):
        """Generate coverage goals."""
        total_functions = 0
        total_classes = 0
        total_branches = 0
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if not node.name.startswith('_') or node.name.startswith('__'):
                    total_functions += 1
                    total_branches += self._count_branches(node)
            elif isinstance(node, ast.ClassDef):
                total_classes += 1
        
        if total_functions > 0:
            plan.coverage_goals.append(f"Test all {total_functions} public functions")
        
        if total_classes > 0:
            plan.coverage_goals.append(f"Test all {total_classes} classes with instantiation and method calls")
        
        if total_branches > 2:
            plan.coverage_goals.append(f"Cover all {total_branches} conditional branches")
        
        if self._exceptions_raised:
            plan.coverage_goals.append(f"Trigger all {len(self._exceptions_raised)} explicit exceptions")
        
        plan.coverage_goals.append("Achieve at least 80% line coverage")
    
    def _generate_boundary_values(self, tree: ast.AST, plan: IntentionPlan):
        """Generate boundary values to test."""
        for func_name, params in self._parameters_info.items():
            for param_name, param_type, default in params:
                if param_name == 'self':
                    continue
                
                if param_type:
                    type_lower = param_type.lower()
                    
                    if 'int' in type_lower:
                        plan.boundary_values.extend([
                            f"{param_name}=0 (zero)",
                            f"{param_name}=1 (one)",
                            f"{param_name}=-1 (negative one)",
                            f"{param_name}=2**31-1 (max 32-bit int)",
                        ])
                    elif 'float' in type_lower:
                        plan.boundary_values.extend([
                            f"{param_name}=0.0",
                            f"{param_name}=1.0",
                            f"{param_name}=-1.0",
                            f"{param_name}=very small positive (1e-10)",
                        ])
                    elif 'str' in type_lower:
                        plan.boundary_values.extend([
                            f"{param_name}='' (empty string)",
                            f"{param_name}='a' (single char)",
                            f"{param_name}=very long string",
                        ])
                    elif any(c in type_lower for c in ['list', 'set', 'tuple']):
                        plan.boundary_values.extend([
                            f"{param_name}=[] (empty)",
                            f"{param_name}=[single_element]",
                            f"{param_name}=large collection",
                        ])
        
        # Deduplicate
        plan.boundary_values = list(dict.fromkeys(plan.boundary_values))
    
    def _enhance_with_description(self, description: str, plan: IntentionPlan):
        """Enhance intentions based on problem description."""
        desc_lower = description.lower()
        
        # Look for keywords in description
        if 'sort' in desc_lower or 'order' in desc_lower:
            plan.intentions.append(TestIntention(
                category="normal_case",
                description="Test that output is correctly sorted/ordered",
                priority="high",
            ))
            plan.intentions.append(TestIntention(
                category="edge_case",
                description="Test already sorted input",
                priority="medium",
            ))
            plan.intentions.append(TestIntention(
                category="edge_case",
                description="Test reverse sorted input",
                priority="medium",
            ))
        
        if 'search' in desc_lower or 'find' in desc_lower:
            plan.intentions.append(TestIntention(
                category="normal_case",
                description="Test finding existing element",
                priority="high",
            ))
            plan.intentions.append(TestIntention(
                category="edge_case",
                description="Test element not found",
                priority="high",
            ))
        
        if 'valid' in desc_lower or 'validate' in desc_lower:
            plan.intentions.append(TestIntention(
                category="normal_case",
                description="Test with valid input",
                priority="high",
            ))
            plan.intentions.append(TestIntention(
                category="error_handling",
                description="Test with invalid input",
                priority="high",
            ))
        
        if 'cache' in desc_lower or 'memo' in desc_lower:
            plan.intentions.append(TestIntention(
                category="integration",
                description="Test cache behavior (multiple calls with same input)",
                priority="medium",
            ))
    
    # Helper methods
    
    def _extract_params(self, node: ast.FunctionDef) -> List[Tuple[str, Optional[str], Optional[str]]]:
        """Extract parameters with types and defaults."""
        params = []
        args = node.args
        
        num_args = len(args.args)
        num_defaults = len(args.defaults)
        defaults_offset = num_args - num_defaults
        
        for i, arg in enumerate(args.args):
            type_hint = None
            default = None
            
            if arg.annotation:
                try:
                    type_hint = ast.unparse(arg.annotation)
                except:
                    type_hint = str(arg.annotation)
            
            default_idx = i - defaults_offset
            if default_idx >= 0 and default_idx < len(args.defaults):
                try:
                    default = ast.unparse(args.defaults[default_idx])
                except:
                    default = "default"
            
            params.append((arg.arg, type_hint, default))
        
        return params
    
    def _is_recursive(self, node: ast.FunctionDef, func_name: str) -> bool:
        """Check if function is recursive."""
        for child in ast.walk(node):
            if isinstance(child, ast.Call):
                if isinstance(child.func, ast.Name) and child.func.id == func_name:
                    return True
        return False
    
    def _modifies_self(self, node: ast.FunctionDef) -> bool:
        """Check if method modifies self attributes."""
        for child in ast.walk(node):
            if isinstance(child, ast.Assign):
                for target in child.targets:
                    if isinstance(target, ast.Attribute):
                        if isinstance(target.value, ast.Name) and target.value.id == 'self':
                            return True
        return False
    
    def _count_branches(self, node: ast.AST) -> int:
        """Count conditional branches in a node."""
        count = 0
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.IfExp)):
                count += 1
                # Count elif as additional branches
                if isinstance(child, ast.If) and child.orelse:
                    for else_child in child.orelse:
                        if isinstance(else_child, ast.If):
                            count += 1
        return count
    
    def _count_loops(self, node: ast.AST) -> int:
        """Count loops in a node."""
        count = 0
        for child in ast.walk(node):
            if isinstance(child, (ast.For, ast.While, ast.AsyncFor)):
                count += 1
        return count
    
    def _count_early_returns(self, node: ast.FunctionDef) -> int:
        """Count return statements that aren't the last statement."""
        returns = []
        for child in ast.walk(node):
            if isinstance(child, ast.Return):
                returns.append(child)
        
        # More than one return usually means early returns
        return max(0, len(returns) - 1)
    
    def _find_raised_exceptions(self, node: ast.AST) -> List[Tuple[str, Optional[str]]]:
        """Find exceptions raised with conditions."""
        exceptions = []
        for child in ast.walk(node):
            if isinstance(child, ast.Raise):
                exc_name = None
                condition = None
                
                if child.exc:
                    if isinstance(child.exc, ast.Call):
                        if isinstance(child.exc.func, ast.Name):
                            exc_name = child.exc.func.id
                        elif isinstance(child.exc.func, ast.Attribute):
                            exc_name = child.exc.func.attr
                    elif isinstance(child.exc, ast.Name):
                        exc_name = child.exc.id
                
                if exc_name:
                    # Try to find the condition
                    parent = self._find_parent_if(node, child)
                    if parent:
                        try:
                            condition = ast.unparse(parent.test)
                        except:
                            pass
                    
                    exceptions.append((exc_name, condition))
        
        return exceptions
    
    def _find_parent_if(self, root: ast.AST, target: ast.AST) -> Optional[ast.If]:
        """Find parent If node of target."""
        for node in ast.walk(root):
            if isinstance(node, ast.If):
                for child in ast.walk(node):
                    if child is target:
                        return node
        return None
    
    def _find_try_blocks(self, node: ast.AST) -> List[List[str]]:
        """Find exception types handled in try blocks."""
        result = []
        for child in ast.walk(node):
            if isinstance(child, ast.Try):
                exc_types = []
                for handler in child.handlers:
                    if handler.type:
                        try:
                            exc_types.append(ast.unparse(handler.type))
                        except:
                            exc_types.append("Exception")
                    else:
                        exc_types.append("Exception (bare except)")
                if exc_types:
                    result.append(exc_types)
        return result
    
    def _has_operation(self, node: ast.AST, op_type) -> bool:
        """Check if node contains a specific operation type."""
        for child in ast.walk(node):
            if isinstance(child, ast.BinOp):
                if isinstance(child.op, op_type):
                    return True
        return False
    
    def _has_subscript(self, node: ast.AST) -> bool:
        """Check if node contains subscript operations."""
        for child in ast.walk(node):
            if isinstance(child, ast.Subscript):
                return True
        return False
    
    def _has_string_methods(self, node: ast.AST) -> bool:
        """Check if node uses string methods."""
        for child in ast.walk(node):
            if isinstance(child, ast.Call):
                if isinstance(child.func, ast.Attribute):
                    if child.func.attr in self.STRING_METHODS:
                        return True
        return False
    
    def _has_numeric_operations(self, node: ast.AST) -> bool:
        """Check if node has numeric operations."""
        for child in ast.walk(node):
            if isinstance(child, ast.BinOp):
                if isinstance(child.op, (ast.Add, ast.Sub, ast.Mult, ast.Pow)):
                    return True
        return False
    
    def _extract_doctest_examples(self, docstring: str) -> List[str]:
        """Extract doctest examples from docstring."""
        examples = []
        pattern = r'>>>\s*(.+)'
        matches = re.findall(pattern, docstring)
        examples.extend(matches)
        return examples
    
    def _generate_type_specific_intentions(
        self, plan: IntentionPlan, func_name: str, param_name: str, param_type: str, default: Optional[str]
    ):
        """Generate intentions based on parameter type."""
        type_lower = param_type.lower()
        
        if 'int' in type_lower:
            plan.intentions.append(TestIntention(
                category="normal_case",
                description=f"Test {param_name} with positive integer",
                priority="high",
                target_function=func_name,
                inputs=f"{param_name}=5",
            ))
            plan.intentions.append(TestIntention(
                category="edge_case",
                description=f"Test {param_name} with zero",
                priority="high",
                target_function=func_name,
                inputs=f"{param_name}=0",
            ))
            plan.intentions.append(TestIntention(
                category="edge_case",
                description=f"Test {param_name} with negative integer",
                priority="medium",
                target_function=func_name,
                inputs=f"{param_name}=-1",
            ))
        
        elif 'float' in type_lower:
            plan.intentions.append(TestIntention(
                category="normal_case",
                description=f"Test {param_name} with float values",
                priority="high",
                target_function=func_name,
            ))
            plan.intentions.append(TestIntention(
                category="edge_case",
                description=f"Test {param_name} with zero",
                priority="medium",
                target_function=func_name,
                inputs=f"{param_name}=0.0",
            ))
        
        elif 'str' in type_lower:
            plan.intentions.append(TestIntention(
                category="normal_case",
                description=f"Test {param_name} with normal string",
                priority="high",
                target_function=func_name,
            ))
            plan.intentions.append(TestIntention(
                category="edge_case",
                description=f"Test {param_name} with empty string",
                priority="high",
                target_function=func_name,
                inputs=f'{param_name}=""',
            ))
        
        elif 'list' in type_lower or 'List' in param_type:
            plan.intentions.append(TestIntention(
                category="normal_case",
                description=f"Test {param_name} with populated list",
                priority="high",
                target_function=func_name,
            ))
            plan.intentions.append(TestIntention(
                category="edge_case",
                description=f"Test {param_name} with empty list",
                priority="high",
                target_function=func_name,
                inputs=f"{param_name}=[]",
            ))
            plan.intentions.append(TestIntention(
                category="edge_case",
                description=f"Test {param_name} with single element list",
                priority="medium",
                target_function=func_name,
            ))
        
        elif 'dict' in type_lower or 'Dict' in param_type:
            plan.intentions.append(TestIntention(
                category="normal_case",
                description=f"Test {param_name} with populated dict",
                priority="high",
                target_function=func_name,
            ))
            plan.intentions.append(TestIntention(
                category="edge_case",
                description=f"Test {param_name} with empty dict",
                priority="high",
                target_function=func_name,
                inputs=f"{param_name}={{}}",
            ))
        
        elif 'bool' in type_lower:
            plan.intentions.append(TestIntention(
                category="normal_case",
                description=f"Test {param_name} with True",
                priority="high",
                target_function=func_name,
            ))
            plan.intentions.append(TestIntention(
                category="normal_case",
                description=f"Test {param_name} with False",
                priority="high",
                target_function=func_name,
            ))
    
    def _prioritize_and_dedupe(self, intentions: List[TestIntention]) -> List[TestIntention]:
        """Sort by priority and remove duplicates."""
        priority_order = {'high': 0, 'medium': 1, 'low': 2}
        
        # Remove duplicates based on description
        seen = set()
        unique = []
        for intention in intentions:
            key = (intention.description, intention.target_function)
            if key not in seen:
                seen.add(key)
                unique.append(intention)
        
        # Sort by priority
        unique.sort(key=lambda x: priority_order.get(x.priority, 1))
        
        # Limit to reasonable number
        return unique[:15]


# For backward compatibility with existing imports
MockIntentionGenerator = StaticIntentionGenerator


if __name__ == "__main__":
    # Example usage
    sample_code = '''
class Calculator:
    """A simple calculator class."""
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b
    
    def divide(self, a: float, b: float) -> float:
        """Divide a by b.
        
        Example:
            >>> calc.divide(10, 2)
            5.0
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    
    def factorial(self, n: int) -> int:
        """Calculate factorial of n."""
        if n < 0:
            raise ValueError("n must be non-negative")
        if n == 0:
            return 1
        return n * self.factorial(n - 1)
'''
    
    generator = StaticIntentionGenerator()
    plan = generator.generate_intentions(sample_code, problem_description="A calculator with basic math operations")
    
    print("=== Test Intentions ===")
    print(plan.to_prompt_format())
    print("\n=== JSON Format ===")
    import json
    print(json.dumps(plan.to_dict(), indent=2))
