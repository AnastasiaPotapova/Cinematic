# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'room.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RoomWindow(object):
    def setupUi(self, RoomWindow):
        RoomWindow.setObjectName("RoomWindow")
        RoomWindow.resize(282, 237)
        self.textEdit = QtWidgets.QTextEdit(RoomWindow)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 261, 31))
        self.textEdit.setObjectName("textEdit")
        self.btnadd_film = QtWidgets.QPushButton(RoomWindow)
        self.btnadd_film.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.btnadd_film.setObjectName("btnadd_film")
        self.name_cinema_5 = QtWidgets.QLineEdit(RoomWindow)
        self.name_cinema_5.setGeometry(QtCore.QRect(90, 50, 41, 20))
        self.name_cinema_5.setObjectName("name_cinema_5")
        self.film_name = QtWidgets.QLineEdit(RoomWindow)
        self.film_name.setGeometry(QtCore.QRect(140, 50, 131, 20))
        self.film_name.setObjectName("film_name")
        self.name_cinema_6 = QtWidgets.QLineEdit(RoomWindow)
        self.name_cinema_6.setGeometry(QtCore.QRect(10, 80, 121, 20))
        self.name_cinema_6.setObjectName("name_cinema_6")
        self.film_time = QtWidgets.QLineEdit(RoomWindow)
        self.film_time.setGeometry(QtCore.QRect(140, 80, 131, 20))
        self.film_time.setObjectName("film_time")
        self.boxfilm = QtWidgets.QComboBox(RoomWindow)
        self.boxfilm.setGeometry(QtCore.QRect(10, 110, 261, 31))
        self.boxfilm.setObjectName("boxfilm")
        self.go_over_2 = QtWidgets.QPushButton(RoomWindow)
        self.go_over_2.setGeometry(QtCore.QRect(10, 150, 71, 51))
        self.go_over_2.setObjectName("go_over_2")
        self.textEdit_2 = QtWidgets.QTextEdit(RoomWindow)
        self.textEdit_2.setGeometry(QtCore.QRect(90, 150, 181, 51))
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(RoomWindow)
        QtCore.QMetaObject.connectSlotsByName(RoomWindow)

    def retranslateUi(self, RoomWindow):
        _translate = QtCore.QCoreApplication.translate
        RoomWindow.setWindowTitle(_translate("RoomWindow", "Form"))
        self.textEdit.setHtml(_translate("RoomWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Добавте или выберите фильм</span></p></body></html>"))
        self.btnadd_film.setText(_translate("RoomWindow", "Добавить"))
        self.name_cinema_5.setText(_translate("RoomWindow", "name"))
        self.name_cinema_6.setText(_translate("RoomWindow", "time"))
        self.go_over_2.setText(_translate("RoomWindow", "Перейти"))
        self.textEdit_2.setHtml(_translate("RoomWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; color:#ff0000;\">Warning! Фильмы не должны иметь одинаковые названия!</span></p></body></html>"))

