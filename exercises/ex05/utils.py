"""EX05 - Utils."""

__author__ = "730332997"


def only_evens(numbers: list[int]) -> list[int]:
    """Given a list of numbers, returns a list of only even numbers."""
    evens: list[int] = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens


def sub(numbers: list[int], start: int, end: int) -> list[int]:
    """Given a list, spits out a subset of the list."""
    new_list: list[int] = []
    i: int = start
    if i < 0:
        i = 0
    if end > len(numbers):
        true_end = len(numbers) - 1
    else:
        true_end: int = end - 1
    while i <= true_end:
        number: int = numbers[i]
        new_list.append(number)
        i += 1
    return new_list


def concat(input_1: list[int], input_2: list[int]) -> list[int]:
    