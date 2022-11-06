def get_popular_name_from_file(filename):
    d = {}
    f = open(filename, mode="r", encoding="UTF-8")
    for line in f.readlines():
        key = line.split()[0]
        d[key] = d.get(key, 0) + 1
    value = max(d.values())
    res = []
    sorted_tuples = sorted(d.items(), key=lambda x: x[0])
    for tuple in sorted_tuples:
        if tuple[1] == value:
            res.append(tuple[0])
    return ", ".join(res)


if __name__ == "__main__":
    get_popular_name_from_file("EXAMPLE_TASK13.txt")