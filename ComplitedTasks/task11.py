def get_balance(name, transactions):
    return sum([i.get("amount") for i in transactions if i.get("name") == name])


def count_debts(names, amount, transactions):
    dict = {}
    for i in names:
        dict.update({i: max(amount - get_balance(i, transactions), 0)})
    return dict


if __name__ == "__main__":
    transactions = [ {"name": "Василий", "amount": 500}, {"name": "Петя", "amount": 100}, {"name": "Василий", "amount": -300}, ]
    print(get_balance("Василий", transactions))
    print(count_debts(["Василий", "Петя", "Вова"], 150, transactions))