import os
import re
import ast
import streamlit as st
import requests

# Backend endpoints
BACKEND_BASE = os.environ.get("BACKEND_URL", "http://localhost:5000")
GENERATE_TESTS_URL = f"{BACKEND_BASE}/generate-tests"
GENERATE_ADAPTIVE_URL = f"{BACKEND_BASE}/generate-tests-adaptive"
ANALYZE_CODE_URL = f"{BACKEND_BASE}/analyze-code"
GENERATE_INTENTIONS_URL = f"{BACKEND_BASE}/generate-intentions"


# =============================================================================
# Helper Functions (defined BEFORE usage)
# =============================================================================

def extract_test_code(raw_text: str) -> str:
    """
    Extract Python test code from the model's response.
    Handles markdown code blocks and raw text.
    """
    # Look for ```python ... ``` blocks
    python_blocks = re.findall(r'```python\n(.*?)```', raw_text, re.DOTALL)
    if python_blocks:
        # Return the last (most complete) code block
        return python_blocks[-1].strip()
    
    # Look for ``` ... ``` blocks
    code_blocks = re.findall(r'```\n(.*?)```', raw_text, re.DOTALL)
    if code_blocks:
        return code_blocks[-1].strip()
    
    # Look for code starting with import or class or def
    lines = raw_text.split('\n')
    code_start = -1
    for i, line in enumerate(lines):
        if line.strip().startswith(('import ', 'from ', 'class ', 'def ', 'unittest')):
            code_start = i
            break
    
    if code_start >= 0:
        # Find the end (look for explanation text)
        code_lines = []
        for line in lines[code_start:]:
            # Stop at explanation sections
            if line.strip().startswith('###') or line.strip().startswith('Explanation'):
                break
            code_lines.append(line)
        return '\n'.join(code_lines).strip()
    
    # Fallback: return as-is
    return raw_text


def split_code_into_chunks(source_code: str) -> list:
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


def merge_test_files(test_results: list) -> str:
    """
    Merge multiple generated test files into one cohesive test file.
    
    Args:
        test_results: List of (name, test_code) tuples
        
    Returns:
        Merged test code
    """
    imports = set()
    test_classes = []
    standalone_tests = []
    
    for name, code in test_results:
        if not code.strip():
            continue
            
        lines = code.split('\n')
        in_class = False
        current_class = []
        
        for line in lines:
            stripped = line.strip()
            
            # Collect imports
            if stripped.startswith(('import ', 'from ')):
                imports.add(line)
            # Skip if __name__ == "__main__" blocks
            elif 'if __name__' in stripped:
                break
            # Collect class definitions
            elif stripped.startswith('class ') and 'TestCase' in line:
                in_class = True
                current_class = [line]
            elif in_class:
                if line and not line[0].isspace() and not stripped.startswith('#'):
                    # End of class
                    test_classes.append('\n'.join(current_class))
                    in_class = False
                    current_class = []
                else:
                    current_class.append(line)
            elif stripped.startswith('def test_'):
                standalone_tests.append(line)
        
        # Don't forget the last class
        if current_class:
            test_classes.append('\n'.join(current_class))
    
    # Build merged file
    result_parts = []
    
    # Imports
    result_parts.append("import unittest")
    for imp in sorted(imports):
        if 'unittest' not in imp:
            result_parts.append(imp)
    result_parts.append("")
    
    # Test classes
    for tc in test_classes:
        result_parts.append(tc)
        result_parts.append("")
    
    # Main block
    result_parts.append("")
    result_parts.append("if __name__ == '__main__':")
    result_parts.append("    unittest.main()")
    
    return '\n'.join(result_parts)


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
            "Upload a Python file",
            type=["py"],
            help="Upload a .py file to generate tests for"
        )
        if uploaded_file is not None:
            code = uploaded_file.read().decode("utf-8")
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
        "Problem description (optional)",
        height=80,
        placeholder="Describe what the code does or any specific testing requirements..."
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
    
    max_new_tokens = st.slider(
        "Max tokens per chunk",
        min_value=256,
        max_value=1024,
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
            st.markdown("**Test Intentions** (via Gemini)")
            try:
                resp = requests.post(
                    GENERATE_INTENTIONS_URL,
                    json={"code": code, "description": description},
                    timeout=60
                )
                if resp.status_code == 200:
                    data = resp.json()
                    st.text(data.get("prompt_format", "No intentions generated"))
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
        
        all_test_results = []
        all_intentions = []
        all_summaries = []
        
        # Choose endpoint based on mode
        url = GENERATE_ADAPTIVE_URL if use_adaptive else GENERATE_TESTS_URL
        
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        total_chunks = len(chunks)
        successful = 0
        failed = 0
        
        for idx, (name, chunk_code, chunk_type) in enumerate(chunks):
            status_text.text(f"🔄 Processing {chunk_type} `{name}` ({idx + 1}/{total_chunks})...")
            progress_bar.progress((idx) / total_chunks)
            
            # Build payload
            if use_adaptive:
                payload = {
                    "code": chunk_code,
                    "description": f"{description}\n\nThis is a {chunk_type} named '{name}'." if description else f"This is a {chunk_type} named '{name}'.",
                    "max_new_tokens": int(max_new_tokens),
                    "include_debug": include_debug,
                }
            else:
                payload = {
                    "code": chunk_code,
                    "description": f"{description}\n\nThis is a {chunk_type} named '{name}'." if description else f"This is a {chunk_type} named '{name}'.",
                    "max_new_tokens": int(max_new_tokens),
                }
            
            try:
                resp = requests.post(url, json=payload, timeout=180)
                data = resp.json()
                
                if resp.status_code == 200:
                    # Extract test code
                    tests_raw = data.get("tests", "")
                    test_code = extract_test_code(tests_raw)
                    all_test_results.append((name, test_code))
                    
                    # Collect analysis info
                    if use_adaptive:
                        all_summaries.append(data.get("structure_summary", ""))
                        all_intentions.append({
                            "name": name,
                            "type": chunk_type,
                            "intentions": data.get("intentions", {})
                        })
                    
                    successful += 1
                else:
                    st.warning(f"⚠️ Failed to generate tests for `{name}`: {data.get('error', 'Unknown error')}")
                    failed += 1
                    
            except requests.exceptions.Timeout:
                st.warning(f"⚠️ Timeout while processing `{name}`")
                failed += 1
            except Exception as e:
                st.warning(f"⚠️ Error processing `{name}`: {e}")
                failed += 1
        
        progress_bar.progress(1.0)
        status_text.empty()
        
        # Display results
        if successful > 0:
            st.success(f"✅ Generated tests for {successful}/{total_chunks} units" + 
                      (f" ({failed} failed)" if failed > 0 else ""))
            
            # Show analysis info if adaptive
            if use_adaptive and show_analysis and all_intentions:
                with st.expander("📋 Generation Details", expanded=False):
                    for item in all_intentions:
                        st.markdown(f"**{item['type'].title()}: `{item['name']}`**")
                        intentions = item.get("intentions", {})
                        for intent in intentions.get("intentions", []):
                            cat = intent.get("category", "").upper()
                            desc = intent.get("description", "")
                            st.markdown(f"  - [{cat}] {desc}")
                        st.markdown("---")
            
            # Merge all test results
            if len(all_test_results) > 1:
                # Multiple chunks - show individually with tabs
                st.subheader("📄 Generated Unit Tests")
                
                tab_names = [f"{name}" for name, _ in all_test_results]
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
                    merged_code = merge_test_files(all_test_results)
                    st.code(merged_code, language="python", line_numbers=True)
                    st.download_button(
                        "⬇️ Download all_tests.py",
                        merged_code,
                        file_name="all_tests.py",
                        mime="text/x-python",
                        key="dl_merged"
                    )
            else:
                # Single chunk - show directly
                _, test_code = all_test_results[0]
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
                    if use_adaptive and all_intentions:
                        import json
                        st.download_button(
                            "⬇️ Download full response (.json)",
                            json.dumps({"intentions": all_intentions, "tests": test_code}, indent=2),
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
    <p>Structure Analysis: Python AST | Test Planning: Gemini | Test Generation: LoRA Model</p>
</div>
""", unsafe_allow_html=True)

