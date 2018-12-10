# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'film.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FilmWindow(object):
    def setupUi(self, FilmWindow):
        FilmWindow.setObjectName("FilmWindow")
        FilmWindow.resize(299, 226)
        self.centralwidget = QtWidgets.QWidget(FilmWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.room_session = QtWidgets.QLineEdit(self.centralwidget)
        self.room_session.setGeometry(QtCore.QRect(10, 9, 271, 141))
        self.room_session.setObjectName("room_session")
        self.name_cinema_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.name_cinema_3.setGeometry(QtCore.QRect(130, 160, 151, 20))
        self.name_cinema_3.setObjectName("name_cinema_3")
        self.btn_choose = QtWidgets.QPushButton(self.centralwidget)
        self.btn_choose.setGeometry(QtCore.QRect(10, 160, 71, 21))
        self.btn_choose.setObjectName("btn_choose")
        FilmWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FilmWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 299, 21))
        self.menubar.setObjectName("menubar")
        FilmWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FilmWindow)
        self.statusbar.setObjectName("statusbar")
        FilmWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FilmWindow)
        QtCore.QMetaObject.connectSlotsByName(FilmWindow)

    def retranslateUi(self, FilmWindow):
        _translate = QtCore.QCoreApplication.translate
        FilmWindow.setWindowTitle(_translate("FilmWindow", "MainWindow"))
        self.btn_choose.setText(_translate("FilmWindow", "Выбрать"))

