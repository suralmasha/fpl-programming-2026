"""L - Liskov Substitution Principle (Принцип подстановки Барбары Лисков)"""

from abc import ABC, abstractmethod


class MessageSender(ABC):
    """Отправляет сообщение указанному получателю."""

    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        """
        Отправляет сообщение.

        :param recipient: Адрес получателя для выбранного канала.
        :param message: Текст сообщения.
        """


class EmailSender(MessageSender):
    def send(self, recipient: str, message: str) -> None:
        print(f'Email to {recipient}: {message}')


class SmsSender(MessageSender):
    def send(self, recipient: str, message: str) -> None:
        print(f'SMS to {recipient}: {message}')

# Если наследник запрещает отправку, он нарушает контракт MessageSender - нарушение LIP
# class DisabledSender(MessageSender):
#     def send(self, recipient: str, message: str) -> None:
#         raise NotImplementedError


def notify(sender: MessageSender, recipient: str, message: str) -> None:
    sender.send(recipient, message)


# Любую реализацию MessageSender можно подставить в notify
# Функция не проверяет конкретный тип отправителя
notify(EmailSender(), 'user@example.com', 'Заказ отправлен')
notify(SmsSender(), '+79991234567', 'Заказ отправлен')