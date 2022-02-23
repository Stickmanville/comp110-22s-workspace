"""Tests the functions of utils."""

from utils import only_evens, sub, concat


def test_only_evens_all_evens() -> None:
    """Use case test given a list of all evens."""
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
    """Use case test given two lists."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 1, 3) == [20, 30]


def test_sub_negative_index() -> None:
    """Use case test with a negative start index."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, -1, 3) == [10, 20, 30]


def test_sub_empty_list() -> None:
    """Edge case test with an empty list."""
    xs: list[int] = []
    assert sub(xs, 0, 3) == []


def test_concat_two_full_lists() -> None:
    """Use case test adding two lists."""
    list_a: list[int] = [10, 20]
    list_b: list[int] = [30, 40]
    assert concat(list_a, list_b) == [10, 20, 30, 40]


def test_concat_one_empty_list() -> None:
    """Use case test adding an empty list to a list."""
    list_a: list[int] = [10, 20]
    list_b: list[int] = []
    assert concat(list_a, list_b) == [10, 20]


def test_concat_two_empty_lists() -> None:
    """Edge case test adding two empty lists together."""
    list_a: list[int] = []
    list_b: list[int] = []
    assert concat(list_a, list_b) == []