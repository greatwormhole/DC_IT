import re as r
import json


def check_string(string: str) -> bool:
    pattern = r.compile(r"((\+(?=7))?[78]?[- ]?[\( ]?\d{3}[\) ]?[- ]?\d{3}-?\d{2}-?\d{2})|"
                        r"(\w+(\.\w{2,})*@\w+(\.\w{2,})+)", flags=r.ASCII)
    return bool(pattern.fullmatch(string))

def get_popular_name_from_file(filename: str) -> str:
    d = {}
    f = open(filename, mode="r", encoding="UTF-8")
    for line in f:
        key = line.split()[0]
        d[key] = d.get(key, 0) + 1
    value = max(d.values())
    res = []
    sorted_tuples = sorted(d.items(), key=lambda x: x[0])
    for tuple in sorted_tuples:
        if tuple[1] == value:
            res.append(tuple[0])
    return ", ".join(res)

def mean_age(json_string: str) -> str:
    json_li = json.loads(json_string)
    age_list = [i.get("age") for i in json_li]
    return json.dumps({"mean_age": sum(age_list)/len(age_list)})