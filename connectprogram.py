import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLCDNumber, QLabel
from visualchain import Ui_MainWindow
from logic import Chain

class Example(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chain = Chain()
        self.initUI()

    def initUI(self):
        self.btnadd_cinema.connect(self.add_cinema)

        
    def add_cinema(self):
        self.chain.append(self.name_cinema.text())



app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())