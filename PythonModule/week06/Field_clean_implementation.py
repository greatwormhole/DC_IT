from re import fullmatch

class Field:

    def __init__(self):
        self.dict = {}

    def __setattr__(self, __name: str, __value) -> None:
        if fullmatch(r"\w\d+", __name):
            return self.__setitem__(__name, __value)
        return super().__setattr__(__name, __value)

    def __getattribute__(self, __name):
        if fullmatch(r"\w\d+", __name):
            return self.__getitem__(__name)
        return super().__getattribute__(__name)

    def __delattr__(self, __name) -> None:
        if fullmatch(r"\w\d+", __name):
            return self.__delitem__(__name)
        return super().__delattr__(__name)

    def __key_normalization(func):

        def wrapper(self, __key, *args, **kwargs):

            if type(__key) == tuple and len(__key) == 2:
                __key = str(__key[0]) + str(__key[1])
            if type(__key) == str:
                __key = __key.lower()
                if fullmatch(r"(^\d+\w)|(^\w\d+)", __key):
                    __key = "".join(sorted(__key))
                else:
                    raise ValueError("Wrong cell name")
            else:
                raise TypeError("Wrong type of arguments")
            
            return func(self, __key, *args, **kwargs)
        
        return wrapper

    @__key_normalization
    def __setitem__(self, __key, __value) -> None:
        self.dict[__key] = __value

    @__key_normalization
    def __getitem__(self, __key):
        return self.dict.get(__key, None)

    @__key_normalization
    def __delitem__(self, __key):
        del self.dict[__key]

    @__key_normalization
    def __contains__(self, __other: object) -> bool:
        return __other in self.dict

    def __missing__(self, __key):
        return None

    def __iter__(self):
        return iter(self.dict.values())