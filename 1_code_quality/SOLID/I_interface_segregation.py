"""I - Interface Segregation Principle (Принцип разделения интерфейсов)"""

from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self, doc):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass

class SimplePrinter(Printer):
    def print(self, doc: str) -> None:
        print('Printing document')


class MultiFunctionDevice(Printer, Scanner):
    def print(self, doc: str) -> None:
        print("Printing document")

    def scan(self) -> None:
        print("Scanning document")


def print_document(printer: Printer, doc: str) -> None:
    """
    Печатает документ через интерфейс принтера.

    :param printer: Устройство с поддержкой печати.
    :param doc: Текст документа.
    """
    printer.print(doc)


# Клиент печати зависит только от Printer, интерфейс Scanner ему не нужен
# Обычный принтер не обязан реализовывать метод scan
printer = SimplePrinter()
device = MultiFunctionDevice()

# Так клиенты реализуют только то, что им нужно
print_document(printer, 'MyDoc')
print_document(device, 'MyDoc')
device.scan()
