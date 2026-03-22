import os
import re
import ast
import json
import streamlit as st
import requests
from typing import List, Dict, Any, Set, Optional

# Backend endpoints
BACKEND_BASE = os.environ.get("BACKEND_URL", "http://localhost:5000")
GENERATE_TESTS_URL = f"{BACKEND_BASE}/generate-tests"
GENERATE_ADAPTIVE_URL = f"{BACKEND_BASE}/generate-tests-adaptive"
ANALYZE_CODE_URL = f"{BACKEND_BASE}/analyze-code"
GENERATE_INTENTIONS_URL = f"{BACKEND_BASE}/generate-intentions"


# =============================================================================
# Helper Functions (defined BEFORE usage)
# =============================================================================

def extract_test_code(response_text: str) -> str:
    """
    Extract clean test code from model response.
    Handles multiple formats and validates the result.
    """
    if not response_text:
        return ""
    
    text = response_text.strip()
    
    # Try to find Python code blocks first (including unclosed ones)
    block_starts = ['```python', '```', '~~~python', '~~~']
    for start in block_starts:
        if start in text:
            # Get everything after the start marker
            after_start = text.split(start, 1)[1]
            end_marker = start[:3]
            # If there's an end marker, cut it off; else take the whole rest (cut off by max_tokens)
            if end_marker in after_start:
                return after_start.split(end_marker, 1)[0].strip()
            return after_start.strip()
            
    # Look for unittest code without code blocks
    lines = text.split('\n')
    code_lines = []
    in_code = False
    
    for line in lines:
        # Start capturing when we see import unittest or class Test or def test_
        if any(marker in line for marker in ['import unittest', 'import pytest', 'class Test']):
            in_code = True
        elif line.strip().startswith('def test_'):
            in_code = True
            
        if in_code:
            # Stop if we hit explanation text
            if line.strip().startswith('#') and len(line.strip()) > 100:
                continue
            if any(marker in line.lower() for marker in ['explanation:', 'note:', 'output:']):
                break
            code_lines.append(line)
    
    if code_lines:
        result = '\n'.join(code_lines).strip()
        if 'test' in result.lower():
            return result
    
    # Final fallback: return text if it looks like valid test code
    if 'import unittest' in text or 'class Test' in text or 'def test_' in text:
        return text
    
    return ""


def is_valid_test_code(code: str) -> bool:
    """
    Check if the extracted code is valid format and syntactically correct Python.
    """
    if not code:
        return False
    
    code_lower = code.lower()
    
    # Must have test indicators
    has_test_indicators = any([
        'import unittest' in code,
        'from unittest' in code,
        'TestCase' in code,
        'def test_' in code,
        'self.assert' in code_lower,
        'self.assertEqual' in code_lower,
        'self.assertTrue' in code_lower,
        'self.assertRaises' in code_lower,
        'pytest' in code_lower
    ])
    
    if not has_test_indicators:
        return False
    
    # Count test methods vs regular methods
    test_method_count = len(re.findall(r'def test_\w+', code))
    
    # Should have at least one test method
    if test_method_count < 1:
        return False
        
    # Strictly validate against Python syntax errors
    import ast
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        # If the code was abruptly cut off by token limit, the last line might be incomplete.
        # Try trimming the last line and re-parsing up to 3 times
        lines = code.split('\n')
        for _ in range(3):
            if not lines:
                break
            lines.pop()
            trimmed_code = '\n'.join(lines)
            try:
                ast.parse(trimmed_code)
                return True
            except SyntaxError:
                continue
                
        return False


def extract_imports(code: str) -> Set[str]:
    """Extract unique import statements from code."""
    imports = set()
    for line in code.split('\n'):
        line = line.strip()
        if line.startswith('import ') or line.startswith('from '):
            # Normalize whitespace
            normalized = ' '.join(line.split())
            imports.add(normalized)
    return imports


def extract_test_classes(code: str) -> List[str]:
    """Extract test class definitions from code."""
    classes = []
    lines = code.split('\n')
    current_class = []
    in_class = False
    class_indent = 0
    
    for line in lines:
        stripped = line.strip()
        
        # Skip imports and empty lines at top level
        if not in_class:
            if stripped.startswith('import ') or stripped.startswith('from '):
                continue
            if not stripped:
                continue
        
        # Check for class definition
        if stripped.startswith('class ') and ('TestCase' in stripped or 'Test' in stripped):
            if in_class and current_class:
                classes.append('\n'.join(current_class))
            current_class = [line]
            in_class = True
            class_indent = len(line) - len(line.lstrip())
            continue
        
        # If we're in a class, collect lines
        if in_class:
            # Check if we've exited the class (new top-level definition)
            current_indent = len(line) - len(line.lstrip()) if line.strip() else class_indent + 1
            
            if stripped and current_indent <= class_indent and not stripped.startswith('#'):
                if stripped.startswith('class ') or stripped.startswith('def ') or stripped.startswith('if __name__'):
                    # Save current class and check if new one is a test class
                    if current_class:
                        classes.append('\n'.join(current_class))
                    if stripped.startswith('class ') and ('TestCase' in stripped or 'Test' in stripped):
                        current_class = [line]
                    else:
                        current_class = []
                        in_class = False
                    continue
            
            current_class.append(line)
    
    # Don't forget the last class
    if in_class and current_class:
        classes.append('\n'.join(current_class))
    
    return classes


def merge_test_files(results: List[tuple], failed_units: List[str] = None) -> str:
    """
    Merge multiple test generation results into a single test file.
    Handles deduplication of imports and proper formatting.
    
    Args:
        results: List of (name, test_code) tuples
        failed_units: List of unit names that failed to generate
    """
    all_imports = set()
    all_classes = []
    
    for name, code in results:
        if not code or not is_valid_test_code(code):
            continue
        
        # Extract test code if wrapped in response
        clean_code = extract_test_code(code) if not is_valid_test_code(code) else code
        if not clean_code or not is_valid_test_code(clean_code):
            continue
        
        # Collect imports (deduplicated)
        imports = extract_imports(clean_code)
        all_imports.update(imports)
        
        # Collect test classes
        classes = extract_test_classes(clean_code)
        all_classes.extend(classes)
    
    if not all_classes:
        return "# No valid test code was generated. Please try again or check individual results."
    
    # Sort imports for consistency
    sorted_imports = sorted(all_imports, key=lambda x: (
        0 if 'import unittest' in x else
        1 if 'from unittest' in x else
        2 if x.startswith('import ') else 3
    ))
    
    # Build merged file
    lines = []
    
    # Add comment about failed units if any
    if failed_units:
        lines.append(f"# NOTE: Tests could not be generated for: {', '.join(failed_units)}")
        lines.append("# Please generate tests for these units manually.")
        lines.append("")
    
    # Add imports (deduplicated)
    for imp in sorted_imports:
        lines.append(imp)
    
    lines.append('')
    lines.append('')
    
    # Add all test classes
    for cls in all_classes:
        lines.append(cls.rstrip())
        lines.append('')
        lines.append('')
    
    # Add main block
    lines.append("if __name__ == '__main__':")
    lines.append("    unittest.main()")
    lines.append('')
    
    return '\n'.join(lines)


def split_code_into_chunks(source_code: str) -> List[tuple]:
    """
    Split Python source code into individual functions and classes.
    Each chunk can be processed separately to fit within context window.
    
    Returns:
        List of tuples: (name, code_chunk, type)
    """
    chunks = []
    
    try:
        tree = ast.parse(source_code)
    except SyntaxError:
        # If parsing fails, return the whole code as one chunk
        return [("full_code", source_code, "module")]
    
    lines = source_code.split('\n')
    
    # Get imports (to include with each chunk for context)
    imports = []
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            start = node.lineno - 1
            end = node.end_lineno if hasattr(node, 'end_lineno') else node.lineno
            imports.extend(lines[start:end])
    
    imports_str = '\n'.join(imports) + '\n\n' if imports else ''
    
    # Extract each function and class
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            start = node.lineno - 1
            end = node.end_lineno if hasattr(node, 'end_lineno') else start + 1
            
            # Include decorators
            if node.decorator_list:
                start = node.decorator_list[0].lineno - 1
            
            func_code = '\n'.join(lines[start:end])
            chunks.append((node.name, imports_str + func_code, "function"))
        
        elif isinstance(node, ast.ClassDef):
            start = node.lineno - 1
            end = node.end_lineno if hasattr(node, 'end_lineno') else start + 1
            
            # Include decorators
            if node.decorator_list:
                start = node.decorator_list[0].lineno - 1
            
            class_code = '\n'.join(lines[start:end])
            chunks.append((node.name, imports_str + class_code, "class"))
    
    # If no functions/classes found, return the whole code
    if not chunks:
        return [("full_code", source_code, "module")]
    
    return chunks


def generate_tests_for_unit(code: str, description: str, use_adaptive: bool, 
                            max_tokens: int, include_debug: bool,
                            max_retries: int = 2, log_generation: bool = False,
                            intentions: Optional[Dict] = None) -> Dict[str, Any]:
    """
    Generate tests for a single code unit with retry logic.
    """
    last_error = None
    
    for attempt in range(max_retries + 1):
        try:
            if use_adaptive:
                url = GENERATE_ADAPTIVE_URL
                payload = {
                    "code": code,
                    "description": description,
                    "max_new_tokens": max_tokens,
                    "include_debug": include_debug,
                    "log_generation": log_generation
                }
                if intentions:
                    payload["intentions"] = intentions
            else:
                url = GENERATE_TESTS_URL
                payload = {
                    "code": code,
                    "description": description,
                    "max_new_tokens": max_tokens,
                    "log_generation": log_generation
                }
            
            resp = requests.post(url, json=payload, timeout=180)
            
            if resp.status_code == 200:
                result = resp.json()
                tests = result.get('tests', '')
                
                # Extract and validate the result
                extracted = extract_test_code(tests)
                if is_valid_test_code(extracted):
                    result['tests'] = extracted
                    result['valid'] = True
                    return result
                elif attempt < max_retries:
                    # Retry if extraction failed
                    last_error = "Generated output was not valid test code"
                    continue
                else:
                    # Return with warning
                    result['valid'] = False
                    result['warning'] = "Output may not be valid test code"
                    return result
            else:
                last_error = f"HTTP {resp.status_code}: {resp.text}"
                
        except requests.exceptions.Timeout:
            last_error = "Request timed out"
        except requests.exceptions.RequestException as e:
            last_error = str(e)
    
    return {"error": last_error or "Unknown error", "tests": "", "valid": False}


# =============================================================================
# Streamlit UI
# =============================================================================

st.set_page_config(page_title="Unit Test Generator", layout="wide")

st.title("🧪 AI-Powered Unit Test Generator")
st.markdown("""
Generate comprehensive unit tests using **Adaptive Prompting**:
1. **Static Analysis** - Extracts code structure (functions, classes, docstrings)
2. **AI Test Planning** - Determines what to test (edge cases, error handling)
3. **Test Generation** - Fine-tuned model generates the actual test code
""")

st.divider()

# =============================================================================
# Input Section
# =============================================================================
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Input Code")
    
    # Input method selector
    input_method = st.radio(
        "Choose input method:",
        ["Paste code", "Upload .py file"],
        horizontal=True
    )
    
    code = ""
    
    if input_method == "Upload .py file":
        uploaded_file = st.file_uploader(
            "Upload a Python file (Max 256KB)",
            type=["py"],
            help="Upload a .py file to generate tests for (up to 256KB)"
        )
        if uploaded_file is not None:
            if uploaded_file.size >  256 * 1024:
                st.error("File size exceeds the 256KB limit. Please upload a smaller file.")
            else:
                code = uploaded_file.read().decode("utf-8")
                
                if "code_expanded" not in st.session_state:
                    st.session_state.code_expanded = False
                
                if st.session_state.code_expanded:
                    if st.button("Collapse Code", key="collapse_file_btn"):
                        st.session_state.code_expanded = False
                        st.rerun()
                    st.code(code, language="python", line_numbers=True)
                else:
                    if st.button("Expand Code", key="expand_file_btn"):
                        st.session_state.code_expanded = True
                        st.rerun()
                    with st.container(height=300):
                        st.code(code, language="python", line_numbers=True)
    else:
        code = st.text_area(
            "Code to test",
            height=300,
            value='''def divide(a: float, b: float) -> float:
    """
    Divide two numbers.
    
    Args:
        a: The dividend
        b: The divisor
        
    Returns:
        The quotient of a divided by b
        
    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b''',
        )
    
    description = st.text_area(
        "Test requirements (Include line by line for each requirement)",
        height=80,
        placeholder="Enter test requirements line by line...",
        help="Examples of test requirements:\n- The test cases should include positive and negative tests\n- Mock the database calls\n- Verify API error responses\n- Ensure invalid arguments throw ValueError"
    )

with col2:
    st.subheader("⚙️ Settings")
    
    # Generation mode
    use_adaptive = st.checkbox(
        "Use Adaptive Prompting",
        value=True,
        help="Enable AI-powered test planning for better test coverage"
    )
    
    # Chunked processing for low context window models
    process_individually = st.checkbox(
        "Process functions/classes individually",
        value=True,
        help="Split code into individual functions/classes for models with low context window (recommended for 2048 token limit)"
    )
    
    # Retry on failure
    retry_failed = st.checkbox(
        "Retry failed generations",
        value=True,
        help="Automatically retry if test generation fails or returns invalid code"
    )

    log_generation = st.checkbox(
        "Enable logging",
        value=False,
        help="Enable optional logging to log the generation time (info like user code is omitted)"
    )
    
    max_new_tokens = st.slider(
        "Max tokens per chunk",
        min_value=256,
        max_value=2048,
        value=512,
        step=64,
        help="Maximum tokens to generate per function/class"
    )
    
    show_analysis = st.checkbox(
        "Show code analysis",
        value=True,
        help="Display the extracted structure and test intentions"
    )
    
    include_debug = st.checkbox(
        "Include prompt (debug)",
        value=False,
        help="Include the full prompt sent to the model"
    )
    
    # Show detected chunks if processing individually
    if process_individually and code.strip():
        chunks = split_code_into_chunks(code)
        if len(chunks) > 1:
            st.info(f"📦 Detected {len(chunks)} testable units: " + 
                   ", ".join([f"`{name}` ({typ})" for name, _, typ in chunks]))

st.divider()

# =============================================================================
# Analysis Preview (when adaptive is enabled)
# =============================================================================
if use_adaptive and show_analysis and code.strip():
    with st.expander("📊 Code Analysis Preview", expanded=False):
        col_struct, col_intent = st.columns(2)
        
        with col_struct:
            st.markdown("**Code Structure** (via `ast`)")
            try:
                resp = requests.post(ANALYZE_CODE_URL, json={"code": code}, timeout=30)
                if resp.status_code == 200:
                    data = resp.json()
                    st.text(data.get("summary", "No structure found"))
                else:
                    st.warning(f"Analysis failed: {resp.json().get('error', 'Unknown error')}")
            except Exception as e:
                st.warning(f"Could not analyze: {e}")
        
        with col_intent:
            st.markdown("**Test Intentions** (via LLM)")
            try:
                resp = requests.post(
                    GENERATE_INTENTIONS_URL,
                    json={"code": code, "description": description},
                    timeout=60
                )
                if resp.status_code == 200:
                    data = resp.json()
                    st.text(data.get("prompt_format", "No intentions generated"))
                    # Cache the generated intentions so we can pass them to the test generator later
                    if "intentions" in data:
                        st.session_state["cached_intentions"] = data["intentions"]
                else:
                    st.warning(f"Intention generation failed: {resp.json().get('error', 'Unknown error')}")
            except Exception as e:
                st.warning(f"Could not generate intentions: {e}")

# =============================================================================
# Generate Button
# =============================================================================
if st.button("🚀 Generate Tests", type="primary", use_container_width=True):
    if not code.strip():
        st.error("Please provide code to test.")
    else:
        # Determine if we need to process in chunks
        if process_individually:
            chunks = split_code_into_chunks(code)
        else:
            chunks = [("full_code", code, "module")]
        
        all_test_results = []  # List of (name, test_code) tuples
        all_response_data = []  # Full response data for each unit
        failed_units = []
        
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        total_chunks = len(chunks)
        max_retries = 2 if retry_failed else 0
        
        for idx, (name, chunk_code, chunk_type) in enumerate(chunks):
            status_text.text(f"🔄 Processing {chunk_type} `{name}` ({idx + 1}/{total_chunks})...")
            progress_bar.progress((idx) / total_chunks)
            
            # Build description with context
            chunk_desc = f"{description}\n\nThis is a {chunk_type} named '{name}'." if description else f"This is a {chunk_type} named '{name}'."
            
            # Only pass cached intentions if we aren't splitting into multiple chunks
            passed_intentions = st.session_state.get("cached_intentions") if len(chunks) == 1 else None
            
            # Generate tests with retry logic
            result = generate_tests_for_unit(
                code=chunk_code,
                description=chunk_desc,
                use_adaptive=use_adaptive,
                max_tokens=max_new_tokens,
                include_debug=include_debug,
                max_retries=max_retries,
                log_generation=log_generation,
                intentions=passed_intentions
            )
            
            if result.get('error'):
                st.warning(f"⚠️ Failed to generate tests for `{name}`: {result.get('error')}")
                failed_units.append(name)
            elif not result.get('valid', False):
                st.warning(f"⚠️ Output for `{name}` may not be valid test code")
                failed_units.append(name)
            else:
                test_code = result.get('tests', '')
                all_test_results.append((name, test_code))
                result['unit_name'] = name
                result['unit_type'] = chunk_type
                all_response_data.append(result)
        
        progress_bar.progress(1.0)
        status_text.empty()
        
        # Display results
        successful = len(all_test_results)
        
        if successful > 0:
            if failed_units:
                st.warning(f"✅ Generated tests for {successful}/{total_chunks} units. Failed: {', '.join(failed_units)}")
            else:
                st.success(f"✅ Generated tests for all {total_chunks} units!")
            
            # Show analysis info if adaptive
            if use_adaptive and show_analysis and all_response_data:
                with st.expander("📋 Generation Details", expanded=False):
                    for item in all_response_data:
                        st.markdown(f"**{item.get('unit_type', 'Unit').title()}: `{item.get('unit_name', 'unknown')}`**")
                        intentions = item.get("intentions", {})
                        for intent in intentions.get("intentions", [])[:5]:
                            cat = intent.get("category", "").upper()
                            desc = intent.get("description", "")
                            st.markdown(f"  - [{cat}] {desc}")
                        
                        prompt_used = item.get("prompt_used", None)
                        if prompt_used:
                            st.markdown("**Prompt Sent to Model:**")
                            st.code(prompt_used, language="markdown")
                            
                        st.markdown("---")
            
            # Show results in tabs if multiple units
            if len(all_test_results) > 1:
                st.subheader("📄 Generated Unit Tests")
                
                tab_names = [name for name, _ in all_test_results]
                tab_names.append("📦 Merged")
                tabs = st.tabs(tab_names)
                
                for i, (name, test_code) in enumerate(all_test_results):
                    with tabs[i]:
                        st.code(test_code, language="python", line_numbers=True)
                        st.download_button(
                            f"⬇️ Download test_{name}.py",
                            test_code,
                            file_name=f"test_{name}.py",
                            mime="text/x-python",
                            key=f"dl_{name}_{i}"
                        )
                
                # Merged tab
                with tabs[-1]:
                    merged_code = merge_test_files(all_test_results, failed_units if failed_units else None)
                    st.code(merged_code, language="python", line_numbers=True)
                    
                    col_dl1, col_dl2 = st.columns(2)
                    with col_dl1:
                        st.download_button(
                            "⬇️ Download all_tests.py",
                            merged_code,
                            file_name="all_tests.py",
                            mime="text/x-python",
                            key="dl_merged"
                        )
                    with col_dl2:
                        st.download_button(
                            "⬇️ Download results.json",
                            json.dumps(all_response_data, indent=2),
                            file_name="test_results.json",
                            mime="application/json",
                            key="dl_json"
                        )
            else:
                # Single chunk - show directly
                name, test_code = all_test_results[0]
                st.subheader("📄 Generated Unit Tests")
                st.code(test_code, language="python", line_numbers=True)
                
                col_dl1, col_dl2 = st.columns(2)
                with col_dl1:
                    st.download_button(
                        "⬇️ Download tests (.py)",
                        test_code,
                        file_name="generated_tests.py",
                        mime="text/x-python",
                        use_container_width=True
                    )
                with col_dl2:
                    if all_response_data:
                        st.download_button(
                            "⬇️ Download full response (.json)",
                            json.dumps(all_response_data[0], indent=2),
                            file_name="test_generation_result.json",
                            mime="application/json",
                            use_container_width=True
                        )
        else:
            st.error("❌ Failed to generate tests for any code units.")


# =============================================================================
# Footer
# =============================================================================
st.divider()
st.markdown("""
<div style="text-align: center; color: gray; font-size: 0.8em;">
    <p>Powered by Fine-Tuned LLM + Adaptive Prompting</p>
    <p>Structure Analysis: Python AST | Test Planning: Gemini/Ollama | Test Generation: GGUF Model</p>
</div>
""", unsafe_allow_html=True)
