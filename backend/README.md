# Backend Flask API

This folder contains a Flask backend that exposes endpoints to generate unit tests using your LoRA-finetuned model with **Adaptive Prompting**.

## Adaptive Prompting Pipeline

The adaptive prompting system uses **static analysis only** (no external AI/LLM required for prompt generation):

1. **Code Structure Analysis** (CodeAnalyzer) - Extracts functions, classes, signatures, docstrings using Python AST
2. **Test Intention Generation** (StaticIntentionGenerator) - Analyzes code patterns to determine what to test:
   - Parameter types and edge cases
   - Control flow (branches, loops, early returns)
   - Error handling (exceptions raised, try/except blocks)
   - Data operations (division, indexing, string ops)
   - Recursion detection
   - Mock suggestions for external dependencies
3. **Prompt Construction** - Merges structure and intentions into optimized prompt
4. **Test Generation** - Fine-tuned model generates actual test code

## Endpoints

### Basic Endpoints
- `GET /health` — Health check
- `POST /generate-tests` — Generate tests (simple prompt)

### Adaptive Prompting Endpoints
- `POST /analyze-code` — Static code analysis only (no model needed)
- `POST /generate-intentions` — Generate test intentions using static analysis
- `POST /generate-prompt-only` — Generate optimized prompt without running model
- `POST /generate-tests-adaptive` — Full pipeline: analysis → intentions → prompt → tests

## API Usage

### POST /generate-tests
```json
{
  "code": "<Python code>",
  "description": "optional problem description",
  "max_new_tokens": 512
}
```

### POST /generate-tests-adaptive
```json
{
  "code": "<Python code>",
  "description": "optional problem description",
  "max_new_tokens": 512,
  "include_debug": false
}
```

Response includes:
- `tests` - Generated test code
- `structure_summary` - Code structure analysis
- `intentions` - Test intentions identified
- `prompt_used` - (if include_debug=true) The full prompt sent to model

### POST /analyze-code
```json
{
  "code": "<Python code>"
}
```

Returns code structure without running any model.

### POST /generate-intentions
```json
{
  "code": "<Python code>",
  "description": "optional problem description"
}
```

Returns test intentions using static analysis (no AI required).

## Environment Variables
- `MODEL_NAME` — path to the GGUF model (default: `../gguf_model/unsloth.q4_k_m.gguf`)
- `MAX_SEQ_LENGTH` — tokenizer/model max seq length (default: `2048`)
- `LOAD_IN_4BIT` — `True`/`False` to load adapters in 4-bit (default: `True`)
- `DEVICE` — `cuda` or `cpu` (default: `cuda`)

## Local Run
```bash
python backend/backend.py
```

## Install Requirements
```bash
pip install -r backend/requirements.txt
```

## Notes
- The model is lazily loaded on first request
- For production, run behind a WSGI server with proper GPU allocation
- Ensure `unsloth` is installed and your model is available locally or via HF
- **No API keys required** - all prompt generation uses static analysis
