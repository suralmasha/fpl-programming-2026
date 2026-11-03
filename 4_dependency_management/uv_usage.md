# Управление зависимостями с uv

Нужен [uv](https://docs.astral.sh/uv/getting-started/installation/).
Общие команды одинаковы для macOS (zsh/bash) и Windows (PowerShell).
Если подходящего Python нет, uv может скачать его автоматически.
Назначение секций и расположение файла разобраны в [инструкции pyproject.toml](pyproject_usage.md).

## Создание проекта

```shell
uv init --no-package myproject
cd myproject
```

Команда создает проект с `pyproject.toml` без настройки сборки пакета.
Для библиотеки вместо `--no-package` используйте `--lib`:
uv создаст структуру с каталогом `src/` и настроит сборку.

## Установка зависимостей

Зависимости приложения:

```shell
uv add requests fastapi
```

Инструменты для разработки и тестирования:

```shell
uv add --dev pytest mypy ruff
```

Команды обновляют `pyproject.toml` и `uv.lock`, устанавливают зависимости
в `.venv` в каталоге проекта. Группа `dev` устанавливается по умолчанию.
Храните `pyproject.toml` и `uv.lock` в Git; `.venv` в Git не добавляйте.

В существующем проекте синхронизируйте окружение:

```shell
uv sync
```

Команда создаст `.venv`, если его нет, и установит зависимости.
При необходимости она создаст или обновит `uv.lock`.
Пакеты, не предусмотренные конфигурацией, удаляются из окружения.

## Запуск команд

`uv run` подготавливает окружение и запускает команду внутри него.
Активация не обязательна на обеих системах.

```shell
uv run python --version
uv run pytest
uv run mypy src/
uv run ruff check src/
```

Для pytest нужны тесты, для команд mypy и Ruff - каталог `src/`.
Для flat-layout замените `src/` на каталог своего пакета.

Для зависимостей из отдельной группы `test`:

```shell
uv sync --group test
uv run --group test pytest
```

Для готового проекта с lock-файлом `uv sync --locked` проверяет его актуальность
и завершится ошибкой вместо изменения устаревшего `uv.lock`. Это удобно в CI.

## Активация окружения (необязательно)

После установки зависимостей можно активировать `.venv` и запускать
команды без `uv run`.

macOS (zsh/bash):

```sh
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Если PowerShell блокирует скрипт активации, используйте `uv run`.
Выход из активированного окружения: `deactivate`.

Источники: [работа с проектами](https://docs.astral.sh/uv/guides/projects/),
[синхронизация окружения](https://docs.astral.sh/uv/concepts/projects/sync/).
