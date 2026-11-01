"""D - Dependency Inversion Principle (Принцип инверсии зависимостей)"""

from abc import ABC, abstractmethod


# Абстракция для платежных систем
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Низкоуровневая реализация 1
class StripeGateway(PaymentGateway):
    def pay(self, amount):
        print(f'Paying {amount} via Stripe')


# Низкоуровневая реализация 2
class PayPalGateway(PaymentGateway):
    def pay(self, amount):
        print(f'Paying {amount} via PayPal')


# Жесткая зависимость - нарушение DIP
# class PaymentProcessor:
#     def __init__(self):
#         self.gateway = StripeGateway()
#     def pay(self, amount):
#         self.gateway.pay(amount)


# Высокоуровневый модуль зависит только от абстракции PaymentGateway
class PaymentProcessor:
    def __init__(self, gateway: PaymentGateway) -> None:
        self.gateway = gateway

    def pay(self, amount: int, *, order_confirmed: bool) -> None:
        """
        Оплачивает подтвержденный заказ.

        :param amount: Сумма оплаты.
        :param order_confirmed: Подтвержден ли заказ (бизнес-логика).
        """
        if not order_confirmed:
            raise ValueError('Order is not confirmed')
        self.gateway.pay(amount)


# Теперь можно легко менять реализацию
processor1 = PaymentProcessor(StripeGateway())
processor1.pay(100, order_confirmed=True)

processor2 = PaymentProcessor(PayPalGateway())
processor2.pay(200, order_confirmed=True)

processor2 = PaymentProcessor(PayPalGateway())
processor2.pay(200, order_confirmed=False)  # ValueError('Order is not confirmed')
