class BaseWallet:
    exchange_rate = None

    def __init__(self, name = None, amount = None):
        self.name = name
        self.amount = amount

    def __add__(self, other):
        if issubclass(type(other), BaseWallet) == True:
            n_amount = self.amount + other.amount * other.exchange_rate
        else:
            n_amount = self.amount + float(other)
        pass

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        self = self.__add__(other)
        
    def __sub__(self, other):
        if issubclass(type(other), BaseWallet) == True:
            n_amount = self.amount - other.amount * other.exchange_rate
        else:
            n_amount = self.amount - float(other)
        return BaseWallet(self.name, n_amount)

    def __rsub__(self, other):
        return BaseWallet(self.name, other - self.amount)

    def __isub__(self, other):
        self = self.__sub__(other)

    def __mul__(self, other):
        return BaseWallet(self.name, self.amount * other)

    def __imul__(self, other):
        self = self.__mul__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        return BaseWallet(self.name, self.amount / other)

    def __idiv__(self, other):
        self = self.__div__(other)

    def __eq__(self, other):
        return bool(type(self) == type(other) and self.amount == other.amount)
        
    def __str__(self):
        return f"{type(self)} {self.name} {self.amount}"

    def __repr__(self):
        return str(self)

    def spend_all(self):
        if self.amount > 0:
            self.amount = 0

    def to_base(self):
        return self.exchange_rate * self.amount



class RubbleWallet(BaseWallet):
    exchange_rate = 1

    def __init__(self, name: str = "RubbleWallet", amount: int = 0):
        super(RubbleWallet, self).__init__(name, amount)

    def __str__(self):
        return f"Rubble Wallet {self.name} {self.amount}"

class DollarWallet(BaseWallet):
    exchange_rate = 60
    def __init__(self, name: str = "DollarWallet", amount: int = 0):
        super(DollarWallet, self).__init__(name, amount)

    def __str__(self):
        return f"Dollar Wallet {self.name} {self.amount}"

    def __add__(self, other):
        super().__add__(other)
        return DollarWallet(self.name, n_amount)

class EuroWallet(BaseWallet):
    exchange_rate = 70

    def __init__(self, name: str = "EuroWallet", amount: int = 0):
        super(EuroWallet, self).__init__(name, amount)

    def __str__(self):
        return f"Euro Wallet {self.name} {self.amount}"