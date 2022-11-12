from sys import stdin


def input_compare() -> str:
    s = input()
    if s == "привет" or s == "здравствуйте":
        return str("привет")

def even_sum() -> int:
    return sum([int(i) for i in filter(lambda x: x != '', map(str.strip, stdin)) if int(i) % 2 == 0])

def symbol_replacement() -> list:
    return list(filter(lambda x: (x != ''), input().split(sep=' ')))

def search_template() -> list:
    list = input().split(sep=' ')
    template = input().lower()
    res = []
    for word in list:
        if word.lower().find(template) != -1:
            res.append(word)
    return res