from sys import stdin
from datetime import datetime as dt


def sorted_list() -> list:
    return sorted([int(i) for i in filter(lambda x: x != '', map(str.strip, stdin))], reverse=True)

def list_from_set() -> list:
    return sorted(set(input().lower().split(sep=", ")))

def sorted_dict() -> list:
    s = input().split(sep=", ")
    d = {}
    for word in s:
        d[word] = d.get(word, 0) + 1
    return sorted(d.items(), key=lambda x: x[-1], reverse=True)

def start_of_week() -> str:
    s = dt.strptime(input(), "%d-%m-%Y")
    return "{}-{:02}-{}".format(s.day - s.weekday(), s.month, s.year)