# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cinema.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CinemaWindow(object):
    def setupUi(self, CinemaWindow):
        CinemaWindow.setObjectName("CinemaWindow")
        CinemaWindow.resize(288, 285)
        self.btnadd_room = QtWidgets.QPushButton(CinemaWindow)
        self.btnadd_room.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.btnadd_room.setObjectName("btnadd_room")
        self.name_cinema_5 = QtWidgets.QLineEdit(CinemaWindow)
        self.name_cinema_5.setGeometry(QtCore.QRect(90, 60, 41, 20))
        self.name_cinema_5.setObjectName("name_cinema_5")
        self.name_room = QtWidgets.QLineEdit(CinemaWindow)
        self.name_room.setGeometry(QtCore.QRect(140, 60, 131, 20))
        self.name_room.setObjectName("name_room")
        self.name_cinema_6 = QtWidgets.QLineEdit(CinemaWindow)
        self.name_cinema_6.setGeometry(QtCore.QRect(10, 90, 121, 20))
        self.name_cinema_6.setObjectName("name_cinema_6")
        self.x_input = QtWidgets.QLineEdit(CinemaWindow)
        self.x_input.setGeometry(QtCore.QRect(140, 90, 131, 20))
        self.x_input.setText("")
        self.x_input.setObjectName("x_input")
        self.name_cinema_7 = QtWidgets.QLineEdit(CinemaWindow)
        self.name_cinema_7.setGeometry(QtCore.QRect(10, 120, 121, 20))
        self.name_cinema_7.setObjectName("name_cinema_7")
        self.y_input = QtWidgets.QLineEdit(CinemaWindow)
        self.y_input.setGeometry(QtCore.QRect(140, 120, 131, 20))
        self.y_input.setText("")
        self.y_input.setObjectName("y_input")
        self.boxrooms = QtWidgets.QComboBox(CinemaWindow)
        self.boxrooms.setGeometry(QtCore.QRect(10, 150, 261, 31))
        self.boxrooms.setObjectName("boxrooms")
        self.go_over_2 = QtWidgets.QPushButton(CinemaWindow)
        self.go_over_2.setGeometry(QtCore.QRect(10, 190, 71, 51))
        self.go_over_2.setObjectName("go_over_2")
        self.textBrowser = QtWidgets.QTextBrowser(CinemaWindow)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 261, 41))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(CinemaWindow)
        QtCore.QMetaObject.connectSlotsByName(CinemaWindow)

    def retranslateUi(self, CinemaWindow):
        _translate = QtCore.QCoreApplication.translate
        CinemaWindow.setWindowTitle(_translate("CinemaWindow", "Form"))
        self.btnadd_room.setText(_translate("CinemaWindow", "Добавить"))
        self.name_cinema_5.setText(_translate("CinemaWindow", "name"))
        self.name_cinema_6.setText(_translate("CinemaWindow", "количество рядов"))
        self.name_cinema_7.setText(_translate("CinemaWindow", "кол-во мест в ряду"))
        self.go_over_2.setText(_translate("CinemaWindow", "Перейти"))
        self.textBrowser.setHtml(_translate("CinemaWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Добавте или выберите зал</span></p></body></html>"))

