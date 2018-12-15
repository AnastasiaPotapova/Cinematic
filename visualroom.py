# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'room.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RoomWindow(object):
    def setupUi(self, RoomWindow, color, colorb):
        RoomWindow.setObjectName("RoomWindow")
        RoomWindow.resize(290, 243)
        RoomWindow.setMinimumSize(QtCore.QSize(0, 0))
        RoomWindow.setMaximumSize(QtCore.QSize(290, 243))
        RoomWindow.setStyleSheet("background-color: rgb{};".format(color))
        self.btnadd_film = QtWidgets.QPushButton(RoomWindow)
        self.btnadd_film.setGeometry(QtCore.QRect(10, 70, 75, 23))
        self.btnadd_film.setStyleSheet("background-color: rgb{};".format(colorb))
        self.btnadd_film.setObjectName("btnadd_film")
        self.film_name = QtWidgets.QLineEdit(RoomWindow)
        self.film_name.setGeometry(QtCore.QRect(150, 70, 131, 20))
        self.film_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.film_name.setObjectName("film_name")
        self.film_time = QtWidgets.QLineEdit(RoomWindow)
        self.film_time.setGeometry(QtCore.QRect(150, 100, 131, 20))
        self.film_time.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.film_time.setObjectName("film_time")
        self.boxfilm = QtWidgets.QComboBox(RoomWindow)
        self.boxfilm.setGeometry(QtCore.QRect(10, 140, 271, 31))
        self.boxfilm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.boxfilm.setObjectName("boxfilm")
        self.go_over_2 = QtWidgets.QPushButton(RoomWindow)
        self.go_over_2.setGeometry(QtCore.QRect(10, 180, 71, 51))
        self.go_over_2.setStyleSheet("background-color: rgb{};".format(colorb))
        self.go_over_2.setObjectName("go_over_2")
        self.textBrowser = QtWidgets.QTextBrowser(RoomWindow)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 261, 31))
        self.textBrowser.setStyleSheet("background-color: transparent;")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.label1 = QtWidgets.QLabel(RoomWindow)
        self.label1.setGeometry(QtCore.QRect(90, 70, 51, 21))
        self.label1.setObjectName("label1")
        self.name_room_wr_2 = QtWidgets.QLabel(RoomWindow)
        self.name_room_wr_2.setGeometry(QtCore.QRect(70, 100, 71, 21))
        self.name_room_wr_2.setObjectName("name_room_wr_2")

        self.retranslateUi(RoomWindow)
        QtCore.QMetaObject.connectSlotsByName(RoomWindow)

    def retranslateUi(self, RoomWindow):
        _translate = QtCore.QCoreApplication.translate
        RoomWindow.setWindowTitle(_translate("RoomWindow", "RoomWindow"))
        self.btnadd_film.setText(_translate("RoomWindow", "Добавить"))
        self.go_over_2.setText(_translate("RoomWindow", "Перейти"))
        self.textBrowser.setHtml(_translate("RoomWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Добавьте или выберите фильм</span></p></body></html>"))
        self.label1.setText(_translate("RoomWindow", "Название:"))
        self.name_room_wr_2.setText(_translate("RoomWindow", "Время начала:"))

