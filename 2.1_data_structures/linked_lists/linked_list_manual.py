from __future__ import annotations  # Позволяет написать внутри Node ссылку на сам класс
from typing import Any

from dataclasses import dataclass


@dataclass
class Node:
    """Узел односвязного списка."""

    data: Any
    next: Node | None = None


if __name__ == '__main__':
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")

    # Связываем: A -> B -> C -> None
    node1.next = node2
    node2.next = node3

    print(f'{node1 = }')
    print(f'{node2 = }')
    print(f'{node3 = }')
