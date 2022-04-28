"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730332997"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    elif head is not None:
        return last(head.next)
    else:
        return head.data


def value_at(head: Optional[Node], index: int) -> int:
    """Returns the data of the Node stored at the given index."""
    if index < 0 or head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index != 0 and head.next is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.data
    else:
        return value_at(head.next, index - 1)
        

def max(head: Optional[Node]) -> int:
    """Returns the maximum data value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    elif head.next is None:
        return head.data
    elif head.data < max(head.next):
        return max(head.next)
    else:
        return head.data


def linkify(items: list[int]) -> Optional[Node]:
    """Returns a linked list with the same values and in the same order as the input list."""
    if len(items) > 1:
        return Node(items[0], linkify(items[1:]))
    elif len(items) == 0:
        return None
    else:
        return Node(items[0], None)


def scale(head: Optional[Node], scaling_factor: int) -> Optional[Node]:
    """Returns a new linked list of Nodes where each value in the original list is multiplied by the scaling factor."""
    if head is None:
        return None
    elif head.next is None:
        return Node((head.data * scaling_factor), None)
    else:
        return Node((head.data * scaling_factor), scale(head.next, scaling_factor))
