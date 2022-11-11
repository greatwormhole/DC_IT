class Calculator:
    last = None

    def __init__(self):
        self._hist = []

    def sum(self, a, b):
        res = a + b
        if type(res) == float:
            st = f"sum({a}, {b}) == {res:.1f}"
        else:
            st = f"sum({a}, {b}) == {res}"
        self._hist.append(st)
        self._write_last(st)
        return res

    def sub(self, a, b):
        res = a - b
        if type(res) == float:
            st = f"sub({a}, {b}) == {res:.1f}"
        else:
            st = f"sub({a}, {b}) == {res}"
        self._hist.append(st)
        self._write_last(st)
        return res

    def mul(self, a, b):
        res = a * b
        if type(res) == float:
            st = f"mul({a}, {b}) == {res:.1f}"
        else:
            st = f"mul({a}, {b}) == {res}"
        self._hist.append(st)
        self._write_last(st)
        return res

    def div(self, a, b, mode: bool = False):
        if mode == False:
            res = a / b
            if type(res) == float:
                st = f"div({a}, {b}) == {res:.1f}"
            else:
                st = f"div({a}, {b}) == {res}"
            self._hist.append(st)
            self._write_last(st)
            return res
        else:
            res = a % b
            if type(res) == float:
                st = f"div({a}, {b}) == {res:.1f}"
            else:
                st = f"div({a}, {b}) == {res}"
            self._hist.append(st)
            self._write_last(st)
            return res

    def history(self, n: int):
        try:
            return self._hist[-n]
        except IndexError:
            return None
    
    @classmethod
    def _write_last(cls, str: str) -> str:
        cls.last = str
        return cls.last

    @classmethod
    def clear(cls) -> None:
        cls.last = None
        return cls.last