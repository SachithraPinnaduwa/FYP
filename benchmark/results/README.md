# Benchmark Results

This directory contains the output of the benchmark evaluation.

## Files

- `test_results.json` / `test_results.csv` - Test execution results
- `coverage_results.json` / `coverage_results.csv` - Code coverage metrics
- `mutation_results.json` / `mutation_results.csv` - Mutation testing scores
- `metrics.csv` - Aggregated metrics for all models and subjects
- `model_summary.json` - Summary statistics by model
- `benchmark_report.txt` - Human-readable benchmark report

## Metrics

### Test Execution
- **syntax_valid**: Whether the generated test has valid Python syntax
- **runnable**: Whether the test can be executed without import/runtime errors
- **tests_run/passed/failed**: Number of test cases and their outcomes

### Code Coverage
- **statement_coverage**: Percentage of statements executed
- **branch_coverage**: Percentage of branches taken

### Mutation Testing
- **mutation_score**: Percentage of mutants killed
- **mutants_killed/total**: Raw counts of mutation testing

### Composite Score
Weighted combination: 10% runnability + 40% coverage + 50% mutation score
