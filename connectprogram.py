import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, \
    QComboBox
from PyQt5.QtWidgets import QLCDNumber, QLabel
from PyQt5 import QtCore
from visualchain import Ui_ChainWindow
from visualcinema import Ui_CinemaWindow
from visualroom import Ui_RoomWindow
from visualfilm import Ui_FilmWindow
from logic import Chain, Cinema, Room, Film


class FilmM(QWidget, Ui_FilmWindow):
    def __init__(self, a=None):  # Убрать =None и раскоментить то, что с 1-й #
        super(FilmM, self).__init__()
        self.setupUi(self)
        self.film = a
        self.initUI()

    def initUI(self):
        self.btn_choose.clicked.connect(self.choose)
        self.room_session.setText(self.film.show_places())

    def choose(self):
        try:
            places = [(int(x[0]), int(x[2])) for x in
                      self.place_coords.text().split("/")]
        except Exception:
            self.change_status("Error1")

        if any(filter(lambda x: self.film.check_place(x[0], x[1]), places)):
            self.change_status("Ошибка. Выбраны уже занятые места.")
        elif len(set(places)) != len(places):
            self.change_status(
                "Ошибка. Выбраны как минимум 2 одиннаковых места")
        else:
            for x in places:
                self.film.book_place(x[0], x[1])

        self.room_session.setText(self.film.show_places())

        ## self.films.append(Film(self.film_name.text(), self.film_time.text()))
        ## self.boxfilms.clear()
        ## self.boxfilms.addItems(self.films.spisok())

    def change_status(self, text):
        self.status.clear()
        self.status.append(text)


class RoomM(QWidget, Ui_RoomWindow):
    def __init__(self, name):
        super(RoomM, self).__init__()
        self.setupUi(self)
        self.room = name
        self.initUI()

    def initUI(self):
        self.btnadd_film.clicked.connect(self.add_film)
        self.boxfilm.addItems(self.room.spisok())
        self.boxfilm.activated[str].connect(self.onActivated)
        self.go_over_2.clicked.connect(self.show_film)

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def add_film(self):
        self.room.append(self.film_name.text(), self.film_time.text())
        self.boxfilm.clear()
        self.boxfilm.addItems(self.room.spisok())

    def show_film(self):
        self.w1 = FilmM(self.room[0])
        self.w1.show()


class CinemaM(QWidget, Ui_CinemaWindow):
    def __init__(self, name):
        super(CinemaM, self).__init__()
        self.setupUi(self)
        self.cinema = name
        self.initUI()

    def initUI(self):
        self.btnadd_room.clicked.connect(self.add_room)
        self.boxrooms.addItems(self.cinema.spisok())
        self.boxrooms.activated[str].connect(self.onActivated)
        self.go_over_2.clicked.connect(self.show_room)

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def add_room(self):
        self.cinema.append(self.name_room.text(), int(self.x_input.text()),
                           int(self.y_input.text()))
        self.boxrooms.clear()
        self.boxrooms.addItems(self.cinema.spisok())

    def show_room(self):
        self.w1 = RoomM(self.cinema[0])
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
        # self.boxcinema.activated[str].connect(self.onActivated)

    # def ex(self):
    #     print(self.boxcinema.currentIndex())

    # def onActivated(self, text):
    #     self.lbl.setText(text)
    #     self.lbl.adjustSize()

    def add_cinema(self):
        name = self.name_cinema.text()
        self.chain.append(name)
        self.boxcinema.addItems([name])

    def show_cinema(self):
        self.w1 = CinemaM(self.chain.chain[self.chain.spisok().index(
            self.boxcinema.currentText())])
        self.w1.show()


app = QApplication(sys.argv)
ex = ChainM()
ex.show()
sys.exit(app.exec_())
