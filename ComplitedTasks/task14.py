import json


def mean_age(json_string):
    json_li = json.loads(json_string)
    age_list = [i.get("age") for i in json_li]
    return json.dumps({"mean_age": sum(age_list)/len(age_list)})


def main():
    data = '[{"name": "Петр","surname": "Петров","patronymic": "Васильевич","age": 23,"occupation": "ойтишнек"},{"name": "Василий","surname": "Васильев","patronymic": "Петрович","age": 24,"occupation": "дворник"}]'
    print(mean_age(data))


if __name__ == "__main__":
    main()