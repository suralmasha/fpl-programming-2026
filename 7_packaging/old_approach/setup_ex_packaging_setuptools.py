"""Располагается в корне проекта (рядом с src/). Обычно называется setup.py"""

# Сохраните как setup.py рядом с src/; сборка: python -m build.
from setuptools import find_packages, setup

# Вызов функции setup описывает метаданные и настройки сборки пакета
setup(
    name='mypackage',  # Название пакета (должно быть уникальным на PyPI, если планируете публиковать)
    version='0.1.0',  # Текущая версия пакета
    description='Краткое описание пакета',
    long_description='Более подробное описание (можно спарсить README.md)',  # (необязательно)
    author='Name Surname',  # Автор пакета
    author_email='email@example.com',  # Контактный email автора
    url='https://github.com/username/mypackage',  # URL репозитория или страницы проекта
    package_dir={'': 'src'},  # Исходники пакетов находятся в src/
    packages=find_packages(where='src'),  # Находит пакеты с __init__.py внутри src/
    install_requires=[  # Зависимости пакета в формате спецификаторов, не произвольный requirements.txt
        'requests>=2.30.0',  # пример зависимости
    ],
    license='MIT',  # Лицензия пакета (необязательно)
    classifiers=[  # Классификаторы помогают другим понять, для чего пакет (необязательно)
        'Programming Language :: Python :: 3',  # поддержка Python 3
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',  # Поддерживаемая версия Python
)
