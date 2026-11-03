import os

from dotenv import load_dotenv

load_dotenv()  # загружает .env, не заменяя уже заданные переменные окружения

"""
os.environ - отображение в Python, которое содержит переменные окружения
операционной системы для текущего процесса.
"""

DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
DB_PORT = int(os.environ.get('DB_PORT', 5432))

"""
Плюсы:
- Секреты не в коде
- Настройки хранятся в .env

Минусы:
- Нет строгой типизации
- Валидацию значений нужно писать вручную (int проверяет только преобразование)
"""

def double(value: int) -> int:
    """Удваивает число.

    Parameters
    ----------
    value : int
        Исходное число.

    Returns
    -------
    int
        Удвоенное число.
    """
    return value * 2



