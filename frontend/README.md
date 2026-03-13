# Frontend — Streamlit UI

This frontend is a minimal Streamlit app that calls the backend API to generate Python unit tests from a provided code snippet and optional description.

Run:

1. Install dependencies (prefer a virtualenv):
```bash
pip install -r frontend/requirements.txt
```

2. Ensure the backend is running (default: `http://localhost:5000`). If different, set `BACKEND_URL`:
```bash
export BACKEND_URL="http://<backend-host>:<port>/generate-tests"
```

3. Start the frontend:
```bash
streamlit run frontend/frontend.py
```

The UI lets you paste code and a problem description, then calls `/generate-tests` and displays (and lets you download) the generated tests.
