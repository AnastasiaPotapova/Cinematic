from theater import Theater

class Chain:
    theaters = {}

    def append(self, theater_name):
        Chain.theaters[theater_name] = Theater()