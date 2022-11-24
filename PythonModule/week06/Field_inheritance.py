from re import fullmatch

class Field(dict):

    def __key_normalization(func):

        def wrapper(self, __key, *args, **kwargs):
            if type(__key) in (tuple, str):
                if type(__key) == tuple and len(__key) != 2:
                    raise ValueError("Invalid tuple key")
                __new_key = "".join(sorted(str(i).lower() for i in __key))
                if fullmatch(r"(\d+\w)|(\w\d+)", __new_key):
                    return func(self, __new_key, *args, **kwargs)
                else:
                    raise ValueError("Invalid string key")
            else:
                raise TypeError("Invalid key type")

        return wrapper

    def __is_attribute_name(default_func):

        def decorator(func):

            def wrapper(self, __name, *args, **kwargs):
                if fullmatch(r"\w\d+", __name):
                    return default_func(self, __name, *args, **kwargs)
                else:
                    return func(self, __name, *args, **kwargs)

            return wrapper

        return decorator

    @__key_normalization
    def __setitem__(self, __key, __value) -> None:
        return super().__setitem__(__key, __value)

    @__key_normalization
    def __getitem__(self, __key):
        return super().__getitem__(__key)

    @__key_normalization
    def __delitem__(self, __key) -> None:
        return super().__delitem__(__key)

    @__key_normalization
    def __contains__(self, __other: object) -> bool:
        return super().__contains__(__other)

    @__is_attribute_name(__setitem__)
    def __setattr__(self, __name: str, __value) -> None:
        return super().__setattr__(__name, __value)

    @__is_attribute_name(__getitem__)
    def __getattribute__(self, __name):
        return super().__getattribute__(__name)

    @__is_attribute_name(__delitem__)
    def __delattr__(self, __name) -> None:
        return super().__delattr__(__name)

    def __missing__(self, __key) -> None:
        return None

    def __iter__(self):
        return iter(self.values())