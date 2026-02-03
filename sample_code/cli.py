"""Command-line entry for sample_code package."""
import argparse
import json
from .realistic_service import summarize_csv


def main(argv=None):
    parser = argparse.ArgumentParser(description="Summarize a CSV file")
    parser.add_argument("path", help="Path to CSV file")
    parser.add_argument("key", help="Key column name")
    parser.add_argument("value_field", help="Numeric value field name")
    args = parser.parse_args(argv)

    summary = summarize_csv(args.path, key=args.key, value_field=args.value_field)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
