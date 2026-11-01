"""S - Single Responsibility Principle (Принцип единственной ответственности)"""

class SalaryCalculator:
    """Рассчитывает зарплату по отработанным часам."""

    @staticmethod
    def calculate(hours: int, hourly_rate: int) -> int:
        return hours * hourly_rate


class SalaryRepository:
    """Сохраняет рассчитанную зарплату."""

    def __init__(self) -> None:
        """Создает хранилище зарплат в памяти."""
        self.salaries: dict[str, int] = {}

    def save(self, employee_id: str, salary: int) -> None:
        self.salaries[employee_id] = salary


# Правила расчета и способ хранения меняются по разным причинам.
# Добавление премий затронет SalaryCalculator.
# Переход на базу данных затронет SalaryRepository.
salary = SalaryCalculator.calculate(hours=160, hourly_rate=500)

repository = SalaryRepository()
repository.save(employee_id='employee-1', salary=salary)
