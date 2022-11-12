from util import *


def task06() -> None:
    print(*sorted_list(), sep='\n')

def task07() -> None:
    print(*list_from_set(), sep=", ")

def task08() -> None:
    for pair in sorted_dict()[:3]:
        print(*pair, sep=": ")

def task09() -> None:
    print(start_of_week())

def main():
    task09()

if __name__ == "__main__":
    main()