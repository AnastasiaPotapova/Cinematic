import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import Qt

from visualchain import Ui_ChainWindow
from visualcinema import Ui_CinemaWindow
from visualroom import Ui_RoomWindow
from visualfilm import Ui_FilmWindow
from logic import Chain
from visualsearch import Ui_Search


class SearchM(QWidget, Ui_Search):
    def __init__(self, a):
        super().__init__()
        self.setupUi(self)
        self.chain = a
        self.initUI()

    def initUI(self):
        self.btnsearch.clicked.connect(self.show_searched)

    def show_searched(self):
        self.cinem_room.setText(self.chain.find_film(self.name_cinema.text()))


class FilmM(QWidget, Ui_FilmWindow):
    def __init__(self, a):
        super(FilmM, self).__init__()
        self.setupUi(self)
        self.film = a
        self.initUI()

    def initUI(self):
        self.btn_choose.clicked.connect(self.choose)
        self.room_session.setText(self.film.show_places())

    def keyPressEvent(self, event):
        ev = event.key()
        if ev == Qt.Key_Enter or ev == 16777220:
            self.choose()

    def choose(self):
        try:
            places = []
            for a in self.place_coords.text().split("/"):
                x, y = map(lambda b: int(b) - 1, a.split(";"))
                places.append((x, y))

            if any(filter(lambda x: self.film.check_place(x[0], x[1]), places)):
                self.change_status("Ошибка. Выбраны уже занятые места.")
            elif len(set(places)) != len(places):
                self.change_status(
                    "Ошибка. Выбраны как минимум 2 одиннаковых места.")
            else:
                for x in places:
                    self.film.book_place(x[0], x[1])
                self.change_status(
                    "Успешно")
        except Exception:
            self.change_status("Неверный формат ввода.")

        self.room_session.setText(self.film.show_places())

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
        self.go_over_2.clicked.connect(self.show_film)

    def add_film(self):
        self.room.append(self.film_name.text(), self.film_time.text())
        self.boxfilm.clear()
        self.boxfilm.addItems(self.room.spisok())

    def show_film(self):
        self.w1 = FilmM(self.room[self.boxfilm.currentIndex()])
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
        self.go_over_2.clicked.connect(self.show_room)

    def add_room(self):
        self.cinema.append(self.name_room.text(), int(self.x_input.text()),
                           int(self.y_input.text()))
        self.boxrooms.clear()
        self.boxrooms.addItems(self.cinema.spisok())

    def show_room(self):
        self.w1 = RoomM(self.cinema[self.boxrooms.currentIndex()])
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
        self.search_film.clicked.connect(self.search)
        self.boxcinema.addItems(self.chain.spisok())

    def add_cinema(self):
        name = self.name_cinema.text()
        self.chain.append(name)
        self.boxcinema.addItems([name])

    def show_cinema(self):
        self.w1 = CinemaM(self.chain[self.boxcinema.currentIndex()])
        self.w1.show()

    def search(self):
        self.w2 = SearchM(self.chain)
        self.w2.show()


app = QApplication(sys.argv)
ex = ChainM()
ex.show()
sys.exit(app.exec_())
