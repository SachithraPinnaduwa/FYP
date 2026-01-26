"""
Dataset Benchmark Runner - Complete pipeline using the KAKA22/CodeRM-UnitTest dataset.
Uses code_ground_truth from the dataset as subjects for test generation.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional


def main():
    parser = argparse.ArgumentParser(
        description="Run benchmark using KAKA22/CodeRM-UnitTest dataset"
    )
    
    parser.add_argument(
        "--stage",
        choices=["setup", "generate", "evaluate", "compare", "all"],
        default="all",
        help="Which stage to run"
    )
    parser.add_argument(
        "--max-subjects",
        type=int,
        default=50,
        help="Maximum number of subjects to use from dataset"
    )
    parser.add_argument(
        "--start-idx",
        type=int,
        default=0,
        help="Starting index in the dataset"
    )
    parser.add_argument(
        "--models",
        nargs="+",
        choices=["your_model", "gpt", "pynguin", "all"],
        default=["all"],
        help="Which models to evaluate"
    )
    parser.add_argument(
        "--use-real-gpt",
        action="store_true",
        help="Use real OpenAI API instead of mock"
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip subjects that already have generated tests"
    )
    
    args = parser.parse_args()
    
    base_dir = Path(__file__).parent
    
    print(f"""
{'='*70}
  DATASET BENCHMARK SUITE
  Using KAKA22/CodeRM-UnitTest
  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'='*70}

Max Subjects: {args.max_subjects}
Starting Index: {args.start_idx}
""")
    
    stages_to_run = []
    if args.stage == "all":
        stages_to_run = ["setup", "generate", "evaluate"]
    elif args.stage == "compare":
        # Legacy: redirect to evaluate
        print("Note: 'compare' stage deprecated. Using standard evaluation metrics.")
        stages_to_run = ["evaluate"]
    else:
        stages_to_run = [args.stage]
    
    # Stage 1: Setup - Load dataset and create subject files
    if "setup" in stages_to_run:
        print(f"\n{'='*70}")
        print("STAGE 1: DATASET SETUP")
        print(f"{'='*70}\n")
        
        from subjects.dataset_loader import setup_dataset_benchmark
        
        subjects_dir, gt_dir, subjects = setup_dataset_benchmark(
            max_subjects=args.max_subjects,
            split="train",
            start_idx=args.start_idx
        )
        
        subjects_with_tests = [s for s in subjects if s.ground_truth_tests]
        print(f"\nSetup complete:")
        print(f"  Total subjects: {len(subjects)}")
        print(f"  Subjects with ground truth tests: {len(subjects_with_tests)}")
    
    # Stage 2: Generate tests using all models
    if "generate" in stages_to_run:
        print(f"\n{'='*70}")
        print("STAGE 2: TEST GENERATION")
        print(f"{'='*70}\n")
        
        from subjects.dataset_loader import DatasetSubjectLoader
        from models.run_all_models import TestGenerationPipeline
        
        # Load subjects
        loader = DatasetSubjectLoader(
            output_dir="subjects_dataset",
            max_subjects=args.max_subjects
        )
        loader.load_dataset()
        
        # Adjust for start_idx
        if args.start_idx > 0:
            end_idx = min(args.start_idx + args.max_subjects, len(loader.dataset))
            loader.dataset = loader.dataset.select(range(args.start_idx, end_idx))
        
        loader.extract_subjects()
        
        models = args.models if "all" not in args.models else ["your_model", "gpt", "pynguin"]
        models_config = {
            "your_model": {"enabled": "your_model" in models},
            "gpt": {"enabled": "gpt" in models, "use_mock": not args.use_real_gpt},
            "pynguin": {"enabled": "pynguin" in models},
        }
        
        # Run test generation on dataset subjects
        pipeline = TestGenerationPipeline(
            subjects_dir="subjects_dataset",
            output_dir="generated_tests",
            models_config=models_config
        )
        pipeline.run_all()
    
    # Stage 3: Standard evaluation (coverage, mutation)
    if "evaluate" in stages_to_run:
        print(f"\n{'='*70}")
        print("STAGE 3: STANDARD EVALUATION")
        print(f"{'='*70}\n")
        
        # Run tests
        print("\n--- Test Execution ---")
        from evaluation.run_tests import TestRunner
        
        runner = TestRunner(
            subjects_dir="subjects_dataset",
            generated_tests_dir="generated_tests",
            results_dir="results"
        )
        test_results = runner.run_all_tests()
        
        # Coverage
        print("\n--- Coverage Evaluation ---")
        from evaluation.coverage_eval import CoverageEvaluator
        
        evaluator = CoverageEvaluator(
            subjects_dir="subjects_dataset",
            generated_tests_dir="generated_tests",
            results_dir="results"
        )
        cov_results = evaluator.evaluate_all()
        
        # Mutation testing
        print("\n--- Mutation Testing ---")
        from evaluation.mutation_eval import MutationTester
        
        tester = MutationTester(
            subjects_dir="subjects_dataset",
            generated_tests_dir="generated_tests",
            results_dir="results",
            max_mutants_per_file=30  # Reduced for dataset subjects
        )
        mut_results = tester.evaluate_all()
        
        # Also run combined dataset evaluation
        print("\n--- Combined Dataset Evaluation ---")
        from evaluation.dataset_eval import DatasetBenchmarkEvaluator
        
        dataset_evaluator = DatasetBenchmarkEvaluator(
            subjects_dir="subjects_dataset",
            generated_tests_dir="generated_tests",
            results_dir="results"
        )
        
        dataset_results = dataset_evaluator.evaluate_all(
            run_coverage=False,  # Already done above
            run_mutation=False   # Already done above
        )
        dataset_summary = dataset_evaluator.summarize_results(dataset_results)
    
    # Final aggregation
    print(f"\n{'='*70}")
    print("FINAL AGGREGATION")
    print(f"{'='*70}\n")
    
    from evaluation.aggregate_results import ResultAggregator
    
    aggregator = ResultAggregator(results_dir="results")
    metrics = aggregator.save_results()
    
    print(aggregator.generate_report())
    
    print(f"""
{'='*70}
  DATASET BENCHMARK COMPLETE
{'='*70}

Results saved in: {base_dir / 'results'}

Key files:
  - metrics.csv                    : All metrics per subject
  - dataset_eval_results.csv       : Dataset evaluation summary
  - benchmark_report.txt           : Human-readable report
  
Evaluation metrics:
  - Test Execution: Syntax validity, runnability, pass rate
  - Coverage: Statement and branch coverage
  - Mutation: Mutation score (mutants killed / total)
  
Subjects from dataset: {base_dir / 'subjects_dataset'}
""")


if __name__ == "__main__":
    main()
