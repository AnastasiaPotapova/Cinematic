# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chain.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChainWindow(object):
    def setupUi(self, ChainWindow):
        ChainWindow.setObjectName("ChainWindow")
        ChainWindow.resize(280, 225)
        ChainWindow.setMinimumSize(QtCore.QSize(0, 0))
        ChainWindow.setMaximumSize(QtCore.QSize(280, 227))
        ChainWindow.setStyleSheet("background-color: rgb(26, 255, 236);")
        self.centralwidget = QtWidgets.QWidget(ChainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boxcinema = QtWidgets.QComboBox(self.centralwidget)
        self.boxcinema.setGeometry(QtCore.QRect(10, 90, 261, 31))
        self.boxcinema.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.boxcinema.setObjectName("boxcinema")
        self.name_cinema = QtWidgets.QLineEdit(self.centralwidget)
        self.name_cinema.setGeometry(QtCore.QRect(70, 50, 131, 20))
        self.name_cinema.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name_cinema.setObjectName("name_cinema")
        self.btnadd_cinema = QtWidgets.QPushButton(self.centralwidget)
        self.btnadd_cinema.setGeometry(QtCore.QRect(210, 50, 61, 23))
        self.btnadd_cinema.setStyleSheet("background-color: rgb(24, 241, 0);\n"
"")
        self.btnadd_cinema.setObjectName("btnadd_cinema")
        self.go_over = QtWidgets.QPushButton(self.centralwidget)
        self.go_over.setGeometry(QtCore.QRect(10, 130, 71, 51))
        self.go_over.setStyleSheet("background-color: rgb(24, 241, 0);")
        self.go_over.setObjectName("go_over")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 0, 261, 31))
        self.textBrowser.setStyleSheet("background-color: transparent;")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.search_film = QtWidgets.QPushButton(self.centralwidget)
        self.search_film.setGeometry(QtCore.QRect(190, 130, 81, 51))
        self.search_film.setStyleSheet("background-color: rgb(24, 241, 0);")
        self.search_film.setObjectName("search_film")
        self.name_cinema_wr = QtWidgets.QLabel(self.centralwidget)
        self.name_cinema_wr.setGeometry(QtCore.QRect(10, 50, 51, 21))
        self.name_cinema_wr.setObjectName("name_cinema_wr")
        ChainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 280, 21))
        self.menubar.setObjectName("menubar")
        ChainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ChainWindow)
        self.statusbar.setObjectName("statusbar")
        ChainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ChainWindow)
        QtCore.QMetaObject.connectSlotsByName(ChainWindow)

    def retranslateUi(self, ChainWindow):
        _translate = QtCore.QCoreApplication.translate
        ChainWindow.setWindowTitle(_translate("ChainWindow", "MainWindow"))
        self.btnadd_cinema.setText(_translate("ChainWindow", "Добавить"))
        self.go_over.setText(_translate("ChainWindow", "Перейти"))
        self.textBrowser.setHtml(_translate("ChainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Добавьте или выберите кинотетр</span></p></body></html>"))
        self.search_film.setText(_translate("ChainWindow", "Найти фильм"))
        self.name_cinema_wr.setText(_translate("ChainWindow", "Название:"))

