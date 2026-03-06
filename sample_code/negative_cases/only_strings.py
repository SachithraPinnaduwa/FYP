"""
negative_cases/only_strings.py
Expected error: "The input contains only plain text strings, not Python code..."

The entire file (after the module docstring handled by the module-level
check) consists of bare string literals — no functions, classes,
imports, or assignments — which parse successfully but represent no
testable code.
"""

"This is just a description of what the module should do."
"It should implement a calculator with add subtract multiply and divide."
"The calculator should handle edge cases like division by zero."
"All inputs should be validated before processing."
