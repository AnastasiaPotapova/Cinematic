from theatre import Theater
from exceptions import BeingError

class Chain:
    theaters = {}

    def theater_checking(self, name):
        return True if name in Chain.theaters else False


    def append_theater(self, theater_name):
        if self.theater_checking(theater_name):
            raise BeingError("Кинотеатр уже существует")
        else:
            Chain.theaters[theater_name] = Theater()

    def append_room(self, theater_name, room_name, room_sizes):
        if self.theater_checking(theater_name):
            Chain.theaters[theater_name].append(room_name, room_sizes)
        else:
            raise BeingError("Кинотеатра не существует")

    def apeend_session(self, theater_name, room_name, film_name, date, length):
        if self.theater_checking(theater_name):
            Chain.theaters[theater_name].append(room_name, room_sizes)
        else:
            raise BeingError("Кинотеатра не существует")