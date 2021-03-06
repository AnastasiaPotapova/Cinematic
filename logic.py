class Film:
    def __init__(self, name, time, room, cinema, x, y):
        self.name = name
        self.time = time
        self.room = room
        self.cinema = cinema
        self.size = [['0' for _ in range(y)] for _ in range(x)]

    def show_name(self):
        return self.name

    def show_places(self):
        return '\n'.join([' '.join(x) for x in self.size])

    def check_place(self, x, y):
        if self.size[x][y] == '0':
            return False
        else:
            return True

    def book_place(self, x, y):
        self.size[x][y] = 'x'

class Room:
    def __init__(self, cinema, name, x, y, films=None):
        self.cinema = cinema
        self.name = name
        self.films = films[:] if films else []
        self.x = x
        self.y = y

    def append(self, film_name, film_time):
        self.films.append(Film(film_name, film_time, self.name, self.cinema, self.x, self.y))

    def show_name(self):
        return self.name

    def spisok(self):
        return [x.show_name() for x in self.films]

    def __getitem__(self, item):
        return self.films[item]


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

    def __getitem__(self, item):
        return self.rooms[item]


class Chain:
    def __init__(self, a=None):
        self.chain = a[:] if a else []

    def append(self, cinema_name):
        self.chain.append(Cinema(cinema_name))

    def clean(self):
        self.chain = []

    def spisok(self):
        return [x.show_name() for x in self.chain]

    def __getitem__(self, item):
        return self.chain[item]
