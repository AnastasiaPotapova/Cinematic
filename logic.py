class Film:
    def __init__(self, name, time, room, cinema, size):
        self.name = name
        self.time = time
        self.room = room
        self.cinema = cinema
        self.size = size
        self.max_indexes = (len(size)-1, len(size[0])-1)
        print(self.max_indexes)
        print(name, time, room, cinema, size, sep='\n')

    def show_name(self):
        return self.name

    def show_places(self):
        return '\n'.join([' '.join(x) for x in self.size])

    def check_place_beeing(self, x, y):
        if 0 <= x <= self.max_indexes[0] and 0 <= y <= self.max_indexes[1]:
            return False
        else:
            return True

    def check_place_is_free(self, x, y):
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
        self.room = [['0' for _ in range(y)] for _ in range(x)]

    def append(self, film_name, film_time):
        self.films.append(Film(film_name, film_time, self.name, self.cinema, self.room))

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
