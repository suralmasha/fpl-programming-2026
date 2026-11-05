# Сборка и публикация пакета с setuptools

setuptools - backend сборки, `build` запускает сборку, а Twine проверяет
метаданные и загружает дистрибутивы. Пример использует `src`-layout.

## Подготовка

Создайте отдельный проект со структурой:

```text
mypackage/
    pyproject.toml
    setup.py
    src/
        mypackage/
            __init__.py
```

Скопируйте `setup_ex_packaging_setuptools.py` из этой папки как `setup.py`.
В `pyproject.toml` укажите backend:

```toml
[build-system]
requires = ['setuptools>=77']
build-backend = 'setuptools.build_meta'
```

Не копируйте сюда Poetry- или uv-backend: в этом примере метаданные
задаются в `setup.py`, а backend - setuptools. Сам файл `setup.py` допустим,
но команды вида `python setup.py sdist` устарели.

## Окружение

Нужен установленный Python 3.10+. Все команды выполняйте из корня своего пакета.

macOS (zsh/bash):

```sh
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Если команды `py` нет, используйте установленный `python`.
Если PowerShell запрещает активацию, вместо `python` в дальнейших командах
используйте `.\.venv\Scripts\python.exe` - активация не обязательна.

В выбранном окружении установите инструменты:

```shell
python -m pip install --upgrade build twine
```

## Сборка и локальная проверка

```shell
python -m build
python -m twine check dist/*
```

В `dist/` появятся `mypackage-0.1.0-py3-none-any.whl` и
`mypackage-0.1.0.tar.gz`. Имена определяются метаданными в `setup.py`.
Wheel устанавливается без сборки; исходный архив требует сборки и иногда
компилятора. Совместимость зависит от Python, платформы и зависимостей пакета.

`twine check` проверяет метаданные и отображение описания локально.
Эта команда ничего не загружает на TestPyPI и не проверяет работоспособность кода.

Установите собранный wheel и проверьте импорт:

```shell
python -m pip install dist/mypackage-0.1.0-py3-none-any.whl
python -c "import mypackage; print(mypackage.__file__)"
```

При повторной установке измененного wheel той же версии добавьте
`--force-reinstall`. Для разработки вместо wheel можно использовать
`python -m pip install -e .`: изменения исходников будут доступны без пересборки.

## Публикация

Для учебной публикации используйте [TestPyPI](https://test.pypi.org/).
Нужны отдельная учетная запись и API-токен этого сервиса.
Замените имя `mypackage` в `setup.py` на уникальное имя своего проекта,
пересоберите пакет и оставьте в `dist/` только нужные дистрибутивы.
Имя импортируемого модуля `mypackage` при этом может остаться прежним.

```shell
python -m twine upload --repository testpypi --username __token__ dist/*
```

В запрос пароля вставьте API-токен TestPyPI. Для настоящей публикации нужны
учетная запись и токен [PyPI](https://pypi.org/):

```shell
python -m twine upload --username __token__ dist/*
```

Эти команды работают на macOS и в PowerShell; Twine умеет раскрывать `dist/*`.
Публикация делает файлы доступными другим пользователям;
повторно загрузить тот же файл нельзя.

Проверяйте установку в отдельном окружении, чтобы локальная копия не скрыла ошибки.
Для установки учебного пакета с TestPyPI:

```shell
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps your-unique-package-name
```

Замените имя на свое. `--no-deps` отключает поиск зависимостей на TestPyPI:
нужные библиотеки установите отдельно из обычного PyPI. При публикации на
основном PyPI пакет устанавливается обычной командой `python -m pip install your-unique-package-name`.

Источники: [сборка с setuptools](https://setuptools.pypa.io/en/stable/userguide/quickstart.html),
[статус setup.py](https://packaging.python.org/en/latest/discussions/setup-py-deprecated/),
[TestPyPI](https://packaging.python.org/en/latest/guides/using-testpypi/).
