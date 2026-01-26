"""
Main Benchmark Runner - Orchestrates the complete benchmark pipeline.
Runs test generation, evaluation, and aggregation in sequence.
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(
        description="Run complete benchmark pipeline for test generation models"
    )
    
    parser.add_argument(
        "--stage",
        choices=["generate", "test", "coverage", "mutation", "aggregate", "all"],
        default="all",
        help="Which stage to run (default: all)"
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
        "--skip-generation",
        action="store_true",
        help="Skip test generation (use existing generated tests)"
    )
    parser.add_argument(
        "--subjects-dir",
        default="subjects",
        help="Directory containing subject code"
    )
    parser.add_argument(
        "--output-dir",
        default="generated_tests",
        help="Directory for generated tests"
    )
    parser.add_argument(
        "--results-dir",
        default="results",
        help="Directory for results"
    )
    
    args = parser.parse_args()
    
    base_dir = Path(__file__).parent
    
    print(f"""
{'='*70}
  TEST GENERATION BENCHMARK SUITE
  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'='*70}

Subjects Directory: {base_dir / args.subjects_dir}
Output Directory:   {base_dir / args.output_dir}
Results Directory:  {base_dir / args.results_dir}
""")
    
    stages_to_run = []
    if args.stage == "all":
        stages_to_run = ["generate", "test", "coverage", "mutation", "aggregate"]
    else:
        stages_to_run = [args.stage]
    
    if args.skip_generation and "generate" in stages_to_run:
        stages_to_run.remove("generate")
    
    # Stage 1: Generate tests
    if "generate" in stages_to_run:
        print(f"\n{'='*70}")
        print("STAGE 1: TEST GENERATION")
        print(f"{'='*70}\n")
        
        from models.run_all_models import TestGenerationPipeline
        
        models = args.models if "all" not in args.models else ["your_model", "gpt", "pynguin"]
        models_config = {
            "your_model": {"enabled": "your_model" in models},
            "gpt": {"enabled": "gpt" in models, "use_mock": not args.use_real_gpt},
            "pynguin": {"enabled": "pynguin" in models},
        }
        
        pipeline = TestGenerationPipeline(
            subjects_dir=args.subjects_dir,
            output_dir=args.output_dir,
            models_config=models_config
        )
        pipeline.run_all()
    
    # Stage 2: Run tests
    if "test" in stages_to_run:
        print(f"\n{'='*70}")
        print("STAGE 2: TEST EXECUTION")
        print(f"{'='*70}\n")
        
        from evaluation.run_tests import TestRunner
        
        runner = TestRunner(
            subjects_dir=args.subjects_dir,
            generated_tests_dir=args.output_dir,
            results_dir=args.results_dir
        )
        results = runner.run_all_tests()
        summary = runner.summarize_results(results)
        
        for model, stats in summary.items():
            print(f"\n{model}: {stats['runnable']}/{stats['total_subjects']} runnable")
    
    # Stage 3: Coverage evaluation
    if "coverage" in stages_to_run:
        print(f"\n{'='*70}")
        print("STAGE 3: COVERAGE EVALUATION")
        print(f"{'='*70}\n")
        
        from evaluation.coverage_eval import CoverageEvaluator
        
        evaluator = CoverageEvaluator(
            subjects_dir=args.subjects_dir,
            generated_tests_dir=args.output_dir,
            results_dir=args.results_dir
        )
        results = evaluator.evaluate_all()
        summary = evaluator.summarize_results(results)
        
        for model, stats in summary.items():
            print(f"\n{model}: {stats.get('avg_statement_coverage', 0):.1%} statement coverage")
    
    # Stage 4: Mutation testing
    if "mutation" in stages_to_run:
        print(f"\n{'='*70}")
        print("STAGE 4: MUTATION TESTING")
        print(f"{'='*70}\n")
        
        from evaluation.mutation_eval import MutationTester
        
        tester = MutationTester(
            subjects_dir=args.subjects_dir,
            generated_tests_dir=args.output_dir,
            results_dir=args.results_dir
        )
        results = tester.evaluate_all()
        summary = tester.summarize_results(results)
        
        for model, stats in summary.items():
            print(f"\n{model}: {stats.get('avg_mutation_score', 0):.1%} mutation score")
    
    # Stage 5: Aggregate results
    if "aggregate" in stages_to_run:
        print(f"\n{'='*70}")
        print("STAGE 5: RESULTS AGGREGATION")
        print(f"{'='*70}\n")
        
        from evaluation.aggregate_results import ResultAggregator
        
        aggregator = ResultAggregator(results_dir=args.results_dir)
        metrics = aggregator.save_results()
        
        print("\n" + aggregator.generate_report())
    
    print(f"""
{'='*70}
  BENCHMARK COMPLETE
{'='*70}

Results saved in: {base_dir / args.results_dir}

Key files:
  - metrics.csv           : All metrics in CSV format
  - benchmark_report.txt  : Human-readable report
  - model_summary.json    : Summary statistics by model
""")


if __name__ == "__main__":
    main()
