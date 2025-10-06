"""Command-line interface for basic arithmetic operations."""

from __future__ import annotations

import argparse
from typing import List

from app.operations import OPERATIONS


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Perform basic arithmetic on two numbers.",
    )
    parser.add_argument("operator", choices=OPERATIONS.keys(), help="Operator to apply.")
    parser.add_argument("left", type=float, help="Left operand.")
    parser.add_argument("right", type=float, help="Right operand.")
    return parser


def format_result(operator: str, left: float, right: float, result: float) -> str:
    return f"{left} {operator} {right} = {result}"


def main(argv: List[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    operation = OPERATIONS[args.operator]
    result = operation(args.left, args.right)
    print(format_result(args.operator, args.left, args.right, result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
