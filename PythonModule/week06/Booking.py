import datetime
import json
from api import register_booking

class Booking:
    
    def __init__(self, __name: str, __start: datetime.datetime, __end: datetime.datetime) -> None:
        if __start > __end:
            raise ValueError("Дата начала позже даты окончания")
        self.__name = __name
        self.__start = __start
        self.__end = __end

    @property
    def room_name(self):
        return self.__name

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, __value):
        if __value < self.end:
            self.__start = __value
        else:
            raise ValueError("Дата начала позже даты окончания")

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, __value):
        if __value > self.start:
            self.__end = __value
        else:
            raise ValueError("Дата начала позже даты окончания")

    @property
    def duration(self):
        return int((self.__end - self.__start).total_seconds() // 60)

    @property
    def start_date(self):
        return self.__start.strftime("%Y-%m-%d")

    @property
    def end_date(self):
        return self.__end.strftime("%Y-%m-%d")

    @property
    def start_time(self):
        return self.__start.strftime("%H:%M")
    
    @property
    def end_time(self):
        return self.__end.strftime("%H:%M")




def create_booking(room_name, start, end) -> str:
    print("Начинаем создание бронирования")
    res: dict = {}
    try:
        bkg = Booking(room_name, start, end)
        if register_booking(bkg) == True:
            res["created"] = True
            res["msg"] = "Бронирование создано"
        else:
            res["created"] = False
            res["msg"] = "Комната занята"
    except KeyError:
        res["created"] = False
        res["msg"] = "Комната не найдена"
    finally:
        print("Заканчиваем создание бронирования")

    res["booking"] = {"room_name": bkg.room_name,
                          "start_date": bkg.start_date,
                          "start_time": bkg.start_time,
                          "end_date": bkg.end_date,
                          "end_time": bkg.end_time,
                          "duration": bkg.duration}
    return json.dumps(res)