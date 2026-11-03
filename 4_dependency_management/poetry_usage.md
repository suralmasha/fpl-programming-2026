# Управление зависимостями с Poetry

Нужны Python и [Poetry 2.x](https://python-poetry.org/docs/#installation).
Общие команды одинаковы для macOS (zsh/bash) и Windows (PowerShell).

## Создание проекта

```shell
mkdir myproject
cd myproject

poetry init
```

`poetry init` задает вопросы о проекте и создает `pyproject.toml`.
Само окружение и зависимости эта команда не устанавливает.

Если проект нужен только для управления зависимостями, без сборки пакета,
добавьте в `pyproject.toml` (в существующую секцию, если она уже есть):

```toml
[tool.poetry]
package-mode = false
```

## Установка зависимостей

Зависимости приложения (например, для requests и fastapi):

```shell
poetry add requests fastapi
```

Инструменты для разработки и тестирования (pytest, mypy, ruff):

```shell
poetry add --group dev pytest mypy ruff
```

Команды устанавливают пакеты в виртуальное окружение, обновляют
`pyproject.toml` и `poetry.lock`. Lock-файл фиксирует выбранные версии;
его следует хранить в Git вместе с `pyproject.toml`.

В существующем проекте установите зависимости из lock-файла:

```shell
poetry install
```

Если lock-файла нет, Poetry разрешит зависимости и создаст его.
В режиме пакета `install` также устанавливает сам проект, поэтому его
исходники должны соответствовать конфигурации.

## Запуск команд

Активация окружения не обязательна: `poetry run` запускает команду внутри него
на обеих системах.

```shell
poetry run python --version
poetry run pytest
poetry run mypy src/
poetry run ruff check src/
```

Для pytest нужны тесты, для команд mypy и Ruff - каталог `src/`.
Для flat-layout замените `src/` на каталог своего пакета.

## Активация окружения (необязательно)

После установки зависимостей можно активировать окружение и запускать
команды без `poetry run`.

macOS (zsh/bash):

```sh
eval "$(poetry env activate)"
```

Windows (PowerShell):

```powershell
Invoke-Expression (poetry env activate)
```

Если PowerShell блокирует скрипт активации, используйте `poetry run`.
Выход из активированного окружения: `deactivate`.
В Poetry 2.x команда `poetry shell` требует отдельного плагина и здесь не нужна.

Источники: [команды Poetry](https://python-poetry.org/docs/cli/),
[виртуальные окружения](https://python-poetry.org/docs/managing-environments/).
