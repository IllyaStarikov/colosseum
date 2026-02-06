#!/usr/bin/env python3
"""
Test runner for LeetCode solutions.

Usage:
    python run_tests.py                    # Run all tests
    python run_tests.py 1                  # Run tests for problem 1
    python run_tests.py two_sum            # Run tests matching pattern
    python run_tests.py -v                 # Verbose output
"""
import sys
import unittest
import argparse
import importlib.util
from pathlib import Path


def load_tests_from_file(file_path: Path) -> unittest.TestSuite:
    """Load test cases from a Python file."""
    spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    loader = unittest.TestLoader()
    return loader.loadTestsFromModule(module)


def main():
    parser = argparse.ArgumentParser(description='Run LeetCode solution tests')
    parser.add_argument('pattern', nargs='?', default='*', help='Problem number or name pattern')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    args = parser.parse_args()

    leetcode_dir = Path(__file__).parent / 'leetcode'

    # Build file pattern
    if args.pattern.isdigit():
        file_pattern = f'{args.pattern}_*.py'
    elif args.pattern == '*':
        file_pattern = '*.py'
    else:
        file_pattern = f'*{args.pattern}*.py'

    # Find matching files
    files = sorted(leetcode_dir.glob(file_pattern))
    files = [f for f in files if f.name != '__init__.py']

    if not files:
        print(f"No files matching pattern: {file_pattern}")
        sys.exit(1)

    # Load tests from each file
    suite = unittest.TestSuite()
    for file_path in files:
        try:
            suite.addTests(load_tests_from_file(file_path))
        except Exception as e:
            print(f"Error loading {file_path.name}: {e}")

    # Run tests
    verbosity = 2 if args.verbose else 1
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)


if __name__ == '__main__':
    main()
