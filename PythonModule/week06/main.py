#from Field_inheritance import *
from Field_clean_implementation import *
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
    field.b123 = 111
    field.qw2 = 0

    print(field['1A'])
    print(field['A1'])
    print(field['A', 1])
    print(field[1, 'A'])
    print("field.__dict__:", field.__dict__)
    field.a1 = 5
    print("field.__dict__:", field.__dict__)

    print((1, 'a') in field)
    print("A1" in field)
    print(('D', '4') in field)

    for i in field:
        print("loop:", i)

    print(field.a10)
    print(field.A10)
    del field.a10
    del field.b123
    print(field["a10"])
    print(field.A324)
    print(field.qw2)

def task19() -> None:
    d: dict = {}
    #d.a1 = 10
    #print(d.a1)
    #print(d.__dict__)

def task20() -> None:
    pass

def main():
    task18()

if __name__ == "__main__":
    main()