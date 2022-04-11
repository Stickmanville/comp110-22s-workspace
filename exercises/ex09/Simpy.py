"""Ex09. Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730332997"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]) -> None:
        self.values = values

    def __str__(self) -> str:
        return f"Simpy({self.values})"
         