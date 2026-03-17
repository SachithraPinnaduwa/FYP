"""
Benchmark Runner - Interactive test generation benchmark suite.
Prompts the user to select a model and runs test generation + evaluation.

Supported models:
  1. Ollama        – Local dolphin-llama3 via Ollama
  2. Finetuned     – LoRA finetuned model (GPU required)
  3. Gemini Flash  – Google Gemini API
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Resolve paths & load environment
# ---------------------------------------------------------------------------
_BENCHMARK_DIR = Path(__file__).parent
_PROJECT_ROOT = _BENCHMARK_DIR.parent

# .env can live in the benchmark dir or the project root
load_dotenv(_BENCHMARK_DIR / ".env")
load_dotenv(_PROJECT_ROOT / ".env")

# Paths & config from environment (with sensible defaults)
SUBJECTS_DIR = os.environ.get("SUBJECTS_DIR", str(_BENCHMARK_DIR / "subjects"))
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", str(_BENCHMARK_DIR / "generated_tests"))
RESULTS_DIR = os.environ.get("RESULTS_DIR", str(_BENCHMARK_DIR / "results"))
LORA_MODEL_PATH = os.environ.get("LORA_MODEL_PATH", str(_PROJECT_ROOT / "lora_model"))
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL_NAME = os.environ.get("OLLAMA_MODEL_NAME", "dolphin-llama3")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL_NAME = os.environ.get("GEMINI_MODEL_NAME", "gemini-2.0-flash")

MODEL_DIR_MAP = {
    "ollama": "ollama",
    "finetuned": "finetuned",
    "gemini": "gemini",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def get_subject_files(subjects_dir: str) -> List[Path]:
    """Return all Python subject files (excluding helpers)."""
    sd = Path(subjects_dir)
    return sorted(
        f for f in sd.glob("*.py")
        if f.name not in ("__init__.py", "dataset_loader.py")
    )


def extract_docstring(filepath: Path) -> str:
    """Extract module-level docstring from a Python file."""
    try:
        with open(filepath, "r") as fh:
            content = fh.read()
        for delim in ('"""', "'''"):
            if content.startswith(delim):
                return content.split(delim)[1].strip()
    except Exception:
        pass
    return ""


def prompt_model_selection() -> str:
    """Interactive prompt – returns one of 'ollama', 'finetuned', 'gemini'."""
    print()
    print("=" * 60)
    print("  SELECT A MODEL FOR TEST GENERATION")
    print("=" * 60)
    print()
    print("  1. Ollama        – Local dolphin-llama3 via Ollama")
    print("  2. Finetuned     – LoRA finetuned model (GPU required)")
    print("  3. Gemini Flash  – Google Gemini API")
    print()
    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == "1":
            return "ollama"
        if choice == "2":
            return "finetuned"
        if choice == "3":
            return "gemini"
        print("Invalid choice. Please enter 1, 2, or 3.")


def build_generator(model_key: str):
    """Instantiate the test-generator for the chosen model."""
    if model_key == "ollama":
        from models.ollama_model import OllamaTestGenerator
        gen = OllamaTestGenerator(model=OLLAMA_MODEL_NAME, base_url=OLLAMA_BASE_URL)
        if not gen._check_connection():
            print(f"\n[ERROR] Cannot connect to Ollama at {OLLAMA_BASE_URL}")
            print("Make sure Ollama is running:  ollama serve")
            sys.exit(1)
        print(f"  Connected to Ollama ({OLLAMA_MODEL_NAME})")
        return gen

    if model_key == "finetuned":
        from models.my_model import YourModelTestGenerator
        gen = YourModelTestGenerator(model_path=LORA_MODEL_PATH)
        print(f"  LoRA model path: {LORA_MODEL_PATH}")
        print("  (model will be loaded on first generation)")
        return gen

    if model_key == "gemini":
        if not GEMINI_API_KEY:
            print("\n[ERROR] GEMINI_API_KEY is not set. Add it to your .env file.")
            sys.exit(1)
        from models.gemini import GeminiTestGenerator
        gen = GeminiTestGenerator(model=GEMINI_MODEL_NAME, api_key=GEMINI_API_KEY)
        print(f"  Gemini model: {GEMINI_MODEL_NAME}")
        return gen

    print(f"[ERROR] Unknown model key: {model_key}")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Pipeline stages
# ---------------------------------------------------------------------------
def stage_generate(generator, model_key: str, subject_files: List[Path], output_base: Path) -> Dict:
    """Generate tests for every subject. Returns a results dict."""
    model_dir = output_base / MODEL_DIR_MAP[model_key]
    model_dir.mkdir(parents=True, exist_ok=True)

    results: Dict = {
        "model": model_key,
        "timestamp": datetime.now().isoformat(),
        "total": len(subject_files),
        "success": 0,
        "failed": 0,
        "subjects": [],
    }

    for idx, subject_file in enumerate(subject_files, 1):
        subject_name = subject_file.stem
        output_file = model_dir / f"test_{subject_name}.py"
        print(f"\n  [{idx}/{len(subject_files)}] {subject_name} ... ", end="", flush=True)

        try:
            with open(subject_file, "r") as fh:
                source_code = fh.read()
            description = extract_docstring(subject_file)

            start = time.time()
            test_code = generator.generate_tests(source_code, problem_description=description)
            elapsed = time.time() - start

            with open(output_file, "w") as fh:
                fh.write(test_code)

            print(f"OK ({elapsed:.1f}s)")
            results["success"] += 1
            results["subjects"].append({
                "subject": subject_name,
                "status": "success",
                "output": str(output_file),
                "time": round(elapsed, 2),
            })
        except Exception as exc:
            print(f"FAILED ({exc})")
            results["failed"] += 1
            results["subjects"].append({
                "subject": subject_name,
                "status": "failed",
                "error": str(exc),
            })

    with open(model_dir / "generation_results.json", "w") as fh:
        json.dump(results, fh, indent=2)

    return results


def stage_evaluate(model_key: str, output_base: Path, results_base: Path):
    """Run test-execution, coverage, and mutation evaluation."""

    # Test execution
    print("\n--- Test Execution ---")
    try:
        from evaluation.run_tests import TestRunner
        runner = TestRunner(
            subjects_dir=SUBJECTS_DIR,
            generated_tests_dir=str(output_base),
            results_dir=str(results_base),
        )
        test_results = runner.run_all_tests()
        summary = runner.summarize_results(test_results)
        for model, stats in summary.items():
            print(f"  {model}: {stats['runnable']}/{stats['total_subjects']} runnable")
    except Exception as exc:
        print(f"  Test execution skipped/failed: {exc}")

    # Coverage
    print("\n--- Coverage Evaluation ---")
    try:
        from evaluation.coverage_eval import CoverageEvaluator
        evaluator = CoverageEvaluator(
            subjects_dir=SUBJECTS_DIR,
            generated_tests_dir=str(output_base),
            results_dir=str(results_base),
        )
        cov_results = evaluator.evaluate_all()
        summary = evaluator.summarize_results(cov_results)
        for model, stats in summary.items():
            print(f"  {model}: {stats.get('avg_statement_coverage', 0):.1%} stmt coverage")
    except Exception as exc:
        print(f"  Coverage evaluation skipped/failed: {exc}")

    # Mutation
    print("\n--- Mutation Testing ---")
    try:
        from evaluation.mutation_eval import MutationTester
        tester = MutationTester(
            subjects_dir=SUBJECTS_DIR,
            generated_tests_dir=str(output_base),
            results_dir=str(results_base),
        )
        mut_results = tester.evaluate_all()
        summary = tester.summarize_results(mut_results)
        for model, stats in summary.items():
            print(f"  {model}: {stats.get('avg_mutation_score', 0):.1%} mutation score")
    except Exception as exc:
        print(f"  Mutation testing skipped/failed: {exc}")

    # Aggregate
    print("\n--- Aggregating Results ---")
    try:
        from evaluation.aggregate_results import ResultAggregator
        aggregator = ResultAggregator(results_dir=str(results_base))
        aggregator.save_results()
        print(aggregator.generate_report())
    except Exception as exc:
        print(f"  Aggregation skipped/failed: {exc}")


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Run the test-generation benchmark suite (one model at a time)."
    )
    parser.add_argument(
        "--stage",
        choices=["generate", "evaluate", "all"],
        default="all",
        help="Which stage to run (default: all)",
    )
    parser.add_argument(
        "--model",
        choices=["ollama", "finetuned", "gemini"],
        default=None,
        help="Model to use. If omitted you will be prompted interactively.",
    )
    parser.add_argument("--subjects-dir", default=None, help="Override SUBJECTS_DIR")
    parser.add_argument("--output-dir", default=None, help="Override OUTPUT_DIR")
    parser.add_argument("--results-dir", default=None, help="Override RESULTS_DIR")
    args = parser.parse_args()

    # Resolve dirs (CLI overrides > env > defaults)
    subjects_dir = args.subjects_dir or SUBJECTS_DIR
    output_dir = args.output_dir or OUTPUT_DIR
    results_dir = args.results_dir or RESULTS_DIR

    # Interactive model selection if not given on CLI
    model_key = args.model or prompt_model_selection()

    subject_files = get_subject_files(subjects_dir)
    if not subject_files:
        print(f"[ERROR] No subject files found in {subjects_dir}")
        sys.exit(1)

    print()
    print("=" * 60)
    print("  TEST GENERATION BENCHMARK SUITE")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print(f"  Model       : {model_key}")
    print(f"  Subjects    : {len(subject_files)} files")
    print(f"  Subjects dir: {subjects_dir}")
    print(f"  Output dir  : {output_dir}")
    print(f"  Results dir : {results_dir}")
    print("=" * 60)

    stages = ["generate", "evaluate"] if args.stage == "all" else [args.stage]
    output_base = Path(output_dir)
    results_base = Path(results_dir)
    output_base.mkdir(parents=True, exist_ok=True)
    results_base.mkdir(parents=True, exist_ok=True)

    if "generate" in stages:
        print(f"\n{'='*60}")
        print("STAGE 1: TEST GENERATION")
        print(f"{'='*60}")
        generator = build_generator(model_key)
        gen_results = stage_generate(generator, model_key, subject_files, output_base)
        print(f"\n  Done: {gen_results['success']}/{gen_results['total']} succeeded")

    if "evaluate" in stages:
        print(f"\n{'='*60}")
        print("STAGE 2: EVALUATION")
        print(f"{'='*60}")
        stage_evaluate(model_key, output_base, results_base)

    print(f"\n{'='*60}")
    print("  BENCHMARK COMPLETE")
    print(f"{'='*60}")
    print(f"  Results saved in: {results_dir}")
    print()


if __name__ == "__main__":
    main()
