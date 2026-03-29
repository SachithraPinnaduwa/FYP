# FYP Thesis Project: Adaptive Prompting for LLM-Based Python Unit Test Generation

This repository contains the full implementation used for a Final Year Project (FYP) thesis on **automatic unit test generation for Python code**, with an emphasis on **adaptive prompting** and **fine-tuned/open-source LLMs**.

The system is built as an end-to-end research artifact:
- Model fine-tuning and experimentation notebooks
- A Flask backend for test generation APIs
- A Streamlit frontend for interactive usage
- A VS Code extension for editor-integrated test generation
- Benchmarking pipelines for quantitative evaluation on public datasets

## Thesis Submission Metadata

| Field | Value |
|------|-------|
| Thesis Title | Adaptive Prompting for LLM-Based Python Unit Test Generation |
| Student Name | Sachithra Pinnaduwa|
| Student ID | 20222016|
| Degree Program | Computer Science |
| Supervisor(s) | Asini Silva|
| Academic Year | 2025/2026 |
| Submission Date | 2026-03-30 |

## Thesis-Oriented Objective

The central thesis idea implemented here is:

1. Analyze input code structure statically (AST-based)
2. Infer what should be tested (test intentions)
3. Construct a better prompt from structure + intentions
4. Generate tests using a fine-tuned or baseline model
5. Evaluate generated tests with objective metrics (coverage, mutation, dataset-level scores)

This allows direct comparison between:
- Simple prompting vs adaptive prompting
- Fine-tuned local model vs base/open models
- LLM-based generation vs automated baselines (for example, Pynguin)

## Repository Overview

- `backend/`: Flask API for test generation and adaptive prompting pipeline
- `frontend/`: Streamlit UI to interact with backend endpoints
- `fyp-extension/`: VS Code extension for generating tests directly from Python files
- `benchmark/`: Benchmark pipeline for comparing multiple model generators
- `benchmark2/`: Benchmark pipeline focused on backend API modes (simple vs adaptive prompting)
- `gguf_model/`: Local GGUF model artifact used by backend (default: `unsloth.q4_k_m.gguf`)
- `sample_code/`: Sample and negative-case files for functional checks
- `model_finetuning.ipynb`: Notebook for fine-tuning workflow
- `performance_test.ipynb`: Notebook for performance-related experiments
- `testing_base.ipynb`: Notebook for base/testing experiments
- `unsloth_compiled_cache/`: Cached/generated trainer artifacts from experimentation

## System Architecture

### 1. Adaptive Prompting Pipeline (Backend)

Implemented in `backend/` using static program analysis:

1. **Code analysis** (`CodeAnalyzer`) extracts functions, classes, signatures, imports, and structure summary.
2. **Intention generation** (`StaticIntentionGenerator` or optional LLM intention module) infers edge cases, error paths, boundaries, and coverage goals.
3. **Prompt orchestration** (`AdaptivePrompter`) builds a structured prompt.
4. **Test generation** uses a local GGUF model through `llama-cpp-python`.

### 2. User Interfaces

- **Streamlit frontend** (`frontend/frontend.py`) for manual code input and test generation.
- **VS Code extension** (`fyp-extension/`) to select Python files and generate tests in-editor.

### 3. Evaluation Layer

- `benchmark/`: compares multiple model families/generators.
- `benchmark2/`: compares backend modes (`/generate-tests` vs `/generate-tests-adaptive`).

## Backend API Endpoints

Default backend host: `http://localhost:5000`

- `GET /health`: backend health check
- `POST /generate-tests`: basic prompting test generation
- `POST /generate-tests-adaptive`: full adaptive prompting pipeline
- `POST /analyze-code`: static code structure analysis only
- `POST /generate-intentions`: intention plan generation only
- `POST /generate-prompt-only`: build final adaptive prompt without generation

## Prerequisites

- Linux/macOS/Windows with Python installed (recommended Python 3.10+)
- Git
- Optional but recommended: NVIDIA GPU for faster local generation
- Node.js + npm (only if using the VS Code extension in development)

## Environment Setup

You can use one environment for the whole repository, or separate environments per module.

### Option A: Single environment (quick start)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Option B: Minimal per-component installs

- Frontend only:
```bash
pip install -r frontend/requirements.txt
```

- Benchmark pipelines:
```bash
pip install -r benchmark/requirements.txt
pip install -r benchmark2/requirements.txt
```

## Backend Configuration

Create a `.env` file in `backend/` (or copy values from `backend/example.env`):

```env
MODEL_NAME=../gguf_model/unsloth.q4_k_m.gguf
MAX_SEQ_LENGTH=16384
DEVICE=cuda
N_GPU_LAYERS=-1
PORT=5000
```

Notes:
- If GPU memory is limited, lower `N_GPU_LAYERS`.
- On CPU-only systems, set `DEVICE=cpu`.

## Running the System

### 1. Start backend

```bash
python backend/backend.py
```

### 2. Start frontend

```bash
streamlit run frontend/frontend.py
```

The frontend expects backend at `http://localhost:5000` by default.

## VS Code Extension (Optional)

Path: `fyp-extension/`

### Development run

```bash
cd fyp-extension
npm install
```

Then open the extension project in VS Code and run Extension Development Host (F5).

### Command provided

- `FYP: Select Python Files and Generate Tests`

### Keybinding

- `Ctrl+Alt+T` (or `Cmd+Alt+T` on macOS)

## Benchmarking and Evaluation

## Benchmark 1: Multi-model comparison

```bash
python benchmark/run_benchmark.py --samples 100 --stage all
```

Interactive prompt lets you choose model/generator variants (base, fine-tuned GGUF, other baselines, Pynguin).

## Benchmark 2: Prompting strategy comparison (API)

```bash
python benchmark2/run_benchmark.py --samples 100 --stage all --backend_url http://127.0.0.1:5000
```

Interactive choice:
- Simple prompting (`/generate-tests`)
- Adaptive prompting (`/generate-tests-adaptive`)

### Typical metrics produced

- Coverage-based quality indicators
- Mutation-based effectiveness indicators
- Aggregate dataset-level summaries

Results are saved inside each benchmark folder under `results/`.

## Notebooks

- `model_finetuning.ipynb`: fine-tuning pipeline and experiments
- `performance_test.ipynb`: generation/performance measurements
- `testing_base.ipynb`: baseline checks and exploratory tests

Use these to reproduce the thesis experimentation workflow and ablation studies.

## Reproducible Run Script (Manual Sequence)

Use this exact sequence when preparing final thesis results:

1. Create/activate environment and install dependencies.
2. Start backend: `python backend/backend.py`
3. (Optional) Start frontend: `streamlit run frontend/frontend.py`
4. Run prompt-strategy benchmark: `python benchmark2/run_benchmark.py --samples 100 --stage all --backend_url http://127.0.0.1:5000`
5. Run multi-model benchmark: `python benchmark/run_benchmark.py --samples 100 --stage all`
6. Archive output folders from `benchmark/results/` and `benchmark2/results/`.
7. Record model configuration used (GGUF path, context length, GPU layer count).

## Reproducibility Checklist

1. Use a fixed random seed where applicable in experiments.
2. Keep model artifact/version constant when comparing prompting strategies.
3. Keep dataset split and sample count fixed for fair comparisons.
4. Log environment metadata (Python version, CUDA, package versions).
5. Archive generated tests and evaluator outputs per experiment run.

