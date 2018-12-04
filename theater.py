from room import Room
from exceptions import BeingError


class Theater:
    def __init__(self):
        self.rooms = {}

    def append(self, room, sizes):
        if room not in self.rooms:
            self.rooms[room] = Room(sizes)
        else:
            raise BeingError("Кинозал уже существует")

    # def append_session(self):

    def show_information(self):
        return self.rooms