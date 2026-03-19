"""
Aggregate Results - Combine all evaluation metrics into a unified report.
Generates comprehensive comparison tables and visualizations.
"""

import os
import sys
import json
import csv
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict


@dataclass
class AggregatedMetrics:
    """Aggregated metrics for a model-subject pair."""
    model: str
    subject: str
    
    # Test execution metrics
    syntax_valid: bool = False
    runnable: bool = False
    tests_run: int = 0
    tests_passed: int = 0
    test_pass_rate: float = 0.0
    
    # Coverage metrics
    statement_coverage: float = 0.0
    branch_coverage: float = 0.0
    
    # Mutation testing metrics
    mutation_score: float = 0.0
    mutants_killed: int = 0
    mutants_total: int = 0
    
    # Composite score
    composite_score: float = 0.0


class ResultAggregator:
    """
    Aggregates results from all evaluation phases.
    """
    
    def __init__(self, results_dir: str = "results"):
        """
        Initialize the aggregator.
        
        Args:
            results_dir: Directory containing result files
        """
        self.base_dir = Path(__file__).parent.parent
        self.results_dir = self.base_dir / results_dir
    
    def load_test_results(self) -> Dict:
        """Load test execution results."""
        results_file = self.results_dir / "test_results.json"
        if results_file.exists():
            with open(results_file, 'r') as f:
                return {(r["model"], r["subject"]): r for r in json.load(f)}
        return {}
    
    def load_coverage_results(self) -> Dict:
        """Load coverage results."""
        results_file = self.results_dir / "coverage_results.json"
        if results_file.exists():
            with open(results_file, 'r') as f:
                return {(r["model"], r["subject"]): r for r in json.load(f)}
        return {}
    
    def load_mutation_results(self) -> Dict:
        """Load mutation testing results."""
        results_file = self.results_dir / "mutation_results.json"
        if results_file.exists():
            with open(results_file, 'r') as f:
                return {(r["model"], r["subject"]): r for r in json.load(f)}
        return {}
    
    def aggregate(self) -> List[AggregatedMetrics]:
        """
        Aggregate all results into unified metrics.
        
        Returns:
            List of AggregatedMetrics objects
        """
        test_results = self.load_test_results()
        coverage_results = self.load_coverage_results()
        mutation_results = self.load_mutation_results()
        
        # Get all unique (model, subject) pairs
        all_keys = set(test_results.keys()) | set(coverage_results.keys()) | set(mutation_results.keys())
        
        aggregated = []
        
        for model, subject in sorted(all_keys):
            metrics = AggregatedMetrics(model=model, subject=subject)
            
            # Test results
            if (model, subject) in test_results:
                tr = test_results[(model, subject)]
                metrics.syntax_valid = tr.get("syntax_valid", False)
                metrics.runnable = tr.get("runnable", False)
                metrics.tests_run = tr.get("tests_run", 0)
                metrics.tests_passed = tr.get("tests_passed", 0)
                if metrics.tests_run > 0:
                    metrics.test_pass_rate = metrics.tests_passed / metrics.tests_run
            
            # Coverage results
            if (model, subject) in coverage_results:
                cr = coverage_results[(model, subject)]
                metrics.statement_coverage = cr.get("statement_coverage", 0.0)
                metrics.branch_coverage = cr.get("branch_coverage", 0.0)
            
            # Mutation results
            if (model, subject) in mutation_results:
                mr = mutation_results[(model, subject)]
                metrics.mutation_score = mr.get("mutation_score", 0.0)
                metrics.mutants_killed = mr.get("killed_mutants", 0)
                metrics.mutants_total = mr.get("total_mutants", 0)
            
            # Calculate composite score (weighted average)
            # Weights: runnability 0.1, coverage 0.4, mutation 0.5
            runnable_score = 1.0 if metrics.runnable else 0.0
            coverage_score = (metrics.statement_coverage + metrics.branch_coverage) / 2
            
            metrics.composite_score = (
                0.1 * runnable_score +
                0.4 * coverage_score +
                0.5 * metrics.mutation_score
            )
            
            aggregated.append(metrics)
        
        return aggregated
    
    def summarize_by_model(self, metrics: List[AggregatedMetrics]) -> Dict:
        """Create summary statistics by model."""
        summary = {}
        
        for m in metrics:
            if m.model not in summary:
                summary[m.model] = {
                    "subjects": 0,
                    "syntax_valid": 0,
                    "runnable": 0,
                    "total_tests_run": 0,
                    "total_tests_passed": 0,
                    "total_statement_coverage": 0.0,
                    "total_branch_coverage": 0.0,
                    "total_mutation_score": 0.0,
                    "total_composite_score": 0.0,
                }
            
            s = summary[m.model]
            s["subjects"] += 1
            s["syntax_valid"] += 1 if m.syntax_valid else 0
            s["runnable"] += 1 if m.runnable else 0
            s["total_tests_run"] += m.tests_run
            s["total_tests_passed"] += m.tests_passed
            s["total_statement_coverage"] += m.statement_coverage
            s["total_branch_coverage"] += m.branch_coverage
            s["total_mutation_score"] += m.mutation_score
            s["total_composite_score"] += m.composite_score
        
        # Calculate averages
        for model, s in summary.items():
            n = s["subjects"]
            if n > 0:
                s["syntax_rate"] = s["syntax_valid"] / n
                s["runnable_rate"] = s["runnable"] / n
                s["avg_statement_coverage"] = s["total_statement_coverage"] / n
                s["avg_branch_coverage"] = s["total_branch_coverage"] / n
                s["avg_mutation_score"] = s["total_mutation_score"] / n
                s["avg_composite_score"] = s["total_composite_score"] / n
            if s["total_tests_run"] > 0:
                s["test_pass_rate"] = s["total_tests_passed"] / s["total_tests_run"]
        
        return summary
    
    def generate_report(self) -> str:
        """
        Generate a comprehensive text report.
        
        Returns:
            Report as a formatted string
        """
        metrics = self.aggregate()
        summary = self.summarize_by_model(metrics)
        
        report = []
        report.append("=" * 80)
        report.append("TEST GENERATION BENCHMARK REPORT")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 80)
        
        # Model comparison table
        report.append("\n### MODEL COMPARISON ###\n")
        
        headers = ["Model", "Syntax%", "Run%", "Stmt Cov%", "Branch Cov%", "Mutation%", "Composite"]
        col_widths = [15, 10, 10, 12, 12, 12, 12]
        
        header_row = "".join(h.ljust(w) for h, w in zip(headers, col_widths))
        report.append(header_row)
        report.append("-" * sum(col_widths))
        
        for model, s in sorted(summary.items()):
            row = [
                model[:14],
                f"{s.get('syntax_rate', 0)*100:.1f}%",
                f"{s.get('runnable_rate', 0)*100:.1f}%",
                f"{s.get('avg_statement_coverage', 0)*100:.1f}%",
                f"{s.get('avg_branch_coverage', 0)*100:.1f}%",
                f"{s.get('avg_mutation_score', 0)*100:.1f}%",
                f"{s.get('avg_composite_score', 0)*100:.1f}%",
            ]
            report.append("".join(str(r).ljust(w) for r, w in zip(row, col_widths)))
        
        # Detailed results by subject
        report.append("\n\n### DETAILED RESULTS BY SUBJECT ###\n")
        
        # Group by subject
        subjects = {}
        for m in metrics:
            if m.subject not in subjects:
                subjects[m.subject] = {}
            subjects[m.subject][m.model] = m
        
        for subject, models in sorted(subjects.items()):
            report.append(f"\n[{subject}]")
            for model, m in sorted(models.items()):
                status = "✓" if m.runnable else "✗"
                report.append(
                    f"  {model:15} {status} "
                    f"Cov:{m.statement_coverage*100:5.1f}% "
                    f"Mut:{m.mutation_score*100:5.1f}% "
                    f"Score:{m.composite_score*100:5.1f}%"
                )
        
        # Winner declaration
        report.append("\n\n### RANKING ###\n")
        ranked = sorted(summary.items(), key=lambda x: x[1].get('avg_composite_score', 0), reverse=True)
        for i, (model, s) in enumerate(ranked, 1):
            report.append(f"{i}. {model}: {s.get('avg_composite_score', 0)*100:.2f}% composite score")
        
        return "\n".join(report)
    
    def save_results(self, metrics: Optional[List[AggregatedMetrics]] = None):
        """Save aggregated results to files."""
        if metrics is None:
            metrics = self.aggregate()
        
        # Save detailed metrics as JSON
        json_file = self.results_dir / "aggregated_metrics.json"
        with open(json_file, 'w') as f:
            json.dump([asdict(m) for m in metrics], f, indent=2)
        
        # Save as CSV
        csv_file = self.results_dir / "metrics.csv"
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            headers = [
                "model", "subject", "syntax_valid", "runnable",
                "tests_run", "tests_passed", "test_pass_rate",
                "statement_coverage", "branch_coverage",
                "mutation_score", "mutants_killed", "mutants_total",
                "composite_score"
            ]
            writer.writerow(headers)
            
            for m in metrics:
                writer.writerow([
                    m.model, m.subject, m.syntax_valid, m.runnable,
                    m.tests_run, m.tests_passed, f"{m.test_pass_rate:.4f}",
                    f"{m.statement_coverage:.4f}", f"{m.branch_coverage:.4f}",
                    f"{m.mutation_score:.4f}", m.mutants_killed, m.mutants_total,
                    f"{m.composite_score:.4f}"
                ])
        
        # Save summary
        summary = self.summarize_by_model(metrics)
        summary_file = self.results_dir / "model_summary.json"
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)
        
        # Save text report
        report = self.generate_report()
        report_file = self.results_dir / "benchmark_report.txt"
        with open(report_file, 'w') as f:
            f.write(report)
        
        print(f"Results saved to:")
        print(f"  - {json_file}")
        print(f"  - {csv_file}")
        print(f"  - {summary_file}")
        print(f"  - {report_file}")
        
        return metrics


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Aggregate benchmark results")
    parser.add_argument("--results-dir", default="results", help="Results directory")
    parser.add_argument("--print-report", action="store_true", help="Print report to stdout")
    
    args = parser.parse_args()
    
    aggregator = ResultAggregator(results_dir=args.results_dir)
    metrics = aggregator.save_results()
    
    if args.print_report:
        print(aggregator.generate_report())
    else:
        summary = aggregator.summarize_by_model(metrics)
        print(f"\n{'='*60}")
        print("Benchmark Summary")
        print(f"{'='*60}")
        
        for model, s in sorted(summary.items()):
            print(f"\n{model}:")
            print(f"  Runnable: {s.get('runnable_rate', 0):.1%}")
            print(f"  Statement Coverage: {s.get('avg_statement_coverage', 0):.1%}")
            print(f"  Mutation Score: {s.get('avg_mutation_score', 0):.1%}")
            print(f"  Composite Score: {s.get('avg_composite_score', 0):.1%}")


if __name__ == "__main__":
    main()
