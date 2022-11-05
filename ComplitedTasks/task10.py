def lists_sum(*args, unique=False):
    if unique == False:
        return sum([sum(i) for i in args])
    else:
        return sum({i for j in args for i in j})


if __name__ == "__main__":
    print(lists_sum([1, 1], [1], [1, 2, 3]))
    print(lists_sum([1, 1, 1], [1, 1], unique=True))
    print(lists_sum([1, 1, 1], unique=False))