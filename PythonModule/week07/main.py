from util import *

def task21():
    
    @time_decorator
    def sleep_1_sec():
        time.sleep(1)
        print("function")
        return 25

    sleep_1_sec()

def task22():
    logger = []

    @logging_decorator(logger)
    def test_simple(a, b=2):
        return 127

    test_simple(1)

    print(logger)

def task23():
    pass

def main():
    task21()

if __name__ == "__main__":
    main()