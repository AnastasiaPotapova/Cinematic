class Film:
    def __init__(self, name, time, room, cinema):
        self.name = name
        self.time = time
        self.room = room
        self.cinema = cinema


class Room:
    def __init__(self, cinema, name, x, y, films=None):
        self.cinema = cinema
        self.name = name
        self.films = films[:] if films else []
        line = ['0' for _ in range(y)]
        self.size = [line.copy() for _ in range(x)]

    def append(self, film_name, film_time):
        self.films.append(Film(film_name, film_time, self.name, self.cinema))


class Cinema:
    def __init__(self, name='-', rooms=None):
        self.name = name
        self.cinemas = rooms[:] if rooms else []

    def append(self, room_name, x=5, y=5):
        self.cinemas.append(Room(self.name, room_name, x, y))

    def show_name(self):
        return self.name


class Chain:
    def __init__(self, a=None):
        self.chain = a[:] if a else []
        self.cinema_names = a[:] if a else []

    def append(self, cinema_name):
        self.chain.append(Cinema(cinema_name))
        self.cinema_names.append(cinema_name)

    def clean(self):
        self.chain = []
        self.cinema_names = []

    def spisok(self):
        return self.cinema_names
