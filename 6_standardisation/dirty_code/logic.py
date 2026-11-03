# Форматтер исправит оформление, но не определит значение неизвестной переменной.
def calculate_total(prices):
    total=sum(prices)
    return total+delivery_cost


if __name__ == "__main__":
    print(calculate_total([100, 200, 300]))
