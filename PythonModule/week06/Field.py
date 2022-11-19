import re

class Field:
    _str_pattern = re.compile(r"(^\d+\w)|(^\w\d+)", flags=re.ASCII)
         