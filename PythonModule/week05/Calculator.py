class Calculator:
    last = None

    def __init__(self):
        self._hist = []

    def sum(self, a, b):
        res = a + b
        st = f"sum({a}, {b}) == {round(res, 1)}"
        self._hist.append(st)
        self._write_last(st)
        return res

    def sub(self, a, b):
        res = a - b
        st = f"sub({a}, {b}) == {round(res, 1)}"
        self._hist.append(st)
        self._write_last(st)
        return res

    def mul(self, a, b):
        res = a * b
        st = f"mul({a}, {b}) == {round(res, 1)}"
        self._hist.append(st)
        self._write_last(st)
        return res

    def div(self, a, b, mode: bool = False):
        if mode == False:
            res = a / b
        else:
            res = a % b
        st = f"div({a}, {b}) == {round(res, 1)}"
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