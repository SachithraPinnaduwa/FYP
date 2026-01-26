# Backend Flask API

This folder contains a minimal Flask backend that exposes an endpoint to generate unit tests using your LoRA-finetuned model.

Endpoints:
- `GET /health` — simple health check
- `POST /generate-tests` — generate tests from provided JSON body

POST /generate-tests JSON body:
```
{
  "code": "<your Python code as a string>",
  "description": "<optional problem description>",
  "max_new_tokens": 512
}
```

Environment variables:
- `MODEL_NAME` — model folder or hub name (default: `lora_model`)
- `MAX_SEQ_LENGTH` — tokenizer/model max seq length (default: `2048`)
- `LOAD_IN_4BIT` — `True`/`False` to load adapters in 4-bit (default: `True`)
- `DEVICE` — `cuda` or `cpu` (default: `cuda`)

Local run (example):
```bash
python backend/app.py
```

Install requirements (recommended in a venv):
```bash
pip install -r backend/requirements.txt
```

Notes:
- This code lazily loads the model on first request. For production, run behind a WSGI server and ensure proper GPU allocation.
- Ensure `unsloth` is installed and your `lora_model` (or the model specified by `MODEL_NAME`) is available locally or via HF.
