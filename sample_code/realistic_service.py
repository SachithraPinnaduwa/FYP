"""Realistic service-style module for generating robust unit tests.

Contains a `CSVDataProcessor` that demonstrates:
- File I/O (should be mocked in tests)
- Stream processing with generators
- Data validation and custom exceptions
- Aggregation and grouping logic
- Dependency injection for external connectors
- Docstrings with examples
"""

from typing import Iterable, List, Dict, Callable, Any, Optional, Tuple
import csv
import os
from contextlib import contextmanager


class DataProcessingError(Exception):
    """Raised for errors during data processing."""


@contextmanager
def open_csv(path: str, mode: str = 'r', **kwargs):
    """Context manager wrapper around open() for CSV files.

    Keeps a single place to swap out file access during tests.
    """
    f = open(path, mode, newline='')
    try:
        yield f
    finally:
        f.close()


class CSVDataProcessor:
    """Process CSV rows with transformation, filtering and aggregation.

    Example usage:
        >>> proc = CSVDataProcessor(['id', 'value'])
        >>> rows = [ {'id':'1','value':'10'}, {'id':'2','value':'20'} ]
        >>> proc.aggregate_rows(rows, key='id', value_field='value')
        {'1': 10.0, '2': 20.0}
    """

    def __init__(self, headers: List[str]):
        self.headers = headers

    def read_rows(self, path: str) -> Iterable[Dict[str, str]]:
        """Yield rows from a CSV file as dicts.

        Raises DataProcessingError if the file cannot be read or headers mismatch.
        """
        if not os.path.exists(path):
            raise DataProcessingError(f"file not found: {path}")

        try:
            with open_csv(path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                # Validate header
                if not all(h in reader.fieldnames for h in self.headers):
                    raise DataProcessingError("CSV header mismatch")
                for row in reader:
                    yield row
        except DataProcessingError:
            raise
        except Exception as e:
            raise DataProcessingError(f"failed to read CSV: {e}") from e

    def transform(self, row: Dict[str, str], converters: Optional[Dict[str, Callable[[str], Any]]] = None) -> Dict[str, Any]:
        """Transform CSV row values using provided converter functions.

        If a converter raises, wrap in DataProcessingError.
        """
        converters = converters or {}
        out: Dict[str, Any] = {}
        for k, v in row.items():
            try:
                if k in converters:
                    out[k] = converters[k](v)
                else:
                    out[k] = v
            except Exception as e:
                raise DataProcessingError(f"conversion failed for {k}: {e}") from e
        return out

    def filter_rows(self, rows: Iterable[Dict[str, Any]], predicate: Callable[[Dict[str, Any]], bool]) -> Iterable[Dict[str, Any]]:
        """Yield rows where predicate(row) is True."""
        for r in rows:
            try:
                if predicate(r):
                    yield r
            except Exception as e:
                raise DataProcessingError(f"filter predicate failed: {e}") from e

    def aggregate_rows(self, rows: Iterable[Dict[str, Any]], key: str, value_field: str) -> Dict[str, float]:
        """Aggregate numeric `value_field` by `key` summing values.

        Non-numeric values raise DataProcessingError.
        """
        result: Dict[str, float] = {}
        for r in rows:
            if key not in r or value_field not in r:
                raise DataProcessingError("missing aggregation keys in row")
            k = r[key]
            try:
                val = float(r[value_field])
            except Exception as e:
                raise DataProcessingError(f"invalid numeric value: {r[value_field]}") from e
            result[k] = result.get(k, 0.0) + val
        return result

    def top_n(self, aggregated: Dict[str, float], n: int = 3) -> List[Tuple[str, float]]:
        """Return top-n items from aggregated results sorted by value desc."""
        if n <= 0:
            raise ValueError("n must be positive")
        return sorted(aggregated.items(), key=lambda kv: kv[1], reverse=True)[:n]


# Dependency-injectable connector function example
def default_db_connector(connection_string: str):
    """A placeholder DB connector factory.

    In real code this would return a DB connection. Here it's a stub to be
    replaced/mocked during testing.
    """
    raise NotImplementedError("DB connector not implemented")


def summarize_csv(path: str, key: str, value_field: str, converter: Optional[Callable[[str], Any]] = None, db_connector: Callable[[str], Any] = default_db_connector) -> Dict[str, Any]:
    """High-level helper that reads a CSV, aggregates and returns a summary.

    Accepts a `db_connector` to demonstrate dependency injection for side-effects
    (e.g., storing the summary), which tests can mock.
    """
    proc = CSVDataProcessor([key, value_field])
    raw_rows = proc.read_rows(path)
    # Apply conversion if given
    convs = {value_field: converter} if converter is not None else None
    transformed = (proc.transform(r, convs) for r in raw_rows)
    aggregated = proc.aggregate_rows(transformed, key=key, value_field=value_field)
    top = proc.top_n(aggregated, n=5)

    # Optionally store using provided connector (side-effect)
    # connector = db_connector("sqlite://:memory:")
    # connector.save_summary(aggregated)

    return {
        'aggregated': aggregated,
        'top': top,
        'count': sum(1 for _ in aggregated)
    }


if __name__ == '__main__':
    print('This module provides CSVDataProcessor for test generation examples')
