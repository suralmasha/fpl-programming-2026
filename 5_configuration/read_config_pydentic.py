from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):  # для проверки типов и преобразования значений из окружения
    db_host: str = 'localhost'
    db_port: int = 5432
    api_key: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


"""
Плюсы:
- Автоматическая валидация типов
- Работает с .env и переменными окружения
- Удобно для API и больших проектов
- Подходит для Dev/Test/Prod окружений
"""


if __name__ == '__main__':
    settings = Settings()
    print(settings.db_host, settings.db_port)  # Секрет api_key не выводим
