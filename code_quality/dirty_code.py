def f(d: list[str], flag: bool) -> dict[str, int]:
    # Подсчитать частоты слов с выбранным учетом регистра
    r: dict[str, int] = {}
    if flag:
        for x in d:
            for y in x.split():
                y = y.strip('.,!?;:').lower()
                if y != '':
                    if y in r:
                        r[y] = r[y] + 1
                    else:
                        r[y] = 1
    if not flag:
        for x in d:
            for y in x.split():
                y = y.strip('.,!?;:')
                if y != '':
                    if y in r:
                        r[y] = r[y] + 1
                    else:
                        r[y] = 1
    else:
        pass

    print(f"{len(r)}")
    return r


if __name__ == '__main__':
    lines = ['Кот, кот! Пес.', 'кот и пес']

    # Проверки
    original_lines = lines.copy()
    assert f(lines, True) == {'кот': 3, 'пес': 2, 'и': 1}
    assert f(lines, False) == {'Кот': 1, 'кот': 2, 'Пес': 1, 'и': 1, 'пес': 1}
    assert f([], True) == {}
    assert f(['   ', '... !!!'], False) == {}
    assert lines == original_lines
