"""
Mutation Testing Evaluation - Measure mutation score of generated tests.
Uses mutation testing to assess the quality of test assertions.
"""

import os
import sys
import re
import ast
import copy
import json
import subprocess
import tempfile
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, asdict, field
import random


@dataclass
class MutationResult:
    """Result of mutation testing for a test-subject pair."""
    model: str
    subject: str
    test_file: str
    subject_file: str
    total_mutants: int = 0
    killed_mutants: int = 0
    survived_mutants: int = 0
    timeout_mutants: int = 0
    error_mutants: int = 0
    mutation_score: float = 0.0
    mutant_details: List[Dict] = field(default_factory=list)
    error: str = ""
    success: bool = False


class MutationOperator:
    """Base class for mutation operators."""
    
    name: str = "base"
    
    def mutate(self, node: ast.AST) -> Optional[ast.AST]:
        """Apply mutation to an AST node."""
        raise NotImplementedError


class ArithmeticOperatorMutation(MutationOperator):
    """Replace arithmetic operators: + <-> -, * <-> /"""
    
    name = "AOR"
    
    replacements = {
        ast.Add: ast.Sub,
        ast.Sub: ast.Add,
        ast.Mult: ast.Div,
        ast.Div: ast.Mult,
        ast.Mod: ast.Mult,
        ast.FloorDiv: ast.Div,
    }
    
    def mutate(self, node: ast.AST) -> Optional[ast.AST]:
        if isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type in self.replacements:
                new_node = copy.deepcopy(node)
                new_node.op = self.replacements[op_type]()
                return new_node
        return None


class ComparisonOperatorMutation(MutationOperator):
    """Replace comparison operators: < <-> <=, > <-> >=, == <-> !="""
    
    name = "COR"
    
    replacements = {
        ast.Lt: ast.LtE,
        ast.LtE: ast.Lt,
        ast.Gt: ast.GtE,
        ast.GtE: ast.Gt,
        ast.Eq: ast.NotEq,
        ast.NotEq: ast.Eq,
    }
    
    def mutate(self, node: ast.AST) -> Optional[ast.AST]:
        if isinstance(node, ast.Compare) and len(node.ops) == 1:
            op_type = type(node.ops[0])
            if op_type in self.replacements:
                new_node = copy.deepcopy(node)
                new_node.ops = [self.replacements[op_type]()]
                return new_node
        return None


class BooleanOperatorMutation(MutationOperator):
    """Replace boolean operators: and <-> or"""
    
    name = "BOR"
    
    def mutate(self, node: ast.AST) -> Optional[ast.AST]:
        if isinstance(node, ast.BoolOp):
            new_node = copy.deepcopy(node)
            if isinstance(node.op, ast.And):
                new_node.op = ast.Or()
            else:
                new_node.op = ast.And()
            return new_node
        return None


class ConstantMutation(MutationOperator):
    """Mutate constant values: change numbers, toggle booleans"""
    
    name = "CON"
    
    def mutate(self, node: ast.AST) -> Optional[ast.AST]:
        if isinstance(node, ast.Constant):
            new_node = copy.deepcopy(node)
            if isinstance(node.value, bool):
                new_node.value = not node.value
            elif isinstance(node.value, int):
                new_node.value = node.value + 1
            elif isinstance(node.value, float):
                new_node.value = node.value + 1.0
            else:
                return None
            return new_node
        return None


class ReturnValueMutation(MutationOperator):
    """Mutate return statements: return None instead"""
    
    name = "RET"
    
    def mutate(self, node: ast.AST) -> Optional[ast.AST]:
        if isinstance(node, ast.Return) and node.value is not None:
            new_node = copy.deepcopy(node)
            new_node.value = ast.Constant(value=None)
            return new_node
        return None


class MutationTester:
    """
    Performs mutation testing on subject code using generated tests.
    """
    
    def __init__(
        self,
        subjects_dir: str = "subjects",
        generated_tests_dir: str = "generated_tests",
        results_dir: str = "results",
        max_mutants_per_file: int = 50
    ):
        """
        Initialize the mutation tester.
        
        Args:
            subjects_dir: Directory containing subject code
            generated_tests_dir: Directory containing generated tests
            results_dir: Directory to save results
            max_mutants_per_file: Maximum number of mutants to generate per file
        """
        self.base_dir = Path(__file__).parent.parent
        self.subjects_dir = self.base_dir / subjects_dir
        self.generated_tests_dir = self.base_dir / generated_tests_dir
        self.results_dir = self.base_dir / results_dir
        self.max_mutants = max_mutants_per_file
        
        self.operators = [
            ArithmeticOperatorMutation(),
            ComparisonOperatorMutation(),
            BooleanOperatorMutation(),
            ConstantMutation(),
            ReturnValueMutation(),
        ]
        
        self.results_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_mutants(self, source_code: str) -> List[Tuple[str, str, int]]:
        """
        Generate mutants for the given source code.
        
        Args:
            source_code: Original Python source code
            
        Returns:
            List of (mutated_code, mutation_description, line_number)
        """
        try:
            tree = ast.parse(source_code)
        except SyntaxError:
            return []
        
        mutants = []
        
        for node in ast.walk(tree):
            for operator in self.operators:
                mutated_node = operator.mutate(node)
                if mutated_node is not None:
                    # Create a copy of the tree with the mutation
                    mutated_tree = copy.deepcopy(tree)
                    
                    # Find and replace the node in the copied tree
                    replaced = self._replace_node(mutated_tree, node, mutated_node)
                    if replaced:
                        try:
                            mutated_code = ast.unparse(mutated_tree)
                            line_no = getattr(node, 'lineno', 0)
                            description = f"{operator.name} at line {line_no}"
                            mutants.append((mutated_code, description, line_no))
                        except:
                            pass
        
        # Limit number of mutants
        if len(mutants) > self.max_mutants:
            mutants = random.sample(mutants, self.max_mutants)
        
        return mutants
    
    def _replace_node(self, tree: ast.AST, old: ast.AST, new: ast.AST) -> bool:
        """Replace a node in the AST tree."""
        for node in ast.walk(tree):
            for field, value in ast.iter_fields(node):
                if isinstance(value, list):
                    for i, item in enumerate(value):
                        if self._nodes_equal(item, old):
                            value[i] = new
                            return True
                elif self._nodes_equal(value, old):
                    setattr(node, field, new)
                    return True
        return False
    
    def _nodes_equal(self, node1: Any, node2: Any) -> bool:
        """Check if two AST nodes are equal."""
        if type(node1) != type(node2):
            return False
        if not isinstance(node1, ast.AST):
            return False
        return (getattr(node1, 'lineno', 0) == getattr(node2, 'lineno', 0) and
                getattr(node1, 'col_offset', 0) == getattr(node2, 'col_offset', 0))
    
    def run_tests_on_mutant(
        self,
        test_file: Path,
        mutant_code: str,
        original_subject: Path,
        timeout: int = 30
    ) -> str:
        """
        Run tests on a mutant and determine if it's killed.
        
        Args:
            test_file: Path to the test file
            mutant_code: Mutated source code
            original_subject: Path to original subject file
            timeout: Timeout in seconds
            
        Returns:
            "killed", "survived", "timeout", or "error"
        """
        try:
            with tempfile.TemporaryDirectory() as tmpdir:
                # Write mutant to temp file
                mutant_file = Path(tmpdir) / original_subject.name
                with open(mutant_file, 'w') as f:
                    f.write(mutant_code)
                
                # Run tests with mutant
                runner_script = f'''
import sys
import unittest
sys.path.insert(0, "{tmpdir}")
sys.path.insert(0, "{test_file.parent}")

# Import mutant module
import {original_subject.stem}

# Load and run tests
import importlib.util
spec = importlib.util.spec_from_file_location("test_module", "{test_file}")
test_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_module)

loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(test_module)
runner = unittest.TextTestRunner(verbosity=0)
result = runner.run(suite)

# If any test failed, mutant is killed
if result.failures or result.errors:
    print("KILLED")
else:
    print("SURVIVED")
'''
                
                proc = subprocess.run(
                    [sys.executable, '-c', runner_script],
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    cwd=str(self.base_dir)
                )
                
                output = proc.stdout + proc.stderr
                if "KILLED" in output:
                    return "killed"
                elif "SURVIVED" in output:
                    return "survived"
                else:
                    return "error"
                    
        except subprocess.TimeoutExpired:
            return "timeout"
        except Exception as e:
            return "error"
    
    def test_mutants(
        self,
        test_file: Path,
        subject_file: Path
    ) -> MutationResult:
        """
        Run mutation testing for a test-subject pair.
        
        Args:
            test_file: Path to the test file
            subject_file: Path to the subject file
            
        Returns:
            MutationResult with mutation testing metrics
        """
        model = test_file.parent.name
        subject = subject_file.stem
        
        result = MutationResult(
            model=model,
            subject=subject,
            test_file=str(test_file),
            subject_file=str(subject_file),
        )
        
        # Read original source
        try:
            with open(subject_file, 'r') as f:
                source_code = f.read()
        except Exception as e:
            result.error = f"Could not read source: {e}"
            return result
        
        # Generate mutants
        mutants = self.generate_mutants(source_code)
        result.total_mutants = len(mutants)
        
        if not mutants:
            result.error = "No mutants generated"
            return result
        
        # Test each mutant
        for mutant_code, description, line_no in mutants:
            status = self.run_tests_on_mutant(
                test_file, mutant_code, subject_file
            )
            
            if status == "killed":
                result.killed_mutants += 1
            elif status == "survived":
                result.survived_mutants += 1
            elif status == "timeout":
                result.timeout_mutants += 1
            else:
                result.error_mutants += 1
            
            result.mutant_details.append({
                "description": description,
                "line": line_no,
                "status": status
            })
        
        # Calculate mutation score
        effective_mutants = result.killed_mutants + result.survived_mutants
        if effective_mutants > 0:
            result.mutation_score = result.killed_mutants / effective_mutants
        
        result.success = True
        return result
    
    def evaluate_all(self) -> List[MutationResult]:
        """
        Run mutation testing for all generated tests.
        
        Returns:
            List of MutationResult objects
        """
        results = []
        
        print(f"\n{'='*60}")
        print("Mutation Testing Evaluation")
        print(f"{'='*60}\n")
        
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
                
                print(f"  Testing {subject_name}...", end=" ", flush=True)
                result = self.test_mutants(test_file, subject_file)
                results.append(result)
                
                if result.success:
                    print(f"Score: {result.mutation_score:.1%} ({result.killed_mutants}/{result.total_mutants} killed)")
                else:
                    print(f"Error: {result.error[:30]}")
        
        self._save_results(results)
        
        return results
    
    def _save_results(self, results: List[MutationResult]):
        """Save mutation testing results."""
        # Save as JSON
        json_file = self.results_dir / "mutation_results.json"
        with open(json_file, 'w') as f:
            json.dump([asdict(r) for r in results], f, indent=2)
        
        # Save as CSV
        csv_file = self.results_dir / "mutation_results.csv"
        with open(csv_file, 'w') as f:
            headers = [
                "model", "subject", "mutation_score",
                "total_mutants", "killed", "survived", "timeout", "error"
            ]
            f.write(",".join(headers) + "\n")
            
            for r in results:
                row = [
                    r.model, r.subject, f"{r.mutation_score:.4f}",
                    str(r.total_mutants), str(r.killed_mutants),
                    str(r.survived_mutants), str(r.timeout_mutants),
                    str(r.error_mutants)
                ]
                f.write(",".join(row) + "\n")
        
        print(f"\nMutation results saved to:")
        print(f"  - {json_file}")
        print(f"  - {csv_file}")
    
    def summarize_results(self, results: List[MutationResult]) -> Dict:
        """Create summary statistics by model."""
        summary = {}
        
        for result in results:
            if not result.success:
                continue
            
            model = result.model
            if model not in summary:
                summary[model] = {
                    "subjects": 0,
                    "total_mutants": 0,
                    "killed": 0,
                    "survived": 0,
                    "total_score": 0.0,
                }
            
            s = summary[model]
            s["subjects"] += 1
            s["total_mutants"] += result.total_mutants
            s["killed"] += result.killed_mutants
            s["survived"] += result.survived_mutants
            s["total_score"] += result.mutation_score
        
        for model, s in summary.items():
            if s["subjects"] > 0:
                s["avg_mutation_score"] = s["total_score"] / s["subjects"]
            effective = s["killed"] + s["survived"]
            if effective > 0:
                s["overall_mutation_score"] = s["killed"] / effective
        
        return summary


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Run mutation testing")
    parser.add_argument("--subjects-dir", default="subjects", help="Subjects directory")
    parser.add_argument("--tests-dir", default="generated_tests", help="Generated tests directory")
    parser.add_argument("--results-dir", default="results", help="Results directory")
    parser.add_argument("--max-mutants", type=int, default=50, help="Max mutants per file")
    
    args = parser.parse_args()
    
    tester = MutationTester(
        subjects_dir=args.subjects_dir,
        generated_tests_dir=args.tests_dir,
        results_dir=args.results_dir,
        max_mutants_per_file=args.max_mutants
    )
    
    results = tester.evaluate_all()
    summary = tester.summarize_results(results)
    
    print(f"\n{'='*60}")
    print("Mutation Testing Summary by Model")
    print(f"{'='*60}")
    
    for model, stats in summary.items():
        print(f"\n{model}:")
        print(f"  Subjects: {stats['subjects']}")
        print(f"  Avg Mutation Score: {stats.get('avg_mutation_score', 0):.1%}")
        print(f"  Overall: {stats['killed']}/{stats['total_mutants']} killed")


if __name__ == "__main__":
    main()
