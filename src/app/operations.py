"""Core arithmetic operations."""

from __future__ import annotations

from typing import Callable, Dict


Operation = Callable[[float, float], float]


def add(left: float, right: float) -> float:
    return left + right


def subtract(left: float, right: float) -> float:
    return left - right


def multiply(left: float, right: float) -> float:
    return left * right


def divide(left: float, right: float) -> float:
    if right == 0:
        raise ZeroDivisionError("division by zero is undefined")
    return left / right


OPERATIONS: Dict[str, Operation] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
