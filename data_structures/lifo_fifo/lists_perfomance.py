from contextlib import contextmanager
import time

@contextmanager
def measure_performance(n: int, func_name: str):
    """
    Измерить время выполнения блока кода.

    :param n: Количество обрабатываемых элементов.
    :param func_name: Название измеряемой операции.
    """
    start_time_append = time.perf_counter()  # Используем perf_counter для более точных замеров
    yield
    end_time_append = time.perf_counter()
    print(f'Время `{func_name}` {n} элементов: {end_time_append - start_time_append:.6f} сек')


if __name__ == '__main__':
    n = 20000  # Достаточно большой размер для наглядности
    print(f'Сравнение производительности для {n} элементов:')
    print()

    # --- Замеряем append - O(1) ---
    big_list_append = []
    with measure_performance(n, 'append()'):
        for i in range(n):
            big_list_append.append(i)

    # --- Замеряем insert(0, ...) - O(n) ---
    big_list_insert = []
    with measure_performance(n, 'insert(0, ...)'):
        for i in range(n):
            big_list_insert.insert(0, i)  # Вставляем в начало

    # =============================================
    # insert(0,...) намного медленнее на больших n
    # =============================================
    print()

    # --- Замеряем pop() - O(1) ---
    big_list = [i for i in range(n)]
    with measure_performance(n, 'pop()'):
        for i in range(n):
            big_list.pop()  # Удаляем последний элемент

    # --- Замеряем pop(0) - O(n) ---
    big_list = [i for i in range(n)]
    with measure_performance(n, 'pop(0)'):
        for i in range(n):
            big_list.pop(0)  # Удаляем первый элемент

    # ============================================
    # pop(0) намного медленнее на больших n
    # ============================================
