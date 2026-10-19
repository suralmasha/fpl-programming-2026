class Node:
    """
    Представляет узел (звено) односвязного списка.
    Хранит данные и ссылку на следующий узел.
    """
    def __init__(self, data=None):
        self.data = data  # Данные, которые хранит узел
        self.next = None  # Ссылка на следующий узел, по умолчанию None

    def __repr__(self):
        """Возвращает строковое представление данных узла.
           Удобно при печати всего списка.
        """
        return str(self.data)

class LinkedList:
    """
    Представляет сам односвязный список.
    Хранит ссылку на голову (head) и предоставляет базовые операции.
    """
    def __init__(self, nodes_data=None):
        """
        Инициализирует связанный список.
        Может принимать итерируемый объект (например, list, tuple)
        для создания узлов списка при инициализации.
        """
        self.head = None # Изначально список пуст, головы нет

        if nodes_data is not None:
            # Пытаемся создать список из переданных данных
            try:
                # Получаем итератор, чтобы работать с любым итерируемым типом
                iterator = iter(nodes_data)
                # Создаем голову из первого элемента
                first_node_data = next(iterator)
                self.head = Node(first_node_data)
                current_node = self.head

                # Добавляем и связываем остальные элементы
                for elem_data in iterator:
                    current_node.next = Node(elem_data)
                    current_node = current_node.next # Переходим к только что созданному узлу
            except StopIteration:
                # Исходный итератор был пуст, self.head останется None
                pass
            except TypeError:
                # Переданный объект неитерируемый
                print("Ошибка: Для инициализации LinkedList нужны итерируемые данные.")
                self.head = None # Сбрасываем на всякий случай

    def __repr__(self):
        """
        Возвращает человекочитаемое строковое представление всего списка.
        Формат: data1 -> data2 -> ... -> None
        """
        nodes_repr = []
        current_node = self.head
        while current_node is not None:
            # Добавляем представление данных текущего узла (используя Node.__repr__)
            nodes_repr.append(str(current_node))
            current_node = current_node.next # Переходим к следующему узлу

        nodes_repr.append("None") # Явно показываем конец списка
        return " -> ".join(nodes_repr)

    def __iter__(self):
        """
        Позволяет итерироваться по данным узлов списка
        с помощью стандартного цикла for.
        """
        current = self.head  # Начинаем с головы
        while current is not None:
            yield current.data  # Возвращаем данные текущего узла
            current = current.next  # Переходим к следующему


if __name__ == "__main__":
    # 1. Создание пустого списка
    empty_llist = LinkedList()
    print(f"Пустой список: {empty_llist}")

    # 2. Создание узлов и ручное связывание
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")

    # Связываем их: A -> B -> C -> None
    node1.next = node2
    node2.next = node3

    # Создаем список и назначаем голову
    manual_llist = LinkedList()
    manual_llist.head = node1
    print(f"Список, связанный вручную: {manual_llist}")

    # 3. Создание списка из итерируемого объекта (списка Python)
    auto_llist = LinkedList(["Раз", "Два", "Три"])
    print(f"Список, созданный из list: {auto_llist}")

    # 4. Создание из другого итератора (например, range)
    range_llist = LinkedList(range(5))
    print(f"Список, созданный из range(5): {range_llist}")

    # 5. Пример с пустым итератором
    empty_init_llist = LinkedList([])
    print(f"Список, созданный из []: {empty_init_llist}")

    # 6. Обход связного списка
    my_playlist = LinkedList(["The Beatles", "Queen", "Led Zeppelin", "Pink Floyd"])
    print(f"Мой плейлист: {my_playlist}")

    print("\nВоспроизводим треки (итерация с помощью for):")
    for track in my_playlist:  # Теперь это работает благодаря __iter__!
        print(f"  🎶 Сейчас играет: {track}")