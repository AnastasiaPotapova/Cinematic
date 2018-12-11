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
        FilmWindow.resize(295, 290)
        self.btn_choose = QtWidgets.QPushButton(FilmWindow)
        self.btn_choose.setGeometry(QtCore.QRect(170, 200, 111, 31))
        self.btn_choose.setObjectName("btn_choose")
        self.place_coords = QtWidgets.QLineEdit(FilmWindow)
        self.place_coords.setGeometry(QtCore.QRect(10, 150, 271, 31))
        self.place_coords.setObjectName("place_coords")
        self.room_session = QtWidgets.QLabel(FilmWindow)
        self.room_session.setGeometry(QtCore.QRect(10, 10, 271, 131))
        self.room_session.setObjectName("room_session")
        self.inscription_price = QtWidgets.QLabel(FilmWindow)
        self.inscription_price.setGeometry(QtCore.QRect(20, 200, 51, 21))
        self.inscription_price.setObjectName("inscription_price")
        self.price = QtWidgets.QLabel(FilmWindow)
        self.price.setGeometry(QtCore.QRect(60, 200, 61, 21))
        self.price.setText("")
        self.price.setObjectName("price")
        self.inscription_statuc = QtWidgets.QLabel(FilmWindow)
        self.inscription_statuc.setGeometry(QtCore.QRect(20, 240, 41, 19))
        self.inscription_statuc.setObjectName("inscription_statuc")
        self.status = QtWidgets.QTextBrowser(FilmWindow)
        self.status.setGeometry(QtCore.QRect(70, 240, 211, 41))
        self.status.setObjectName("status")

        self.retranslateUi(FilmWindow)
        QtCore.QMetaObject.connectSlotsByName(FilmWindow)

    def retranslateUi(self, FilmWindow):
        _translate = QtCore.QCoreApplication.translate
        FilmWindow.setWindowTitle(_translate("FilmWindow", "Form"))
        self.btn_choose.setText(_translate("FilmWindow", "Забронировать"))
        self.room_session.setText(_translate("FilmWindow", "TextLabel"))
        self.inscription_price.setText(_translate("FilmWindow", "Цена:"))
        self.inscription_statuc.setText(_translate("FilmWindow", "Статус:"))
        self.status.setHtml(_translate("FilmWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ff0000;\">Ожидание бронирования</span></p></body></html>"))

