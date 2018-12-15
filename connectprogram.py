import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtCore import Qt

from visualchain import Ui_ChainWindow
from visualcinema import Ui_CinemaWindow
from visualroom import Ui_RoomWindow
from visualfilm import Ui_FilmWindow
from logic import Chain
from visualsearch import Ui_Search
from visualsettings import Ui_Form


class SearchM(QWidget, Ui_Search):
    def __init__(self, a):
        super().__init__()
        self.setupUi(self, sett.colour, sett.colourb)
        self.chain = a
        self.initUI()

    def initUI(self):
        self.btnsearch.clicked.connect(self.show_searched)

    def show_searched(self):
        self.cinem_room.setText(self.chain.find_film(self.name_cinema.text()))


class FilmM(QWidget, Ui_FilmWindow):
    def __init__(self, a):
        super(FilmM, self).__init__()
        self.setupUi(self, sett.colour, sett.colourb)
        self.film = a
        self.initUI()

    def initUI(self):
        self.btn_choose.clicked.connect(self.choose)
        self.room_session.setText(self.film.show_places())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x, y = (event.x() - 12) // 9, (event.y() - 12) // 13

            if not self.film.check_place_beeing(y, x):
                self.place_coords.setText(
                    self.place_coords.text() + "/{};{}".format(y + 1, x + 1))

    def keyPressEvent(self, event):
        ev = event.key()
        if ev == Qt.Key_Enter or ev == 16777220:
            self.choose()

    def choose(self):
        try:
            places = []
            for a in self.place_coords.text().strip("/").split("/"):
                x, y = map(lambda b: int(b) - 1, a.split(";"))
                places.append((x, y))

            if any(filter(lambda z: self.film.check_place_beeing(z[0], z[1]),
                          places)):
                self.change_status("Ошибка. Выбраны несуществующие места.")
            elif len(set(places)) != len(places):
                self.change_status(
                    "Ошибка. Выбраны как минимум 2 одиннаковых места.")
            elif any(filter(lambda x: self.film.check_place_is_free(x[0], x[1]),
                            places)):
                self.change_status("Ошибка. Выбраны уже занятые места.")
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
        self.setupUi(self, sett.colour, sett.colourb)
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
        self.setupUi(self, sett.colour, sett.colourb)
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


class Settings(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.colour = "(25, 255, 235)"
        self.colourb = "(25, 240, 0)"
        self.setupUi(self, self.colour, self.colourb)
        self.initUI()

    def initUI(self):
        self.use_settings.clicked.connect(self.look_settings)

    def look_settings(self):
        if self.color_1.isChecked():
            self.colour = "(255, 255, 255)"
        elif self.color_2.isChecked():
            self.colour = "(225, 225, 225)"
        elif self.color_3.isChecked():
            self.colour = "(120, 120, 120)"
        elif self.color_5.isChecked():
            self.colour = "(190, 15, 175)"
        elif self.color_6.isChecked():
            self.colour = "(255, 226, 155)"
        elif self.color_7.isChecked():
            self.colour = "(255, 128, 238)"
        elif self.color_8.isChecked():
            self.colour = "(190, 245, 115)"
        elif self.color_9.isChecked():
            self.colour = "(25, 240, 0)"
        elif self.color_10.isChecked():
            self.colour = "(25, 255, 235)"
        if self.color2_1.isChecked():
            self.colourb = "(255, 255, 255)";
        elif self.color2_2.isChecked():
            self.colourb = "(220, 220, 220)";
        elif self.color2_3.isChecked():
            self.colourb = "(190, 15, 175)";
        elif self.color2_4.isChecked():
            self.colourb = "(255, 226, 155)";
        elif self.color2_5.isChecked():
            self.colourb = "(255, 128, 238)";
        elif self.color2_6.isChecked():
            self.colourb = "(190, 245, 115)";
        elif self.color2_7.isChecked():
            self.colourb = "(25, 240, 0)";
        elif self.color2_8.isChecked():
            self.colourb = "(25, 255, 235)";
        self.setupUi(self, self.colour, self.colourb)
        try:
            ex.setupUi(ex, sett.colour, sett.colourb)
        except Exception as e:
            print(e)


class ChainM(QMainWindow, Ui_ChainWindow):
    def __init__(self):
        super(ChainM, self).__init__()
        self.setupUi(self, sett.colour, sett.colourb)
        self.chain = Chain()
        self.initUI()

    def initUI(self):
        self.btnadd_cinema.clicked.connect(self.add_cinema)
        self.go_over.clicked.connect(self.show_cinema)
        self.settings_button.clicked.connect(self.show_settings)
        self.search_film.clicked.connect(self.search)
        self.boxcinema.addItems(self.chain.spisok())

    def add_cinema(self):
        name = self.name_cinema.text()
        self.chain.append(name)
        self.boxcinema.addItems([name])

    def show_cinema(self):
        self.w1 = CinemaM(self.chain[self.boxcinema.currentIndex()])
        self.w1.show()

    def show_settings(self):
        sett.show()

    def search(self):
        self.w2 = SearchM(self.chain)
        self.w2.show()


app = QApplication(sys.argv)
sett = Settings()
ex = ChainM()
ex.show()
sys.exit(app.exec_())
