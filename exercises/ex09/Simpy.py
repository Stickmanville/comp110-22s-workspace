"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730332997"


class Simpy:
    """Exercise 09. Working with sequences of data."""

    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """Initializes the values attribute to the argument."""
        self.values = values

    def __str__(self) -> str:
        """Returns a string in the format of "Simpy()"."""
        return f"Simpy({self.values})"
         
    def fill(self, f: float, num: int) -> None:
        """Fills Simpy's values with a specific number of repeating values."""
        output = [f] * num
        self.values = output
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in the values attribute with a range of float values counting from the given start to stop."""
        assert step != 0.0
        output: list[float] = []
        number: float = start
        if start < stop:
            while number < stop:
                output.append(number)
                number += step
        else:
            while number > stop:
                output.append(number)
                number += step
        self.values = output

    def sum(self) -> float:
        """Computes and returns the sum of all items in the values attribute."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Produces a new object that is the sum of each item of the original objects at the same index. If the rhs is a float value, produces a new object that is the sum of each item of the same index on the left object and the float."""
        output: list[float] = []
        for item in range(len(self.values)):
            if isinstance(rhs, Simpy):
                assert len(self.values) == len(rhs.values)
                output.append(self.values[item] + rhs.values[item])
            else:
                output.append(self.values[item] + rhs)
        return Simpy(output)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Same thing as __add__ except exponential operation rather than addition."""
        output: list[float] = []
        for item in range(len(self.values)):
            if isinstance(rhs, Simpy):
                assert len(self.values) == len(rhs.values)
                output.append(self.values[item] ** rhs.values[item])
            else:
                output.append(self.values[item] ** rhs)
        return Simpy(output)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloads ==."""
        output: list[bool] = []
        for item in range(len(self.values)):
            if isinstance(rhs, Simpy):
                assert len(self.values) == len(rhs.values)
                if self.values[item] == rhs.values[item]:
                    output.append(True)
                else:
                    output.append(False)
            else:
                if self.values[item] == rhs:
                    output.append(True)
                else:
                    output.append(False)
        return output

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloads >."""
        output: list[bool] = []
        for item in range(len(self.values)):
            if isinstance(rhs, Simpy):
                assert len(self.values) == len(rhs.values)
                if self.values[item] > rhs.values[item]:
                    output.append(True)
                else:
                    output.append(False)
            else:
                if self.values[item] > rhs:
                    output.append(True)
                else:
                    output.append(False)
        return output

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Implements the subscription operator if rhs is integer, if its a list[bool], will return filtered values."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            output: list[float] = []
            for item in range(len(self.values)):
                if rhs[item] is True:
                    output.append(self.values[item])
            return Simpy(output)
