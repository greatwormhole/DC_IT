import time
def register_booking(booking):
    if int(time.time()) % 5 == 3:
        raise KeyError
    return int(time.time()) % 2