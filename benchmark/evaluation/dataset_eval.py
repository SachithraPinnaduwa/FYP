"""
Dataset Benchmark Evaluation - Evaluate generated tests on dataset subjects.
Uses standard metrics: test execution, coverage, and mutation testing.
Optionally compares assertion patterns to ground truth for reference.
"""

import os
import sys
import json
import ast
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict, field

# Import the standard evaluation modules
sys.path.insert(0, str(Path(__file__).parent.parent))


@dataclass
class DatasetEvalResult:
    """Evaluation result for a dataset subject."""
    model: str
    subject_id: str
    question: str  # Problem description from dataset
    
    # Test execution metrics
    syntax_valid: bool = False
    runnable: bool = False
    tests_run: int = 0
    tests_passed: int = 0
    tests_failed: int = 0
    execution_time: float = 0.0
    
    # Coverage metrics
    statement_coverage: float = 0.0
    branch_coverage: float = 0.0
    statements_covered: int = 0
    statements_total: int = 0
    
    # Mutation testing metrics
    mutation_score: float = 0.0
    mutants_killed: int = 0
    mutants_total: int = 0
    
    # Reference info (not for comparison, just metadata)
    has_ground_truth: bool = False
    ground_truth_test_count: int = 0
    
    error: str = ""


class DatasetBenchmarkEvaluator:
    """
    Evaluates generated tests on dataset subjects using standard metrics.
    """
    
    def __init__(
        self,
        subjects_dir: str = "subjects_dataset",
        generated_tests_dir: str = "generated_tests",
        results_dir: str = "results"
    ):
        """Initialize the evaluator."""
        self.base_dir = Path(__file__).parent.parent
        self.subjects_dir = self.base_dir / subjects_dir
        self.generated_tests_dir = self.base_dir / generated_tests_dir
        self.results_dir = self.base_dir / results_dir
        
        self.results_dir.mkdir(parents=True, exist_ok=True)
        
        # Load subjects metadata
        self.subjects_metadata = self._load_metadata()
    
    def _load_metadata(self) -> Dict:
        """Load subjects metadata."""
        metadata_file = self.subjects_dir / "subjects_metadata.json"
        if metadata_file.exists():
            with open(metadata_file, 'r') as f:
                data = json.load(f)
                return {item['id']: item for item in data}
        return {}
    
    def get_dataset_subjects(self) -> List[Tuple[str, Path]]:
        """Get all dataset subject files."""
        subjects = []
        for file in self.subjects_dir.glob("subject_*.py"):
            subject_id = file.stem
            subjects.append((subject_id, file))
        return sorted(subjects)
    
    def evaluate_all(
        self,
        run_coverage: bool = True,
        run_mutation: bool = True,
        max_mutants: int = 30
    ) -> List[DatasetEvalResult]:
        """
        Evaluate all generated tests using standard metrics.
        
        Args:
            run_coverage: Whether to run coverage evaluation
            run_mutation: Whether to run mutation testing
            max_mutants: Maximum mutants per subject for mutation testing
            
        Returns:
            List of DatasetEvalResult objects
        """
        from evaluation.run_tests import TestRunner
        from evaluation.coverage_eval import CoverageEvaluator
        from evaluation.mutation_eval import MutationTester
        
        results = []
        
        print(f"\n{'='*60}")
        print("Dataset Benchmark Evaluation")
        print("Using standard metrics: Execution, Coverage, Mutation")
        print(f"{'='*60}\n")
        
        # Get all model directories
        model_dirs = [d for d in self.generated_tests_dir.iterdir() if d.is_dir()]
        
        # Initialize evaluators
        test_runner = TestRunner(
            subjects_dir=str(self.subjects_dir.relative_to(self.base_dir)),
            generated_tests_dir=str(self.generated_tests_dir.relative_to(self.base_dir)),
            results_dir=str(self.results_dir.relative_to(self.base_dir))
        )
        
        if run_coverage:
            coverage_eval = CoverageEvaluator(
                subjects_dir=str(self.subjects_dir.relative_to(self.base_dir)),
                generated_tests_dir=str(self.generated_tests_dir.relative_to(self.base_dir)),
                results_dir=str(self.results_dir.relative_to(self.base_dir))
            )
        
        if run_mutation:
            mutation_tester = MutationTester(
                subjects_dir=str(self.subjects_dir.relative_to(self.base_dir)),
                generated_tests_dir=str(self.generated_tests_dir.relative_to(self.base_dir)),
                results_dir=str(self.results_dir.relative_to(self.base_dir)),
                max_mutants_per_file=max_mutants
            )
        
        for model_dir in model_dirs:
            model_name = model_dir.name
            print(f"\n[{model_name}]")
            
            # Find test files for dataset subjects
            for test_file in sorted(model_dir.glob("test_subject_*.py")):
                subject_id = test_file.stem.replace("test_", "")
                subject_file = self.subjects_dir / f"{subject_id}.py"
                
                if not subject_file.exists():
                    continue
                
                # Get metadata
                metadata = self.subjects_metadata.get(subject_id, {})
                question = metadata.get("question", "")[:100]
                ground_truth_tests = metadata.get("ground_truth_tests", [])
                
                result = DatasetEvalResult(
                    model=model_name,
                    subject_id=subject_id,
                    question=question,
                    has_ground_truth=len(ground_truth_tests) > 0,
                    ground_truth_test_count=len(ground_truth_tests)
                )
                
                # 1. Run test execution
                test_result = test_runner.run_test_file(test_file, subject_file)
                result.syntax_valid = test_result.syntax_valid
                result.runnable = test_result.runnable
                result.tests_run = test_result.tests_run
                result.tests_passed = test_result.tests_passed
                result.tests_failed = test_result.tests_failed
                result.execution_time = test_result.execution_time
                
                # 2. Run coverage evaluation
                if run_coverage and result.runnable:
                    try:
                        cov_result = coverage_eval.measure_coverage(test_file, subject_file)
                        result.statement_coverage = cov_result.statement_coverage
                        result.branch_coverage = cov_result.branch_coverage
                        result.statements_covered = cov_result.statements_covered
                        result.statements_total = cov_result.statements_total
                    except Exception as e:
                        result.error = f"Coverage error: {e}"
                
                # 3. Run mutation testing
                if run_mutation and result.runnable:
                    try:
                        mut_result = mutation_tester.test_mutants(test_file, subject_file)
                        result.mutation_score = mut_result.mutation_score
                        result.mutants_killed = mut_result.killed_mutants
                        result.mutants_total = mut_result.total_mutants
                    except Exception as e:
                        if not result.error:
                            result.error = f"Mutation error: {e}"
                
                results.append(result)
                
                # Print status
                status = "✓" if result.runnable else ("⚠" if result.syntax_valid else "✗")
                print(f"  {status} {subject_id}: "
                      f"Tests={result.tests_passed}/{result.tests_run}, "
                      f"Cov={result.statement_coverage:.1%}, "
                      f"Mut={result.mutation_score:.1%}")
        
        self._save_results(results)
        
        return results
    
    def _save_results(self, results: List[DatasetEvalResult]):
        """Save evaluation results."""
        # Save as JSON
        json_file = self.results_dir / "dataset_eval_results.json"
        with open(json_file, 'w') as f:
            json.dump([asdict(r) for r in results], f, indent=2)
        
        # Save as CSV
        csv_file = self.results_dir / "dataset_eval_results.csv"
        with open(csv_file, 'w') as f:
            headers = [
                "model", "subject_id", "syntax_valid", "runnable",
                "tests_run", "tests_passed", "tests_failed",
                "statement_coverage", "branch_coverage",
                "mutation_score", "mutants_killed", "mutants_total",
                "has_ground_truth"
            ]
            f.write(",".join(headers) + "\n")
            
            for r in results:
                row = [
                    r.model, r.subject_id, str(r.syntax_valid), str(r.runnable),
                    str(r.tests_run), str(r.tests_passed), str(r.tests_failed),
                    f"{r.statement_coverage:.4f}", f"{r.branch_coverage:.4f}",
                    f"{r.mutation_score:.4f}", str(r.mutants_killed), str(r.mutants_total),
                    str(r.has_ground_truth)
                ]
                f.write(",".join(row) + "\n")
        
        print(f"\nDataset evaluation results saved to:")
        print(f"  - {json_file}")
        print(f"  - {csv_file}")
        
        # Save as Excel
        try:
            import pandas as pd
            excel_file = self.results_dir / "dataset_eval_results.xlsx"
            df = pd.DataFrame([asdict(r) for r in results])
            
            df.to_excel(excel_file, index=False)
            print(f"  - {excel_file}")
        except ImportError:
            print("  - Pandas or openpyxl not installed, skipping Excel export")
            pass
    
    def summarize_results(self, results: List[DatasetEvalResult]) -> Dict:
        """Create summary statistics by model."""
        summary = {}
        
        for result in results:
            model = result.model
            if model not in summary:
                summary[model] = {
                    "subjects": 0,
                    "syntax_valid": 0,
                    "runnable": 0,
                    "total_tests_run": 0,
                    "total_tests_passed": 0,
                    "total_statement_coverage": 0.0,
                    "total_branch_coverage": 0.0,
                    "total_mutation_score": 0.0,
                    "coverage_count": 0,  # Count of subjects with coverage data
                    "mutation_count": 0,  # Count of subjects with mutation data
                }
            
            s = summary[model]
            s["subjects"] += 1
            s["syntax_valid"] += 1 if result.syntax_valid else 0
            s["runnable"] += 1 if result.runnable else 0
            s["total_tests_run"] += result.tests_run
            s["total_tests_passed"] += result.tests_passed
            
            if result.statement_coverage > 0:
                s["total_statement_coverage"] += result.statement_coverage
                s["total_branch_coverage"] += result.branch_coverage
                s["coverage_count"] += 1
            
            if result.mutants_total > 0:
                s["total_mutation_score"] += result.mutation_score
                s["mutation_count"] += 1
        
        # Calculate averages
        for model, s in summary.items():
            n = s["subjects"]
            if n > 0:
                s["syntax_rate"] = s["syntax_valid"] / n
                s["runnable_rate"] = s["runnable"] / n
            if s["total_tests_run"] > 0:
                s["overall_pass_rate"] = s["total_tests_passed"] / s["total_tests_run"]
            else:
                s["overall_pass_rate"] = 0.0
            if s["coverage_count"] > 0:
                s["avg_statement_coverage"] = s["total_statement_coverage"] / s["coverage_count"]
                s["avg_branch_coverage"] = s["total_branch_coverage"] / s["coverage_count"]
            if s["mutation_count"] > 0:
                s["avg_mutation_score"] = s["total_mutation_score"] / s["mutation_count"]
        
        return summary


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Evaluate generated tests on dataset subjects")
    parser.add_argument("--subjects-dir", default="subjects_dataset", help="Dataset subjects directory")
    parser.add_argument("--tests-dir", default="generated_tests", help="Generated tests directory")
    parser.add_argument("--results-dir", default="results", help="Results directory")
    parser.add_argument("--skip-coverage", action="store_true", help="Skip coverage evaluation")
    parser.add_argument("--skip-mutation", action="store_true", help="Skip mutation testing")
    parser.add_argument("--max-mutants", type=int, default=30, help="Max mutants per subject")
    
    args = parser.parse_args()
    
    evaluator = DatasetBenchmarkEvaluator(
        subjects_dir=args.subjects_dir,
        generated_tests_dir=args.tests_dir,
        results_dir=args.results_dir
    )
    
    results = evaluator.evaluate_all(
        run_coverage=not args.skip_coverage,
        run_mutation=not args.skip_mutation,
        max_mutants=args.max_mutants
    )
    
    summary = evaluator.summarize_results(results)
    
    print(f"\n{'='*60}")
    print("Dataset Benchmark Summary by Model")
    print(f"{'='*60}")
    
    for model, stats in summary.items():
        print(f"\n{model}:")
        print(f"  Subjects: {stats['subjects']}")
        print(f"  Syntax Valid: {stats.get('syntax_rate', 0):.1%}")
        print(f"  Runnable: {stats.get('runnable_rate', 0):.1%}")
        print(f"  Avg Statement Coverage: {stats.get('avg_statement_coverage', 0):.1%}")
        print(f"  Avg Branch Coverage: {stats.get('avg_branch_coverage', 0):.1%}")
        print(f"  Avg Mutation Score: {stats.get('avg_mutation_score', 0):.1%}")


if __name__ == "__main__":
    main()
