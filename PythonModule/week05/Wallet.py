class BaseWallet:
    exchange_rate = None

    def __init__(self, name = None, amount = None):
        self.name = name
        self.amount = amount

    def copy(self):
        return self.__class__(self.name, self.amount)

    def __add__(self, other):
        tmp = self.copy()
        if issubclass(type(other), BaseWallet) == True:
            tmp.amount += other.to_base() / tmp.exchange_rate
        else:
            tmp.amount += float(other)
        return tmp

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if issubclass(type(other), BaseWallet) == True:
            self.amount += other.to_base() / self.exchange_rate
        else:
            self.amount += float(other)
        return self
        
    def __sub__(self, other):
        tmp = self.copy()
        if issubclass(type(other), BaseWallet) == True:
            tmp.amount -= other.to_base() / tmp.exchange_rate
        else:
            tmp.amount -= float(other)
        return tmp

    def __rsub__(self, other):
        tmp = self.copy()
        tmp.amount = other - self.amount
        return tmp

    def __isub__(self, other):
        if issubclass(type(other), BaseWallet) == True:
            self.amount -= other.to_base() / self.exchange_rate
        else:
            self.amount -= float(other)
        return self

    def __mul__(self, other):
        tmp = self.copy()
        tmp.amount *= float(other)
        return tmp

    def __imul__(self, other):
        self.amount *= float(other)
        return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        tmp = self.copy()
        tmp.amount /= other
        return tmp

    def __itruediv__(self, other):
        self.amount /= other
        return self

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

class EuroWallet(BaseWallet):
    exchange_rate = 70

    def __init__(self, name: str = "EuroWallet", amount: int = 0):
        super(EuroWallet, self).__init__(name, amount)

    def __str__(self):
        return f"Euro Wallet {self.name} {self.amount}"