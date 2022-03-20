"""EX06 dictionary test. Tests the functions of dictionary."""

__author__ = "730332997"

from dictionary import invert, favorite_color, count

import pytest


def test_invert_simple() -> None:
    """Use case test given a simple dictionary."""
    xs: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_empty() -> None:
    """Use case test given an empty dictionary."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_invert_key_error() -> None:
    """Edge case test if duplicate key asserts KeyError."""
    with pytest.raises(KeyError):
        xs = {'kris': 'jordan', 'michael': 'jordan'}
        invert(xs)


def test_favorite_color_simple() -> None:
    """Use case test given a simple dictionary."""
    xs: dict[str, str] = {"A": "yellow", "B": "blue", "C": "blue"}
    assert favorite_color(xs) == "blue"


def test_favorite_color_empty() -> None:
    """Use case test given an empty dictionary."""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == ""


def test_favorite_color_repeated() -> None:
    """Edge case test given a dictionary with values which repeat an equal number of times."""
    xs: dict[str, str] = {"A": "blue", "B": "red", "C": "blue", "D": "red"}
    assert favorite_color(xs) == "blue"
    

def test_count_simple() -> None:
    """Use case test given a simple list."""
    xs: list[str] = ["blue", "red", "blue"]
    assert count(xs) == {"blue": 2, "red": 1}


def test_count_empty() -> None:
    """Use case test given an empty list."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_e() -> None:
    """Edge case test given a list with one value."""
    xs: list[str] = ["blue"]
    assert count(xs) == {"blue": 1}