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
    Q = DollarWallet("Q", 60)
    E = EuroWallet("E", 60)
    R = RubbleWallet("R", 60)
    print("Q ==", Q)
    print("E ==", E)
    print("R ==", R)
    print("Q + E ==", Q + E)
    print("E + Q ==", E + Q)
    print("R + Q ==", R + Q)
    print("Q + R ==", Q + R)
    print("E + R ==", E + R)
    print("R + E ==", R + E)
    print("Q.to_base() ==", Q.to_base())
    print("Q + 10 ==", Q + 10)
    print("Q - 10 ==", Q - 10)
    print("Q * 10 ==", Q * 10)
    print("20 - Q ==", 20 - Q)
    print("10 * Q ==", 10 * Q)
    print("10 + Q ==", 10 + Q)
    Q += 10
    print("Q += 10; Q ==", Q)
    Q -= 10
    print("Q -= 10; Q ==", Q)
    Q *= 10
    print("Q *= 10; Q ==", Q)
    Q /= 10
    print("Q /= 10; Q ==", Q)
    Q.spend_all()
    print("Q.spend_all(); Q ==", Q)

def main():
    task17()


if __name__ == "__main__":
    main()