from util import *


def task13() -> None:
    li_tel = ["+79160000000", 
          "9160000000",
          "8(916)000-00-00",
          "+7(916)000-00-00", 
          "(916)000-00-00",
          "8 (916) 000-00-00",
          "+7 (916) 000-00-00",
          "(916) 000-00-00", 
          "8(916)0000000",
          "+7(916)0000000",
          "(916)0000000",
          "8-916-000-00-00",
          "+7-916-000-00-00",
          "916-000-00-00"]
    li_mail_true = ["abc@abc.ab",
                    "abc@abc.ab.ab",
                    "a@ab.ab",
                    "abc.abc@abc.abc"]
    li_mail_false = ["@abc.abc",
                     "abc@abc",
                     "abc@abc.a",
                     "abc@abc.abc.a",
                     "abc@abc.",
                     "abc@abc@abc"]
    for i in li_tel + li_mail_true + li_mail_false:
        print(f"{i}:\t{check_string(i)}")

def task14() -> None:
    print(get_popular_name_from_file("EXAMPLE_TEXT_TASK14.txt"))

def task15() -> None:
    data = '[{"name": "Петр","surname": "Петров","patronymic": "Васильевич","age": 23,"occupation": "ойтишнек"},{"name": "Василий","surname": "Васильев","patronymic": "Петрович","age": 24,"occupation": "дворник"}]'
    print(mean_age(data))

def main():
    task15()

if __name__ == "__main__":
    main()