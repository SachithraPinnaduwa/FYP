import os
import streamlit as st
import requests

BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:5000/generate-tests")
st.set_page_config(page_title="Unit Test Generator", layout="centered")

st.title("Generate Unit Tests")
st.markdown("Enter a short problem description and paste the code you want tests for.")

description = st.text_area("Problem description", height=120, key="description")
code = st.text_area(
    "Code to test",
    height=300,
    key="code",
    value='''def find_max(numbers):
    max_val = 0
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val''',
)

max_new_tokens = st.number_input("Max tokens", min_value=64, max_value=2048, value=512, step=64)

if st.button("Generate tests"):
    if not code.strip():
        st.error("Please provide code to test.")
    else:
        payload = {"code": code, "description": description, "max_new_tokens": int(max_new_tokens)}
        with st.spinner("Generating unit tests..."):
            try:
                resp = requests.post(BACKEND_URL, json=payload, timeout=120)
                resp.raise_for_status()
                data = resp.json()
                tests = data.get("tests") or data.get("error") or ""
                if resp.status_code == 200:
                    st.subheader("Generated unit tests")
                    st.code(tests, language="python")
                    st.download_button("Download tests (.py)", tests, file_name="generated_tests.py", mime="text/x-python")
                else:
                    st.error(f"Backend error: {tests}")
            except Exception as e:
                st.error(f"Request failed: {e}")
