from __future__ import annotations

from typing import Optional

class Node:
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        self.data = data
        self.next = next

    def __str__(self) --> str:
        if self.next == None:
            return


def sum(node: Optional[Node]) -> int:
    if node == None:
        return 0
    else:
        return node.data + sum(node.next)


def count(node: Node, current_count: int = 0) -> int:
    if node.next == None:
        return current_count + 1
    else:
        return count(node.next, current_count + 1)


head: Node = Node(3, None)
head: Node = Node(2, head)
head: Node = Node(1, head)
print(sum(head))
print(count(head))