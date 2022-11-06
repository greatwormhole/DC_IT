import re as r


def check_string(string):
    pattern = r.compile(r"(\+{0,1}[78]{0,1}[- ]{0,1}[\( ]{0,1}\d{3}[\) ]{0,1}[- ]{0,1}\d{3}-*\d{2}-*\d{2})"
                        r"|((\w\.{0,1})+@(\w\.{0,1}))")
    return bool(pattern.fullmatch(string))


if __name__ == "__main__":
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