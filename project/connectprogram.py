import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLCDNumber, QLabel
from visualchain import Ui_ChainWindow
from visualcinema import Ui_CinemaWindow
from visualroom import Ui_RoomWindow
from visualfilm import Ui_FilmWindow
from logic import Chain


class FilmM(QWidget, Ui_FilmWindow):
    def __init__(self):
        super(FilmM, self).__init__()
        self.setupUi(self)
        self.film = Film()
        self.initUI()

    def initUI(self):
        self.btnchoose.clicked.connect(self.choose)

    def show_room(self):
        self.room_session.append(self.film.show_places)

    def choose(self):
        self.films.append(Film(self.film_name.text(), self.film_time.text()))
        self.boxfilms.clear()
        self.boxfilms.addItems(self.films.spisok())


class RoomM(QWidget, Ui_CinemaWindow):
    def __init__(self):
        super(RoomM, self).__init__()
        self.setupUi(self)
        self.room = Room()
        self.initUI()

    def initUI(self):
        self.btnadd_film.clicked.connect(self.add_film)
        self.boxfilms.addItems(self.films.spisok())
        self.boxfilms.activated[str].connect(self.onActivated)
        self.go_over_2.clicked.connect(self.show_film)

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def add_room(self):
        self.room.append(Film(self.film_name.text(), self.film_time.text()))
        self.boxfilms.clear()
        self.boxfilms.addItems(self.films.spisok())

    def show_film(self):
        self.w1 = FilmM()
        self.w1.show()


class CinemaM(QWidget, Ui_CinemaWindow):
    def __init__(self):
        super(CinemaM, self).__init__()
        self.setupUi(self)
        self.cinema = Cinema()
        self.initUI()

    def initUI(self):
        self.btnadd_room.clicked.connect(self.add_room)
        self.boxrooms.addItems(self.rooms.spisok())
        self.boxrooms.activated[str].connect(self.onActivated)
        self.go_over_2.clicked.connect(self.show_room)

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def add_room(self):
        self.cinema.append(Room(self.name_room.text(), self.x_input.text(), self.y_input.text()))
        self.boxrooms.clear()
        self.boxrooms.addItems(self.rooms.spisok())

    def show_room(self):
        self.w1 = RoomM()
        self.w1.show()


class ChainM(QMainWindow, Ui_ChainWindow):
    def __init__(self):
        super(ChainM, self).__init__()
        self.setupUi(self)
        self.chain = Chain()
        self.initUI()

    def initUI(self):
        self.btnadd_cinema.clicked.connect(self.add_cinema)
        self.go_over.clicked.connect(self.show_cinema)
        self.boxcinema.addItems(self.chain.spisok())
        self.boxcinema.activated[str].connect(self.onActivated)

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def add_cinema(self):
        self.chain.append(self.name_cinema.text())
        self.boxcinema.clear()
        self.boxcinema.addItems(self.chain.spisok())

    def show_cinema(self):
        self.w1 = CinemaM()
        self.w1.show()


app = QApplication(sys.argv)
ex = ChainM()
ex.show()
sys.exit(app.exec_())
