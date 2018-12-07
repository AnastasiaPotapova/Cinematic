class Film:
    def __init__(self, name, time, room, cinema):
        self.name = name
        self.time = time
        self.room = room
        self.cinema = cinema

class Room:
    def __init__(self, cinema, name, x, y, a):
        self.cinema = cinema
        self.name = name
        self.size = [['0' for x in range(y)] for x in range(x)]
        self.cinemas = a[:] if a else []

    def append(self, film_name, film_time):
        self.cinemas.append(Room(self.name, room_name, Type))


class Cinema:
    def __init__(self, name, rooms=None):
        self.name = name
        self.cinemas = rooms[:] if rooms else []

    def append(self, room_name, x=5, y=5):
        self.cinemas.append(Room(self.name, room_name, x, y))


class Chain:
    def __init__(self, a=None):
        self.chain = a[:] if a else []

    def append(self, cinema_name):
        self.chain.append(Cinema(cinema_name))

    def show(self):
        print(self.chain)



