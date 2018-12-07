import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLCDNumber, QLabel
import visualchain, visualcinema
from logic import Chain


class Chain_visual(QMainWindow, visualchain.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chain = Chain()
        self.initUI()

    def initUI(self):
        self.btnadd_cinema.clicked.connect(self.add_cinema)
        self.boxcinema.addItems(self.chain.spisok())
        self.boxcinema.activated[str].connect(self.onActivated)
        self.go_over_to_cinema.clicked.connect(self.open_cinema_window)

    def onActivated(self, text):
        self.selected_cinema = text

    def open_cinema_window(self):
        pass #Хз как это сделать
        # ap = QApplication(sys.argv)
        # exx = Cinema_visual()
        # exx.show()
        # sys.exit(ap.exec_())

    def add_cinema(self):
        cinema_name = self.name_cinema.text()
        self.chain.append(cinema_name)
        self.boxcinema.addItems([cinema_name])




class Cinema_visual(QMainWindow, visualcinema.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.cinema = Chain()
        # self.initUI()

    # def initUI(self):
    #     self.btnadd_room.clicked.connect(self.add_cinema)
    #     self.boxroom.addItems(self.chain.spisok())
    #     self.boxroom.activated[str].connect(self.onActivated)


    # def onActivated(self, text):
    #     self.lbl.setText(text)
    #     self.lbl.adjustSize()
    #
    # def add_cinema(self):
    #     cinema_name = self.name_cinema.text()
    #     self.chain.append(cinema_name)
    #     self.boxcinema.addItems([cinema_name])


app = QApplication(sys.argv)
ex = Chain_visual()
ex.show()
sys.exit(app.exec_())
