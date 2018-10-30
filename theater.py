from room import Room
from exceptions import Being


class Theater:
    def __init__(self):
        self.rooms = {}

    def append(self, room, sizes):
        if room not in self.rooms:
            self.rooms[room] = Room(sizes)
        else:
            raise Being("Кинозал уже существует")

    def show_information(self):
        return self.rooms
