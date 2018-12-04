class BeingError(Exception):
    def __init__(self, text):
        print(text)

class PlaceBookingError(Exception):
    def __init__(self, text):
        print(text)