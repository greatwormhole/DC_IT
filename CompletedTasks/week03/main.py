import datetime
from util import *

def task10() -> None:
    birthdays = {"Иванов Иван Иванович": datetime.date(1989, 5, 1), "Петров Петр Петрович": datetime.date(1998, 5, 6)}
    print(gift_count(20000, 5, birthdays))
    print(gift_count(budget=20000, month=5, birthdays=birthdays))

def task11() -> None:
    print(lists_sum([1, 1], [1], [1, 2, 3]))
    print(lists_sum([1, 1, 1], [1, 1], unique=True))
    print(lists_sum([1, 1, 1], unique=False))

def task12() -> None:
    transactions = [ {"name": "Василий", "amount": 500}, {"name": "Петя", "amount": 100}, {"name": "Василий", "amount": -300}, ]
    print(get_balance("Василий", transactions))
    print(count_debts(["Василий", "Петя", "Вова"], 150, transactions))

def main():
    pass

if __name__ == "__main__":
    main()