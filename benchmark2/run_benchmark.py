import sys
import os
import json
from pathlib import Path
from tqdm import tqdm
import argparse
from datasets import load_dataset

# Setup local paths for benchmark2 imports
current_dir = Path(__file__).resolve().parent
if str(current_dir) not in sys.path:
    sys.path.append(str(current_dir))

from evaluation.dataset_eval import DatasetBenchmarkEvaluator

def main():
    parser = argparse.ArgumentParser(description="Run Benchmark on KAKA22/CodeRM-UnitTest (Test Split)")
    parser.add_argument("--samples", type=int, default=100, help="Number of samples to evaluate (default: 100)")
    parser.add_argument("--stage", choices=["setup", "generate", "evaluate", "all"], default="all", help="Stage to run")
    args = parser.parse_args()

    print("\nSelect the model you want to benchmark:")
    print("1) Base Model (Qwen2.5-Coder-7B-Instruct-bnb-4bit via Unsloth)")
    print("2) Finetuned Model (GGUF localized)")
    print("3) Qwen3.5-4B Base Model (unsloth/Qwen3.5-4B via Unsloth)")
    
    choice = input("\nEnter choice (1, 2, or 3): ").strip()
    
    if choice == "1":
        model_name = "base_model"
        from models.base_model import BaseModelGenerator
        generator_class_name = "BaseModelGenerator"
    elif choice == "2":
        model_name = "finetuned_model"
        from models.gguf_model import GGUFModelGenerator
        generator_class_name = "GGUFModelGenerator"
    elif choice == "3":
        model_name = "qwen3.5_base"
        from models.qwen35_base_model import Qwen35BaseModelGenerator
        generator_class_name = "Qwen35BaseModelGenerator"
    else:
        print("Invalid choice, defaulting to Base Model.")
        model_name = "base_model"
        from models.base_model import BaseModelGenerator
        generator_class_name = "BaseModelGenerator"

    # Directories mapping inside benchmark2
    base_dir = current_dir
    subjects_dir = base_dir / "subjects" / "dataset"
    generated_dir = base_dir / "generated_tests" / model_name
    results_dir = base_dir / "results"

    if args.stage in ["setup", "generate", "all"]:
        # Directly load the dataset and subset here
        print(f"\n--- Loading {args.samples} samples from KAKA22/CodeRM-UnitTest (Test Split) ---")
        dataset = load_dataset("KAKA22/CodeRM-UnitTest", split="test")
        dataset = dataset.shuffle(seed=42).select(range(args.samples))
        
        # Make directories
        subjects_dir.mkdir(parents=True, exist_ok=True)
        generated_dir.mkdir(parents=True, exist_ok=True)
        
        if args.stage in ["generate", "all"]:
            print(f"\n--- [1] Generating Tests using {generator_class_name} ---")
            
            if model_name == "base_model":
                generator = BaseModelGenerator()
            elif model_name == "finetuned_model":
                generator = GGUFModelGenerator()
            elif model_name == "qwen3.5_base":
                generator = Qwen35BaseModelGenerator()
            
            for i, sample in enumerate(tqdm(dataset, desc="Generating Tests")):
                # Ensure a stable ID for both subject and test
                subject_id = f"subject_{i}"
                
                # 1. We MUST write out the subject.py because evaluation tools (coverage/mutation) 
                # execute at the file level and need an actual file to import.
                subject_file = subjects_dir / f"{subject_id}.py"
                with open(subject_file, "w", encoding="utf-8") as f:
                    f.write(sample["code_ground_truth"])
                
                # 2. Generate and write the test
                test_file_path = generated_dir / f"test_{subject_id}.py"
                if test_file_path.exists():
                    continue # Skip if already generated
                
                test_code = generator.generate_tests(
                    code=sample["code_ground_truth"], 
                    problem_description=sample["question"]
                )
                
                with open(test_file_path, "w", encoding="utf-8") as f:
                    f.write(test_code)
                    
            # Save a summary file
            summary = {
                "model": model_name,
                "samples": len(dataset),
                "output_dir": str(generated_dir)
            }
            with open(generated_dir / "generation_summary.json", "w") as f:
                json.dump(summary, f, indent=4)
            print(f"Generated tests saved to {generated_dir}")

    if args.stage in ["evaluate", "all"]:
        print("\n--- [3] Evaluating Generated Tests ---")
        evaluator = DatasetBenchmarkEvaluator(
            subjects_dir=str(subjects_dir),
            generated_tests_dir=str(base_dir / "generated_tests"), # Evaluate all models in generated_tests folder
            results_dir=str(results_dir)
        )
        
        results = evaluator.evaluate_all(
            run_coverage=True,
            run_mutation=True,
            max_mutants=30
        )
        
        summary = evaluator.summarize_results(results)
        print("\n--- Evaluation Summary ---")
        print(json.dumps(summary, indent=4))
        print(f"Results saved to {results_dir}")

if __name__ == "__main__":
    main()
