from Field_inheritance import *
#from Field_clean_implementation import *
from Booking import *
import json

def task_Field_inherintance() -> None:
    field = Field()

    print("test_asignment:")
    field.qwerty = "ytrewq"
    field.A1 = 14
    field.a1 = 13
    field[1, 'a'] = 12
    field['a', 1] = 11
    field['a', '1'] = 10
    field['1', 'a'] = 9
    field['1a'] = 8
    field['a1'] = 7
    field[1, 'A'] = 6
    field['A', 1] = 5
    field['A', '1'] = 4
    field['1', 'A'] = 3
    field['1A'] = 2
    field['A1'] = 1
    field['b2'] = 100
    print("Only keys:", *field.keys())
    print("Only attributes", field.__dict__, '\n')

    print("test_printing:")
    print("field['1A'] ==", field['1A'])
    print("field['A1'] ==", field['A1'])
    print("field['A', 1] ==", field['A', 1])
    print("field[1, 'A'] ==", field[1, 'A'])
    print("field.a1 ==", field.a1)
    print("field.A1 ==", field.A1)
    print("field.qwerty ==", field.qwerty)
    print("field.__dict__:", field.__dict__, '\n')

    print("(1, 'a') in field:", (1, 'a') in field)
    print('"A1" in field:', "A1" in field)
    print("('D', '4') in field:", ('D', '4') in field, '\n')

    print("loop testing:")
    for i in field:
        print("loop:", i)
    print('')

    print("test_printing_None:")
    print("field['10A'] ==", field['10A'])
    print("field['A10'] ==", field['A10'])
    print("field['A', 10] ==", field['A', 10])
    print("field[10, 'A'] ==", field[10, 'A'])
    print("field.a10 ==", field.a10)
    print("field.A10 ==", field.A10, '\n')

def task_Field_clean() -> None:
    field = Field()

    print("test_asignment:")
    field.qwerty = "ytrewq"
    field.A1 = 14
    field.a1 = 13
    field[1, 'a'] = 12
    field['a', 1] = 11
    field['a', '1'] = 10
    field['1', 'a'] = 9
    field['1a'] = 8
    field['a1'] = 7
    field[1, 'A'] = 6
    field['A', 1] = 5
    field['A', '1'] = 4
    field['1', 'A'] = 3
    field['1A'] = 2
    field['A1'] = 1
    field['b2'] = 100
    print("Only keys:", *field.dict.keys())
    print("Only attributes", field.__dict__, '\n')

    print("test_printing:")
    print("field['1A'] ==", field['1A'])
    print("field['A1'] ==", field['A1'])
    print("field['A', 1] ==", field['A', 1])
    print("field[1, 'A'] ==", field[1, 'A'])
    print("field.a1 ==", field.a1)
    print("field.A1 ==", field.A1)
    print("field.qwerty ==", field.qwerty)
    print("field.__dict__:", field.__dict__, '\n')

    print("(1, 'a') in field:", (1, 'a') in field)
    print('"A1" in field:', "A1" in field)
    print("('D', '4') in field:", ('D', '4') in field, '\n')

    print("loop testing:")
    for i in field:
        print("loop:", i)
    print('')

    print("test_printing_None:")
    print("field['10A'] ==", field['10A'])
    print("field['A10'] ==", field['A10'])
    print("field['A', 10] ==", field['A', 10])
    print("field[10, 'A'] ==", field[10, 'A'])
    print("field.a10 ==", field.a10)
    print("field.A10 ==", field.A10, '\n')

def task20() -> None:
    result = create_booking(
    "Вагнер",
    datetime.datetime(2022, 9, 1, 14),
    datetime.datetime(2022, 9, 1, 15, 15)
    )
    print(json.loads(result))

def main():
    task20()

if __name__ == "__main__":
    main()