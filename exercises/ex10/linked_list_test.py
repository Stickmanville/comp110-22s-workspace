"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, is_equal, last, value_at, max, linkify, scale

__author__ = "730332997"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Edge case test if empty list raises an IndexError."""
    with pytest.raises(IndexError):
        value_at(None, 0)


def test_value_at_non_empty() -> None:
    """Use case test."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 1) == 2


def test_max_empty() -> None:
    """Edge case test if empty list raises a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_max_non_empty() -> None:
    """Use case test."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert max(linked_list) == 3

