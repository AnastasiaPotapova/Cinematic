import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLCDNumber, QLabel
from visualchain import ChainWindow
from visualcinma import CinemaWindow
from visualroom import RoomWindow
from visualfilm import FilmWindow
from logic import Chain


class CinemaM(QMainWindow, CinemaWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chain = Chain()
        self.initUI()

    def initUI(self):
        self.btnadd_cinema.clicked.connect(self.add_cinema)
        self.boxcinema.addItems(self.chain.spisok())
        self.boxcinema.activated[str].connect(self.onActivated)

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def add_cinema(self):
        self.chain.append(self.name_cinema.text())
        self.boxcinema.clear()
        self.boxcinema.addItems(self.chain.spisok())


class ChainM(QMainWindow, ChainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chain = Chain()
        self.initUI()

    def initUI(self):
        self.btnadd_cinema.clicked.connect(self.add_cinema)
        self.boxcinema.addItems(self.chain.spisok())
        self.boxcinema.activated[str].connect(self.onActivated)

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def add_cinema(self):
        self.chain.append(self.name_cinema.text())
        self.boxcinema.clear()
        self.boxcinema.addItems(self.chain.spisok())






app = QApplication(sys.argv)
ex = Cinem()
ex.show()
sys.exit(app.exec_())
