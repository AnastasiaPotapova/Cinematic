from session import Session


class Room():
    def __init__(self, sizes):
        self.sizes = [['o'] * sizes[0]] * sizes[1]
        self.sessions = {}

    def create_session(self, film_name, film_start, duration):
        if film_name not in self.sessions:
            self.sessions[film_name] = {
                film_start: Session(self.sizes, duration)}

        else:
            self.sessions[film_name].add(
                {film_start: Session(self.sizes, duration)})

    def book(self, film_name, film_start, places):
        self.sessions[film_name][film_start].broning(places)

    def film_inf(self, film_name, film_start):
        return self.sessions[film_name][film_start].get_length(), \
               self.sessions[film_name][film_start].get_mesta()