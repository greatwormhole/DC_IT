from Calculator import *
from Wallet import *


def task16()-> None:
    c = Calculator()
    print(c.sum(2, 7))
    print(c.sub(2, 7))
    print(c.mul(2, 7))
    print(c.div(2, 7))
    print(c.div(2, 7, mode=True))
    print(c.last)
    c.clear()
    print(c.last)
    print(c.history(4))
    t = Calculator()
    print(t.sub(1, 2))
    print(c.last)
    print(t.last)
    print(t.history(1))

def task17() -> None:
    Q = DollarWallet("Q", 10)
    print(Q + 10)

def main():
    task17()


if __name__ == "__main__":
    main()