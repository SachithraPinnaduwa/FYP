"""
Code Analyzer Module (Part A - Static Analysis)

Uses Python's ast module to extract:
- Function signatures
- Docstrings
- Class definitions
- Usage examples (from docstrings)
- Parameter types and return types (from annotations)

No AI required - pure static analysis.
"""

import ast
import re
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class ParameterInfo:
    """Information about a function parameter."""
    name: str
    annotation: Optional[str] = None
    default: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "annotation": self.annotation,
            "default": self.default,
        }


@dataclass
class FunctionInfo:
    """Extracted information about a function."""
    name: str
    signature: str
    docstring: Optional[str] = None
    parameters: List[ParameterInfo] = field(default_factory=list)
    return_annotation: Optional[str] = None
    decorators: List[str] = field(default_factory=list)
    is_async: bool = False
    usage_examples: List[str] = field(default_factory=list)
    line_number: int = 0
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "signature": self.signature,
            "docstring": self.docstring,
            "parameters": [p.to_dict() for p in self.parameters],
            "return_annotation": self.return_annotation,
            "decorators": self.decorators,
            "is_async": self.is_async,
            "usage_examples": self.usage_examples,
            "line_number": self.line_number,
        }


@dataclass
class ClassInfo:
    """Extracted information about a class."""
    name: str
    docstring: Optional[str] = None
    methods: List[FunctionInfo] = field(default_factory=list)
    base_classes: List[str] = field(default_factory=list)
    decorators: List[str] = field(default_factory=list)
    class_variables: List[str] = field(default_factory=list)
    line_number: int = 0
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "docstring": self.docstring,
            "methods": [m.to_dict() for m in self.methods],
            "base_classes": self.base_classes,
            "decorators": self.decorators,
            "class_variables": self.class_variables,
            "line_number": self.line_number,
        }


@dataclass
class ModuleInfo:
    """Extracted information about a Python module."""
    module_docstring: Optional[str] = None
    imports: List[str] = field(default_factory=list)
    functions: List[FunctionInfo] = field(default_factory=list)
    classes: List[ClassInfo] = field(default_factory=list)
    global_variables: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "module_docstring": self.module_docstring,
            "imports": self.imports,
            "functions": [f.to_dict() for f in self.functions],
            "classes": [c.to_dict() for c in self.classes],
            "global_variables": self.global_variables,
        }


class CodeAnalyzer:
    """
    Static code analyzer using Python's ast module.
    
    Extracts structure information from Python source code without
    executing it or using any AI/ML models.
    """
    
    def __init__(self):
        self._source_lines: List[str] = []
    
    def analyze(self, source_code: str) -> ModuleInfo:
        """
        Analyze Python source code and extract structural information.
        
        Args:
            source_code: The Python source code to analyze
            
        Returns:
            ModuleInfo containing all extracted information
        """
        self._source_lines = source_code.split('\n')
        
        try:
            tree = ast.parse(source_code)
        except SyntaxError as e:
            raise ValueError(f"Failed to parse Python code: {e}")
        
        module_info = ModuleInfo()
        
        # Extract module docstring
        module_info.module_docstring = ast.get_docstring(tree)
        
        # Process top-level nodes
        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    module_info.imports.append(alias.name)
            
            elif isinstance(node, ast.ImportFrom):
                module_name = node.module or ""
                for alias in node.names:
                    module_info.imports.append(f"{module_name}.{alias.name}")
            
            elif isinstance(node, ast.FunctionDef):
                module_info.functions.append(self._extract_function(node))
            
            elif isinstance(node, ast.AsyncFunctionDef):
                module_info.functions.append(self._extract_function(node, is_async=True))
            
            elif isinstance(node, ast.ClassDef):
                module_info.classes.append(self._extract_class(node))
            
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        module_info.global_variables.append(target.id)
        
        return module_info
    
    def _extract_function(self, node: ast.FunctionDef, is_async: bool = False) -> FunctionInfo:
        """Extract information from a function definition."""
        func_info = FunctionInfo(
            name=node.name,
            signature=self._build_signature(node),
            docstring=ast.get_docstring(node),
            is_async=is_async,
            line_number=node.lineno,
        )
        
        # Extract parameters
        func_info.parameters = self._extract_parameters(node.args)
        
        # Extract return annotation
        if node.returns:
            func_info.return_annotation = self._annotation_to_str(node.returns)
        
        # Extract decorators
        for decorator in node.decorator_list:
            func_info.decorators.append(self._node_to_str(decorator))
        
        # Extract usage examples from docstring
        if func_info.docstring:
            func_info.usage_examples = self._extract_examples(func_info.docstring)
        
        return func_info
    
    def _extract_class(self, node: ast.ClassDef) -> ClassInfo:
        """Extract information from a class definition."""
        class_info = ClassInfo(
            name=node.name,
            docstring=ast.get_docstring(node),
            line_number=node.lineno,
        )
        
        # Extract base classes
        for base in node.bases:
            class_info.base_classes.append(self._node_to_str(base))
        
        # Extract decorators
        for decorator in node.decorator_list:
            class_info.decorators.append(self._node_to_str(decorator))
        
        # Extract methods and class variables
        for item in node.body:
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                is_async = isinstance(item, ast.AsyncFunctionDef)
                class_info.methods.append(self._extract_function(item, is_async))
            elif isinstance(item, ast.Assign):
                for target in item.targets:
                    if isinstance(target, ast.Name):
                        class_info.class_variables.append(target.id)
            elif isinstance(item, ast.AnnAssign):
                if isinstance(item.target, ast.Name):
                    class_info.class_variables.append(item.target.id)
        
        return class_info
    
    def _extract_parameters(self, args: ast.arguments) -> List[ParameterInfo]:
        """Extract parameter information from function arguments."""
        parameters = []
        
        # Calculate defaults offset
        num_args = len(args.args)
        num_defaults = len(args.defaults)
        defaults_offset = num_args - num_defaults
        
        for i, arg in enumerate(args.args):
            param = ParameterInfo(name=arg.arg)
            
            if arg.annotation:
                param.annotation = self._annotation_to_str(arg.annotation)
            
            # Check for default value
            default_idx = i - defaults_offset
            if default_idx >= 0 and default_idx < len(args.defaults):
                param.default = self._node_to_str(args.defaults[default_idx])
            
            parameters.append(param)
        
        # Handle *args
        if args.vararg:
            param = ParameterInfo(name=f"*{args.vararg.arg}")
            if args.vararg.annotation:
                param.annotation = self._annotation_to_str(args.vararg.annotation)
            parameters.append(param)
        
        # Handle keyword-only arguments
        for i, arg in enumerate(args.kwonlyargs):
            param = ParameterInfo(name=arg.arg)
            if arg.annotation:
                param.annotation = self._annotation_to_str(arg.annotation)
            if i < len(args.kw_defaults) and args.kw_defaults[i]:
                param.default = self._node_to_str(args.kw_defaults[i])
            parameters.append(param)
        
        # Handle **kwargs
        if args.kwarg:
            param = ParameterInfo(name=f"**{args.kwarg.arg}")
            if args.kwarg.annotation:
                param.annotation = self._annotation_to_str(args.kwarg.annotation)
            parameters.append(param)
        
        return parameters
    
    def _build_signature(self, node: ast.FunctionDef) -> str:
        """Build a function signature string."""
        try:
            # Get the source line for the function definition
            start_line = node.lineno - 1
            end_line = start_line
            
            # Find the complete signature (might span multiple lines)
            signature_lines = []
            paren_count = 0
            found_open = False
            
            for i in range(start_line, min(start_line + 10, len(self._source_lines))):
                line = self._source_lines[i]
                signature_lines.append(line)
                
                for char in line:
                    if char == '(':
                        found_open = True
                        paren_count += 1
                    elif char == ')':
                        paren_count -= 1
                
                if found_open and paren_count == 0:
                    break
            
            signature = '\n'.join(signature_lines)
            # Clean up the signature
            if ':' in signature:
                signature = signature[:signature.rindex(':')]
            return signature.strip()
            
        except Exception:
            # Fallback: construct from AST
            params = []
            for param in self._extract_parameters(node.args):
                param_str = param.name
                if param.annotation:
                    param_str += f": {param.annotation}"
                if param.default:
                    param_str += f" = {param.default}"
                params.append(param_str)
            
            sig = f"def {node.name}({', '.join(params)})"
            if node.returns:
                sig += f" -> {self._annotation_to_str(node.returns)}"
            return sig
    
    def _annotation_to_str(self, annotation: ast.expr) -> str:
        """Convert an annotation AST node to string."""
        return self._node_to_str(annotation)
    
    def _node_to_str(self, node: ast.expr) -> str:
        """Convert an AST node to its string representation."""
        try:
            return ast.unparse(node)
        except Exception:
            # Fallback for older Python versions
            if isinstance(node, ast.Name):
                return node.id
            elif isinstance(node, ast.Constant):
                return repr(node.value)
            elif isinstance(node, ast.Attribute):
                return f"{self._node_to_str(node.value)}.{node.attr}"
            elif isinstance(node, ast.Subscript):
                return f"{self._node_to_str(node.value)}[{self._node_to_str(node.slice)}]"
            elif isinstance(node, ast.Call):
                return f"{self._node_to_str(node.func)}(...)"
            return "<unknown>"
    
    def _extract_examples(self, docstring: str) -> List[str]:
        """Extract usage examples from a docstring."""
        examples = []
        
        # Look for doctest-style examples (>>> )
        doctest_pattern = r'>>>\s*(.+?)(?=\n(?:>>>|\s*$)|$)'
        doctests = re.findall(doctest_pattern, docstring, re.MULTILINE)
        examples.extend(doctests)
        
        # Look for "Example:" or "Examples:" sections
        example_section_pattern = r'(?:Examples?|Usage):\s*\n((?:\s+.+\n?)+)'
        sections = re.findall(example_section_pattern, docstring, re.IGNORECASE)
        for section in sections:
            # Extract code-like lines from the section
            lines = section.strip().split('\n')
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    examples.append(line)
        
        return examples
    
    def get_structure_summary(self, module_info: ModuleInfo) -> str:
        """
        Generate a human-readable summary of the code structure.
        
        Args:
            module_info: The analyzed module information
            
        Returns:
            A formatted string summary
        """
        lines = []
        
        if module_info.module_docstring:
            lines.append(f"Module Description: {module_info.module_docstring[:200]}...")
            lines.append("")
        
        if module_info.imports:
            lines.append(f"Dependencies: {', '.join(module_info.imports[:10])}")
            lines.append("")
        
        for func in module_info.functions:
            lines.append(f"Function: {func.signature}")
            if func.docstring:
                lines.append(f"  Purpose: {func.docstring.split(chr(10))[0]}")
            if func.parameters:
                params_str = ", ".join([
                    f"{p.name}" + (f": {p.annotation}" if p.annotation else "")
                    for p in func.parameters if not p.name.startswith('self')
                ])
                if params_str:
                    lines.append(f"  Parameters: {params_str}")
            if func.return_annotation:
                lines.append(f"  Returns: {func.return_annotation}")
            if func.usage_examples:
                lines.append(f"  Examples: {'; '.join(func.usage_examples[:3])}")
            lines.append("")
        
        for cls in module_info.classes:
            lines.append(f"Class: {cls.name}")
            if cls.base_classes:
                lines.append(f"  Inherits: {', '.join(cls.base_classes)}")
            if cls.docstring:
                lines.append(f"  Purpose: {cls.docstring.split(chr(10))[0]}")
            if cls.methods:
                method_names = [m.name for m in cls.methods if not m.name.startswith('_') or m.name == '__init__']
                lines.append(f"  Methods: {', '.join(method_names)}")
            lines.append("")
        
        return '\n'.join(lines)


# Convenience function
def analyze_code(source_code: str) -> Dict[str, Any]:
    """
    Analyze Python source code and return structured information.
    
    Args:
        source_code: The Python source code to analyze
        
    Returns:
        Dictionary containing module structure information
    """
    analyzer = CodeAnalyzer()
    module_info = analyzer.analyze(source_code)
    return module_info.to_dict()


if __name__ == "__main__":
    # Example usage
    sample_code = '''
def divide(a: float, b: float) -> float:
    """
    Divide two numbers.
    
    Args:
        a: The dividend
        b: The divisor
        
    Returns:
        The quotient of a divided by b
        
    Example:
        >>> divide(10, 2)
        5.0
        
    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
'''
    
    analyzer = CodeAnalyzer()
    info = analyzer.analyze(sample_code)
    print(analyzer.get_structure_summary(info))
