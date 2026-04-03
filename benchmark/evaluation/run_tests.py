"""
Run Tests - Execute generated tests and collect results.
Validates that generated tests are syntactically correct and runnable.
"""

import os
import sys
import json
import unittest
import subprocess
import tempfile
import traceback
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict
import importlib.util


@dataclass
class TestResult:
    """Result of running a test file."""
    test_file: str
    model: str
    subject: str
    syntax_valid: bool
    runnable: bool
    tests_run: int
    tests_passed: int
    tests_failed: int
    tests_errors: int
    error_message: str = ""
    execution_time: float = 0.0
    
    @property
    def pass_rate(self) -> float:
        if self.tests_run == 0:
            return 0.0
        return self.tests_passed / self.tests_run


class TestRunner:
    """
    Runs generated tests and collects results.
    """
    
    def __init__(
        self,
        subjects_dir: str = "subjects",
        generated_tests_dir: str = "generated_tests",
        results_dir: str = "results"
    ):
        """
        Initialize the test runner.
        
        Args:
            subjects_dir: Directory containing subject code
            generated_tests_dir: Directory containing generated tests
            results_dir: Directory to save results
        """
        self.base_dir = Path(__file__).parent.parent
        self.subjects_dir = self.base_dir / subjects_dir
        self.generated_tests_dir = self.base_dir / generated_tests_dir
        self.results_dir = self.base_dir / results_dir
        
        # Ensure results directory exists
        self.results_dir.mkdir(parents=True, exist_ok=True)
    
    def check_syntax(self, test_file: Path) -> Tuple[bool, str]:
        """
        Check if a test file has valid Python syntax.
        
        Args:
            test_file: Path to the test file
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            with open(test_file, 'r') as f:
                source = f.read()
            compile(source, test_file, 'exec')
            return True, ""
        except SyntaxError as e:
            return False, f"Syntax error at line {e.lineno}: {e.msg}"
        except Exception as e:
            return False, str(e)
    
    def run_test_file(
        self, 
        test_file: Path, 
        subject_file: Path,
        timeout: int = 60
    ) -> TestResult:
        """
        Run a test file and collect results.
        
        Args:
            test_file: Path to the test file
            subject_file: Path to the subject being tested
            timeout: Maximum execution time in seconds
            
        Returns:
            TestResult with execution details
        """
        model = test_file.parent.name
        subject = subject_file.stem
        
        result = TestResult(
            test_file=str(test_file),
            model=model,
            subject=subject,
            syntax_valid=False,
            runnable=False,
            tests_run=0,
            tests_passed=0,
            tests_failed=0,
            tests_errors=0,
        )
        
        # Check syntax first
        is_valid, error_msg = self.check_syntax(test_file)
        result.syntax_valid = is_valid
        if not is_valid:
            result.error_message = error_msg
            return result
        
        # Run the tests using subprocess for isolation
        try:
            start_time = datetime.now()
            
            # Create a runner script that imports the subject and runs tests
            runner_script = f'''
import sys
import unittest
import json
import builtins
import importlib

# Add paths
sys.path.insert(0, "{self.subjects_dir}")
sys.path.insert(0, "{test_file.parent}")

# Forcefully expose all symbols from the subject module to builtins
# This ensures that generated tests can run even if they missed the import statement
try:
    subject_module = importlib.import_module("{subject}")
    for name, obj in vars(subject_module).items():
        if not name.startswith("_"):
            setattr(builtins, name, obj)
except Exception:
    pass

# Load and run tests
loader = unittest.TestLoader()
suite = unittest.TestSuite()

try:
    # Try to load the test module
    import importlib.util
    spec = importlib.util.spec_from_file_location("test_module", "{test_file}")
    test_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(test_module)
    
    # Discover tests from the module
    suite = loader.loadTestsFromModule(test_module)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    
    # Output results as JSON
    output = {{
        "success": True,
        "tests_run": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
    }}
    print("RESULT:" + json.dumps(output))
    
except Exception as e:
    print("RESULT:" + json.dumps({{"success": False, "error": str(e)}}))
'''
            
            # Run the script
            proc = subprocess.run(
                [sys.executable, '-c', runner_script],
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=str(self.base_dir)
            )
            
            end_time = datetime.now()
            result.execution_time = (end_time - start_time).total_seconds()
            
            # Parse output
            output = proc.stdout + proc.stderr
            if "RESULT:" in output:
                json_str = output.split("RESULT:")[-1].strip().split('\n')[0]
                test_output = json.loads(json_str)
                
                if test_output.get("success"):
                    result.runnable = True
                    result.tests_run = test_output.get("tests_run", 0)
                    result.tests_failed = test_output.get("failures", 0)
                    result.tests_errors = test_output.get("errors", 0)
                    result.tests_passed = result.tests_run - result.tests_failed - result.tests_errors
                else:
                    result.error_message = test_output.get("error", "Unknown error")
            else:
                result.error_message = f"Unexpected output: {output[:200]}"
                
        except subprocess.TimeoutExpired:
            result.error_message = f"Timeout after {timeout}s"
        except json.JSONDecodeError as e:
            result.error_message = f"JSON parse error: {e}"
        except Exception as e:
            result.error_message = f"Execution error: {e}"
        
        return result
    
    def run_all_tests(self) -> List[TestResult]:
        """
        Run all generated tests for all subjects.
        
        Returns:
            List of TestResult objects
        """
        results = []
        
        print(f"\n{'='*60}")
        print("Running Generated Tests")
        print(f"{'='*60}\n")
        
        # Get all models (subdirectories in generated_tests)
        model_dirs = [d for d in self.generated_tests_dir.iterdir() if d.is_dir()]
        
        for model_dir in model_dirs:
            model_name = model_dir.name
            print(f"\n[{model_name}]")
            
            # Get all test files for this model
            test_files = list(model_dir.glob("test_*.py"))
            
            for test_file in test_files:
                # Find corresponding subject
                subject_name = test_file.stem.replace("test_", "")
                subject_file = self.subjects_dir / f"{subject_name}.py"
                
                if not subject_file.exists():
                    print(f"  ✗ {test_file.name} - Subject not found")
                    continue
                
                result = self.run_test_file(test_file, subject_file)
                results.append(result)
                
                if result.runnable:
                    print(f"  ✓ {test_file.name}: {result.tests_passed}/{result.tests_run} passed")
                elif result.syntax_valid:
                    print(f"  ⚠ {test_file.name}: Valid syntax but not runnable - {result.error_message[:50]}")
                else:
                    print(f"  ✗ {test_file.name}: Syntax error - {result.error_message[:50]}")
        
        # Save results
        self._save_results(results)
        
        return results
    
    def _save_results(self, results: List[TestResult]):
        """Save test results to JSON and CSV files."""
        # Save as JSON
        json_file = self.results_dir / "test_results.json"
        with open(json_file, 'w') as f:
            json.dump([asdict(r) for r in results], f, indent=2)
        
        # Save as CSV
        csv_file = self.results_dir / "test_results.csv"
        with open(csv_file, 'w') as f:
            headers = [
                "model", "subject", "syntax_valid", "runnable",
                "tests_run", "tests_passed", "tests_failed", "tests_errors",
                "pass_rate", "execution_time"
            ]
            f.write(",".join(headers) + "\n")
            
            for r in results:
                row = [
                    r.model, r.subject, str(r.syntax_valid), str(r.runnable),
                    str(r.tests_run), str(r.tests_passed), str(r.tests_failed),
                    str(r.tests_errors), f"{r.pass_rate:.2f}", f"{r.execution_time:.2f}"
                ]
                f.write(",".join(row) + "\n")
        
        print(f"\nResults saved to:")
        print(f"  - {json_file}")
        print(f"  - {csv_file}")
    
    def summarize_results(self, results: List[TestResult]) -> Dict:
        """
        Create a summary of test results by model.
        
        Args:
            results: List of TestResult objects
            
        Returns:
            Summary dictionary
        """
        summary = {}
        
        for result in results:
            model = result.model
            if model not in summary:
                summary[model] = {
                    "total_subjects": 0,
                    "syntax_valid": 0,
                    "runnable": 0,
                    "total_tests": 0,
                    "total_passed": 0,
                    "total_failed": 0,
                    "total_errors": 0,
                }
            
            s = summary[model]
            s["total_subjects"] += 1
            s["syntax_valid"] += 1 if result.syntax_valid else 0
            s["runnable"] += 1 if result.runnable else 0
            s["total_tests"] += result.tests_run
            s["total_passed"] += result.tests_passed
            s["total_failed"] += result.tests_failed
            s["total_errors"] += result.tests_errors
        
        # Calculate rates
        for model, s in summary.items():
            s["syntax_rate"] = s["syntax_valid"] / s["total_subjects"] if s["total_subjects"] > 0 else 0
            s["runnable_rate"] = s["runnable"] / s["total_subjects"] if s["total_subjects"] > 0 else 0
            s["pass_rate"] = s["total_passed"] / s["total_tests"] if s["total_tests"] > 0 else 0
        
        return summary


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Run generated tests")
    parser.add_argument("--subjects-dir", default="subjects", help="Subjects directory")
    parser.add_argument("--tests-dir", default="generated_tests", help="Generated tests directory")
    parser.add_argument("--results-dir", default="results", help="Results directory")
    parser.add_argument("--timeout", type=int, default=60, help="Timeout per test file")
    
    args = parser.parse_args()
    
    runner = TestRunner(
        subjects_dir=args.subjects_dir,
        generated_tests_dir=args.tests_dir,
        results_dir=args.results_dir
    )
    
    results = runner.run_all_tests()
    
    # Print summary
    summary = runner.summarize_results(results)
    
    print(f"\n{'='*60}")
    print("Summary by Model")
    print(f"{'='*60}")
    
    for model, stats in summary.items():
        print(f"\n{model}:")
        print(f"  Subjects: {stats['total_subjects']}")
        print(f"  Syntax Valid: {stats['syntax_valid']} ({stats['syntax_rate']:.1%})")
        print(f"  Runnable: {stats['runnable']} ({stats['runnable_rate']:.1%})")
        print(f"  Tests: {stats['total_passed']}/{stats['total_tests']} passed ({stats['pass_rate']:.1%})")


if __name__ == "__main__":
    main()
