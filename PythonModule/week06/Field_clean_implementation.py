from re import fullmatch

class Field:

    def __init__(self):
        self.dict = {}

    def __contains__(self, __other: object) -> bool:
        try:
            __proper_key = self._key_normalize(__other)
        except ValueError:
            return __other in self.__dict__
        else:
            return __proper_key in self.dict

    def __setattr__(self, __name: str, __value) -> None:
        try:
            __proper_key = self._key_normalize(__name)
        except ValueError:
            return super().__setattr__(__name, __value)
        else:
            self.dict[__proper_key] = __value
            return super().__setattr__(__proper_key, __value)

    def __getattribute__(self, __name):
        try:
            __proper_key = Field._key_normalize(__name)
        except ValueError:
            return super().__getattribute__(__name)
        else:
            self.dict.get(__proper_key, None)

    def __delattr__(self, __name) -> None:
        try:
            __proper_key = self._key_normalize(__name)
        except ValueError:
            return super().__delattr__(__name)
        else:
            del self.dict[__proper_key]
            return super().__delattr__(__proper_key)

    def __setitem__(self, __key, __value) -> None:
        return self.__setattr__(self._key_normalize(__key), __value)

    def __getitem__(self, __key):
        return self.__getattribute__(self._key_normalize(__key))

    def __delitem__(self, __key):
        return self.__delattr__(self._key_normalize(__key))

    def __iter__(self):
        return iter(self.dict.values())

    @staticmethod
    def _key_normalize(__key) -> str:
        if type(__key) == tuple and len(__key) == 2:
            __key = str(__key[0]) + str(__key[1])
        if type(__key) == str:
            if bool(fullmatch(r"(^\d+\w)|(^\w\d+)", __key.lower())) == True:
                return "".join(sorted(__key.lower()))
            else:
                raise ValueError("Имя ячейки составлено неверно")
        else:
            raise TypeError("Неверные аргументы для записи")