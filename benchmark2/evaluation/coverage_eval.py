"""
Coverage Evaluation - Measure code coverage achieved by generated tests.
Uses Python's coverage.py library to measure statement and branch coverage.
"""

import os
import sys
import json
import subprocess
import tempfile
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict, field


@dataclass
class CoverageResult:
    """Coverage result for a test-subject pair."""
    model: str
    subject: str
    test_file: str
    subject_file: str
    statement_coverage: float = 0.0
    statements_covered: int = 0
    statements_total: int = 0
    missing_lines: List[int] = field(default_factory=list)
    error: str = ""
    success: bool = False


class CoverageEvaluator:
    """
    Evaluates code coverage for generated tests.
    """
    
    def __init__(
        self,
        subjects_dir: str = "subjects",
        generated_tests_dir: str = "generated_tests",
        results_dir: str = "results"
    ):
        """
        Initialize the coverage evaluator.
        
        Args:
            subjects_dir: Directory containing subject code
            generated_tests_dir: Directory containing generated tests
            results_dir: Directory to save results
        """
        self.base_dir = Path(__file__).parent.parent
        self.subjects_dir = self.base_dir / subjects_dir
        self.generated_tests_dir = self.base_dir / generated_tests_dir
        self.results_dir = self.base_dir / results_dir
        
        self.results_dir.mkdir(parents=True, exist_ok=True)
    
    def measure_coverage(
        self,
        test_file: Path,
        subject_file: Path,
        timeout: int = 120
    ) -> CoverageResult:
        """
        Measure code coverage for a test file against its subject.
        
        Args:
            test_file: Path to the test file
            subject_file: Path to the subject being tested
            timeout: Maximum execution time in seconds
            
        Returns:
            CoverageResult with coverage metrics
        """
        model = test_file.parent.name
        subject = subject_file.stem
        
        result = CoverageResult(
            model=model,
            subject=subject,
            test_file=str(test_file),
            subject_file=str(subject_file),
        )
        
        try:
            with tempfile.TemporaryDirectory() as tmpdir:
                coverage_file = Path(tmpdir) / ".coverage"
                json_report = Path(tmpdir) / "coverage.json"
                
                # Create a coverage runner script
                runner_script = f'''
import sys
import coverage
import unittest

# Start coverage
cov = coverage.Coverage(
    source=["{subject_file.parent}"],
    data_file="{coverage_file}"
)
cov.start()

# Add paths
sys.path.insert(0, "{self.subjects_dir}")
sys.path.insert(0, "{test_file.parent}")

try:
    # Import subject module first
    import {subject}
    
    # Load test module
    import importlib.util
    spec = importlib.util.spec_from_file_location("test_module", "{test_file}")
    test_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(test_module)
    
    # Run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_module)
    runner = unittest.TextTestRunner(verbosity=0)
    runner.run(suite)
    
except Exception as e:
    print(f"ERROR: {{e}}", file=sys.stderr)

# Stop and save coverage
cov.stop()
cov.save()

# Generate JSON report
cov.json_report(outfile="{json_report}")
print("COVERAGE_DONE")
'''
                
                # Run coverage
                proc = subprocess.run(
                    [sys.executable, '-c', runner_script],
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    cwd=str(self.base_dir)
                )
                
                if "COVERAGE_DONE" not in proc.stdout:
                    result.error = f"Coverage failed: {proc.stderr[:200]}"
                    return result
                
                # Parse JSON report
                if json_report.exists():
                    with open(json_report, 'r') as f:
                        cov_data = json.load(f)
                    
                    # Find subject file in coverage data
                    for file_path, file_data in cov_data.get("files", {}).items():
                        if subject in file_path:
                            summary = file_data.get("summary", {})
                            
                            result.statements_covered = summary.get("covered_lines", 0)
                            result.statements_total = summary.get("num_statements", 0)
                            result.statement_coverage = summary.get("percent_covered", 0) / 100
                            
                            
                            result.missing_lines = file_data.get("missing_lines", [])
                            result.success = True
                            break
                    
                    if not result.success:
                        # Check totals
                        totals = cov_data.get("totals", {})
                        result.statements_covered = totals.get("covered_lines", 0)
                        result.statements_total = totals.get("num_statements", 0)
                        if result.statements_total > 0:
                            result.statement_coverage = result.statements_covered / result.statements_total
                        result.success = True
                else:
                    result.error = "Coverage report not generated"
                    
        except subprocess.TimeoutExpired:
            result.error = f"Timeout after {timeout}s"
        except Exception as e:
            result.error = str(e)
        
        return result
    
    def evaluate_all(self) -> List[CoverageResult]:
        """
        Evaluate coverage for all generated tests.
        
        Returns:
            List of CoverageResult objects
        """
        results = []
        
        print(f"\n{'='*60}")
        print("Coverage Evaluation")
        print(f"{'='*60}\n")
        
        # Get all model directories
        model_dirs = [d for d in self.generated_tests_dir.iterdir() if d.is_dir()]
        
        for model_dir in model_dirs:
            model_name = model_dir.name
            print(f"\n[{model_name}]")
            
            test_files = list(model_dir.glob("test_*.py"))
            
            for test_file in test_files:
                subject_name = test_file.stem.replace("test_", "")
                subject_file = self.subjects_dir / f"{subject_name}.py"
                
                if not subject_file.exists():
                    print(f"  ✗ {test_file.name} - Subject not found")
                    continue
                
                result = self.measure_coverage(test_file, subject_file)
                results.append(result)
                
                if result.success:
                    print(f"  ✓ {subject_name}: Statement={result.statement_coverage:.1%}")
                else:
                    print(f"  ✗ {subject_name}: {result.error[:50]}")
        
        self._save_results(results)
        
        return results
    
    def _save_results(self, results: List[CoverageResult]):
        """Save coverage results to files."""
        # Save as JSON
        json_file = self.results_dir / "coverage_results.json"
        with open(json_file, 'w') as f:
            json.dump([asdict(r) for r in results], f, indent=2)
        
        # Save as CSV
        csv_file = self.results_dir / "coverage_results.csv"
        with open(csv_file, 'w') as f:
            headers = [
                "model", "subject", "statement_coverage",
                "statements_covered", "statements_total", "success"
            ]
            f.write(",".join(headers) + "\n")
            
            for r in results:
                row = [
                    r.model, r.subject,
                    f"{r.statement_coverage:.4f}",
                    str(r.statements_covered), str(r.statements_total),
                    str(r.success)
                ]
                f.write(",".join(row) + "\n")
        
        print(f"\nCoverage results saved to:")
        print(f"  - {json_file}")
        print(f"  - {csv_file}")
    
    def summarize_results(self, results: List[CoverageResult]) -> Dict:
        """Create summary statistics by model."""
        summary = {}
        
        for result in results:
            if not result.success:
                continue
                
            model = result.model
            if model not in summary:
                summary[model] = {
                    "subjects": 0,
                    "total_statement_coverage": 0.0,
                    "statements_covered": 0,
                    "statements_total": 0,
                }
            
            s = summary[model]
            s["subjects"] += 1
            s["total_statement_coverage"] += result.statement_coverage
            s["statements_covered"] += result.statements_covered
            s["statements_total"] += result.statements_total
        
        # Calculate averages
        for model, s in summary.items():
            if s["subjects"] > 0:
                s["avg_statement_coverage"] = s["total_statement_coverage"] / s["subjects"]
            if s["statements_total"] > 0:
                s["overall_statement_coverage"] = s["statements_covered"] / s["statements_total"]
        
        return summary


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Evaluate test coverage")
    parser.add_argument("--subjects-dir", default="subjects", help="Subjects directory")
    parser.add_argument("--tests-dir", default="generated_tests", help="Generated tests directory")
    parser.add_argument("--results-dir", default="results", help="Results directory")
    parser.add_argument("--timeout", type=int, default=120, help="Timeout per coverage run")
    
    args = parser.parse_args()
    
    evaluator = CoverageEvaluator(
        subjects_dir=args.subjects_dir,
        generated_tests_dir=args.tests_dir,
        results_dir=args.results_dir
    )
    
    results = evaluator.evaluate_all()
    summary = evaluator.summarize_results(results)
    
    print(f"\n{'='*60}")
    print("Coverage Summary by Model")
    print(f"{'='*60}")
    
    for model, stats in summary.items():
        print(f"\n{model}:")
        print(f"  Subjects evaluated: {stats['subjects']}")
        print(f"  Avg Statement Coverage: {stats.get('avg_statement_coverage', 0):.1%}")
        print(f"  Overall Statement: {stats['statements_covered']}/{stats['statements_total']}")


if __name__ == "__main__":
    main()
