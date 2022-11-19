import re

class Field:
    _str_pattern = re.compile(r"(^\d+\w)|(^\w\d+)", flags=re.ASCII)

    def __init__(self):
        self.dict = {}

    def __contains__(self, __other: object) -> bool:
        return self._key_check(__other) in self.dict

    def __setattr__(self, __name: str, __value) -> None:
        self.__dict__[__name.lower()] = __value
        try:
            self.dict[self._key_check(__name)] = __value
        except (ValueError, TypeError):
            pass

    def __getattribute__(self, __name):
        try:
            return super().__getattribute__(__name.lower())
        except AttributeError:
            return None

    def __delattr__(self, __name) -> None:
        try:
            del self.__dict__[__name.lower()]
            del self.dict[__name.lower()]
        except KeyError:
            pass

    def __setitem__(self, __key, __value) -> None:
        self.dict[self._key_check(__key)] = __value
        self.__dict__[self._key_check(__key)] = __value

    def __getitem__(self, __key):
        try:
            return self.dict[self._key_check(__key)]
        except KeyError:
            return None

    def __delitem__(self, __key):
        del self.dict[self._key_check(__key)]
        del self.__dict__[self._key_check(__key)]

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.dict):
            x = self.dict[list(self.dict.keys())[self.i]]
            self.i += 1
            return x
        else:
            raise StopIteration

    def _key_check(self, __key) -> str:
        if type(__key) == tuple and len(__key) == 2:
            __key = str(__key[0]) + str(__key[1])
        if type(__key) == str:
            if bool(re.fullmatch(self._str_pattern, __key.lower())) == True:
                tmp = re.findall(r"\d+|\w", __key.lower())
                if tmp[0].isalpha() == True:
                    return tmp[0] + tmp[1]
                else:
                    return tmp[1] + tmp[0]
            else:
                raise ValueError
        else:
            raise TypeError
         