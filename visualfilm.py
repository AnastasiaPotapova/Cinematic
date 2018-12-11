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
        FilmWindow.resize(295, 191)
        self.btn_choose = QtWidgets.QPushButton(FilmWindow)
        self.btn_choose.setGeometry(QtCore.QRect(10, 160, 71, 21))
        self.btn_choose.setObjectName("btn_choose")
        self.name_cinema_3 = QtWidgets.QLineEdit(FilmWindow)
        self.name_cinema_3.setGeometry(QtCore.QRect(130, 160, 151, 20))
        self.name_cinema_3.setObjectName("name_cinema_3")
        self.room_session = QtWidgets.QLabel(FilmWindow)
        self.room_session.setGeometry(QtCore.QRect(10, 10, 271, 131))
        self.room_session.setObjectName("room_session")

        self.retranslateUi(FilmWindow)
        QtCore.QMetaObject.connectSlotsByName(FilmWindow)

    def retranslateUi(self, FilmWindow):
        _translate = QtCore.QCoreApplication.translate
        FilmWindow.setWindowTitle(_translate("FilmWindow", "Form"))
        self.btn_choose.setText(_translate("FilmWindow", "Выбрать"))
        self.room_session.setText(_translate("FilmWindow", "TextLabel"))

