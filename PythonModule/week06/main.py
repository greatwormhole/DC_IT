from Field import *
from Booking import *

def task18() -> None:
    field = Field()
    field[1, 'a'] = 1
    field['a', 1] = 2
    field['a', '1'] = 3
    field['1', 'a'] = 4
    field['1a'] = 5
    field['a1'] = 6
    field[1, 'A'] = 7
    field['A', 1] = 8
    field['A', '1'] = 9
    field['1', 'A'] = 10
    field['1A'] = 11
    field['A1'] = 12
    field.a10 = 33
    field.A10 = 34

    print(field['1A'])
    print(field['A1'])
    print(field['A', 1])
    print(field[1, 'A'])
    print("field.dict:", field.dict)
    print("field.__dict__:", field.__dict__)

    print((1, 'a') in field)
    print("A1" in field)
    print(('D', '4') in field)

    for i in field:
        print("loop:", i)

    print(field.a10)
    print(field.A10)
    del field.a10
    print(field.A10)
    del field.aa

def task19() -> None:
    pass

def task20() -> None:
    pass

def main():
    task18()

if __name__ == "__main__":
    main()