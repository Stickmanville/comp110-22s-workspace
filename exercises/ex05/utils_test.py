"""Tests utils."""

from exercises.ex05.utils import only_evens, sub


def test_only_evens_all_evens() -> None:
    "Use case test given a list of all evens."
    xs: list[int] = [2, 4, 6, 8, 10]
    assert only_evens(xs) == [2, 4, 6, 8, 10]


def test_only_evens_some_evens() -> None:
    """Use case test given a list with some evens."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(xs) == [2, 4]


def test_only_evens_no_numbers() -> None:
    """Edge case test given an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_sub_some_numbers() -> None:
    """Use case test."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 1, 3) == [20, 30]


def test_sub_empty_list() -> None:
    """Edge case with empty list."""
    xs: list[int] = []
    assert sub(xs, 0, 3) == []


def test_sub_negative_index() -> None:
    """Edge case with negative index."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, -1, 3) == [10, 20, 30]


def test_concat() -> None:
    """"""