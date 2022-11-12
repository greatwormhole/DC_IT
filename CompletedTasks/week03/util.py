def gift_count(budget: int, month: int, birthdays: dict) -> str:
    res = sorted([f"{i} ({j.strftime('%d.%m.%Y')})"
                for i, j in filter(lambda x: x[-1].month == month, birthdays.items())],
                key=lambda x: x[-11:-9])
    if len(res) != 0:
        return str(f"Именинники в месяце {month}: {', '.join(res)}"
              f". При бюджете {budget} они получат по {budget // len(res)} рублей.")
    else:
        return str("В этом месяце нет именинников.")

def lists_sum(*args: list, unique: bool = False) -> (int | float):
    if unique == False:
        return sum([sum(i) for i in args])
    else:
        return sum({i for j in args for i in j})

def get_balance(name: str, transactions: list) -> (int | float):
    return sum([i.get("amount") for i in transactions if i.get("name") == name])


def count_debts(names: list, amount: (int | float), transactions: list) -> dict:
    dict = {}
    for i in names:
        dict.update({i: max(amount - get_balance(i, transactions), 0)})
    return dict