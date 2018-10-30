class Session:
    def __init__(self, mesta, length):
        self.mesta = mesta[:]
        self.length = length

    def broning(self,spisok):
        zabr = []
        for i in spisok:
            if self.mesta[int(i[0])][int(i[1])] != 'x':
                self.mesta[int(i[0])][int(i[1])] = 'x'
            else:
                zabr.append(i)
                raise PlaceBookingError


    def get_mesta(self):
        return self.mesta

    def get_length(self):
        return self.length