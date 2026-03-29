import sys
import os
import argparse
from pathlib import Path
from tqdm import tqdm
from datasets import load_dataset

# Setup local paths for benchmark3 imports
current_dir = Path(__file__).resolve().parent
if str(current_dir) not in sys.path:
    sys.path.append(str(current_dir))

from evaluation.dataset_eval import DatasetBenchmarkEvaluator

def main():
    parser = argparse.ArgumentParser(description="Run Benchmark to Compare Simple vs Adaptive Prompting via Backend API")
    parser.add_argument("--samples", type=int, default=100, help="Number of samples to evaluate (default: 100)")
    parser.add_argument("--stage", choices=["setup", "generate", "evaluate", "all"], default="all", help="Stage to run")
    parser.add_argument("--backend_url", type=str, default="http://127.0.0.1:5000", help="URL of the backend API")
    args = parser.parse_args()

    print("\nSelect the prompting method you want to benchmark:")
    print("1) Simple Prompting (Calls /generate-tests in backend)")
    print("2) Adaptive Prompting (Calls /generate-tests-adaptive in backend)")
    
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    if choice == "1":
        model_name = "api_simple_prompt"
        from models.api_model import APISimplePromptGenerator
        GeneratorClass = APISimplePromptGenerator
    elif choice == "2":
        model_name = "api_adaptive_prompt"
        from models.api_model import APIAdaptivePromptGenerator
        GeneratorClass = APIAdaptivePromptGenerator
    else:
        print("Invalid choice, defaulting to Simple Prompting.")
        model_name = "api_simple_prompt"
        from models.api_model import APISimplePromptGenerator
        GeneratorClass = APISimplePromptGenerator

    # Directories mapping inside benchmark3
    base_dir = current_dir
    subjects_dir = base_dir / "subjects" / "dataset"
    generated_dir = base_dir / "generated_tests" / model_name
    results_dir = base_dir / "results"

    if args.stage in ["setup", "generate", "all"]:
        print(f"\n--- Loading {args.samples} samples from KAKA22/CodeRM-UnitTest (Test Split) ---")
        dataset = load_dataset("KAKA22/CodeRM-UnitTest", split="test")
        dataset = dataset.shuffle(seed=42).select(range(args.samples))
        
        # Make directories
        subjects_dir.mkdir(parents=True, exist_ok=True)
        generated_dir.mkdir(parents=True, exist_ok=True)
        
        if args.stage in ["generate", "all"]:
            print(f"\n--- Generating Tests using {model_name} backend API ---")
            
            generator = GeneratorClass(backend_url=args.backend_url)
            
            for i, sample in enumerate(tqdm(dataset, desc="Generating Tests")):
                subject_id = f"subject_{i}"
                subject_file = subjects_dir / f"{subject_id}.py"
                
                # Write the subject file
                code = sample["code_ground_truth"]
                
                # Avoid permission issues or duplicate writes if it exists (but we'll overwrite safely)
                with open(subject_file, "w") as f:
                    f.write(code)
                
                # Prepare a placeholder or empty content test file
                gen_test_file = generated_dir / f"test_{subject_id}.py"
                if gen_test_file.exists():
                    print(f"Skipping {subject_id} as it already exists in {generated_dir}...")
                    continue
                
                problem_description = sample.get("question", "")
                
                # Generate via API
                generated_test_code = generator.generate_tests(code, problem_description)
                
                # Save generated code
                with open(gen_test_file, "w") as f:
                    # Provide default imports to help tests
                    if "import pytest" not in generated_test_code and "import unittest" not in generated_test_code:
                        f.write("import pytest\nimport unittest\n")
                    f.write(f"from {subject_id} import *\n\n")
                    f.write(generated_test_code)

    if args.stage in ["evaluate", "all"]:
        print(f"\n--- Running Evaluation for {model_name} ---")
        
        # Instantiate evaluator and run all metrics
        evaluator = DatasetBenchmarkEvaluator(
            subjects_dir=str(subjects_dir),
            generated_tests_dir=str(base_dir / "generated_tests"),
            results_dir=str(results_dir)
        )
        
        # Evaluate everything
        results = evaluator.evaluate_all(
            run_coverage=True,
            run_mutation=True,
            max_mutants=30
        )
        
        summary = evaluator.summarize_results(results)
        import json
        print("\n--- Evaluation Summary ---")
        print(json.dumps(summary, indent=4))
        
        print(f"\n✅ Benchmark completed! Results saved to {results_dir}")

if __name__ == "__main__":
    main()