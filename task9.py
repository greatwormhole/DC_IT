import datetime

def gift_count(budget, month, birthdays):
    res = sorted([f"{i} ({j.strftime('%d.%m.%Y')})"
                for i, j in filter(lambda x: x[-1].month == month, birthdays.items())],
                key=lambda x: x[-1])
    if len(res) != 0:
        print(f"Именинники в месяце {month}: {', '.join(res)}"
              f". При бюджете {budget} они получат по {budget // len(res)} рублей.")
    else:
        print("В этом месяце нет именниннков.")

if __name__ == "__main__":
    birthdays = {"Иванов Иван Иванович": datetime.date(1989, 5, 1), "Петров Петр Петрович": datetime.date(1998, 5, 6)}
    gift_count(20000, 5, birthdays)
    #gift_count(budget=20000, month=5, birthdays=birthdays)