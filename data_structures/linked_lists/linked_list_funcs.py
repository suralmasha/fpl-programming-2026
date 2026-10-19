from __future__ import annotations  # Позволяет написать внутри Node ссылку на сам класс
from typing import Any

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Node:
    """Узел односвязного списка."""

    data: Any
    next: Node | None = None


def append(head: Node | None, value: int) -> Node:
    """
    Добавить элемент в конец списка.

    :param head: Первый узел или None для пустого списка.
    :param value: Добавляемое значение.
    :return: Первый узел обновленного списка.
    """
    new_node = Node(value)

    if head is None:
        return new_node

    current = head
    while current.next is not None:
        current = current.next

    current.next = new_node
    return head


def iter_values(head: Node | None) -> Iterator[int]:
    """
    Перебрать значения списка.

    :param head: Первый узел списка.
    :yield: Значения узлов по порядку.
    """
    current = head
    while current is not None:
        yield current.data
        current = current.next


if __name__ == '__main__':
    linked_list = append(None, 10)
    linked_list = append(linked_list, 20)
    linked_list = append(linked_list, 30)

    print(f"{linked_list = }")

    for value in iter_values(linked_list):
        print(f"{value = }")
