import datetime
import json
from api import register_booking

class Booking:
    
    def __init__(self, __name: str, __start: datetime.datetime, __end: datetime.datetime) -> None:
        if __start > __end:
            raise ValueError("Дата начала позже даты окончания")
        self.room_name = __name
        self.start = __start
        self.end = __end

    @property
    def duration(self):
        return (self.end - self.start).total_seconds() // 60

    @property
    def start_date(self):
        return self.start.strftime("%Y-%m-%d")

    @property
    def end_date(self):
        return self.end.strftime("%Y-%m-%d")

    @property
    def start_time(self):
        return self.start.strftime("%H:%M")
    
    @property
    def end_time(self):
        return self.end.strftime("%H:%M")

def create_booking(room_name, start, end) -> str:
    print("Начинаем создание бронирования")
    res = {}
    try:
        bkg = Booking(room_name, start, end)
        res["booking"] = {"room_name": bkg.room_name,
                          "start_date": bkg.start_date,
                          "start_time": bkg.start_time,
                          "end_date": bkg.end_date,
                          "end_time": bkg.end_time,
                          "duration": bkg.duration}
        if register_booking(bkg) == True:
            res["created"] = True
            res["msg"] = "Бронирование создано"
        else:
            res["created"] = False
            res["msg"] = "Комната занята"
    except (KeyError, ValueError):
        res["created"] = False
        res["msg"] = "Комната не найдена"
    finally:
        print("Заканчиваем создание бронирования")
    return json.dumps(res)