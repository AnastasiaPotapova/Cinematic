class Film:
    def __init__(self, name, time, room, cinema):
        self.name = name
        self.time = time
        self.room = room
        self.cinema = cinema

    def show_name(self):
        return self.name


class Room:
    def __init__(self, cinema, name, x, y, films=None):
        self.cinema = cinema
        self.name = name
        self.films = films[:] if films else []
        line = ['0' for _ in range(y)]
        self.size = [line.copy() for _ in range(x)]

    def append(self, film_name, film_time):
        self.films.append(Film(film_name, film_time, self.name, self.cinema))

    def show_name(self):
        return self.name

    def spisok(self):
        return [x.show_name() for x in self.films]


class Cinema:
    def __init__(self, name='-', a=None):
        self.name = name
        self.rooms = a[:] if a else []

    def append(self, room_name, x=5, y=5):
        self.rooms.append(Room(self.name, room_name, x, y))

    def show_name(self):
        return self.name

    def spisok(self):
        return [x.show_name() for x in self.rooms]


class Chain:
    def __init__(self, a=None):
        self.chain = a[:] if a else []

    def append(self, cinema_name):
        self.chain.append(Cinema(cinema_name))

    def clean(self):
        self.chain = []

    def spisok(self):
        return [x.show_name() for x in self.chain]
