# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cinema.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CinemaWindow(object):
    def setupUi(self, CinemaWindow, color, colorb):
        CinemaWindow.setObjectName("CinemaWindow")
        CinemaWindow.resize(290, 245)
        CinemaWindow.setMinimumSize(QtCore.QSize(0, 0))
        CinemaWindow.setMaximumSize(QtCore.QSize(290, 245))
        CinemaWindow.setStyleSheet("background-color: rgb{};".format(color))
        self.btnadd_room = QtWidgets.QPushButton(CinemaWindow)
        self.btnadd_room.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.btnadd_room.setStyleSheet("background-color: rgb{};".format(colorb))
        self.btnadd_room.setObjectName("btnadd_room")
        self.name_room = QtWidgets.QLineEdit(CinemaWindow)
        self.name_room.setGeometry(QtCore.QRect(150, 60, 131, 20))
        self.name_room.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name_room.setObjectName("name_room")
        self.x_input = QtWidgets.QLineEdit(CinemaWindow)
        self.x_input.setGeometry(QtCore.QRect(150, 90, 131, 20))
        self.x_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.x_input.setText("")
        self.x_input.setObjectName("x_input")
        self.y_input = QtWidgets.QLineEdit(CinemaWindow)
        self.y_input.setGeometry(QtCore.QRect(150, 120, 131, 20))
        self.y_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.y_input.setText("")
        self.y_input.setObjectName("y_input")
        self.boxrooms = QtWidgets.QComboBox(CinemaWindow)
        self.boxrooms.setGeometry(QtCore.QRect(10, 150, 271, 31))
        self.boxrooms.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.boxrooms.setObjectName("boxrooms")
        self.go_over_2 = QtWidgets.QPushButton(CinemaWindow)
        self.go_over_2.setGeometry(QtCore.QRect(10, 190, 71, 51))
        self.go_over_2.setStyleSheet("background-color: rgb{};".format(colorb))
        self.go_over_2.setObjectName("go_over_2")
        self.textBrowser = QtWidgets.QTextBrowser(CinemaWindow)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 261, 31))
        self.textBrowser.setStyleSheet("background-color: transparent;")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.name_room_wr = QtWidgets.QLabel(CinemaWindow)
        self.name_room_wr.setGeometry(QtCore.QRect(90, 60, 51, 21))
        self.name_room_wr.setObjectName("name_room_wr")
        self.label1 = QtWidgets.QLabel(CinemaWindow)
        self.label1.setGeometry(QtCore.QRect(20, 90, 91, 21))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(CinemaWindow)
        self.label2.setGeometry(QtCore.QRect(20, 120, 121, 21))
        self.label2.setObjectName("label2")
        self.status = QtWidgets.QTextBrowser(CinemaWindow)
        self.status.setGeometry(QtCore.QRect(90, 190, 191, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        self.status.setStyleSheet("background-color: transparent;")
        self.status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.status.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.status.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.status.setObjectName("status")

        self.retranslateUi(CinemaWindow)
        QtCore.QMetaObject.connectSlotsByName(CinemaWindow)

    def retranslateUi(self, CinemaWindow):
        _translate = QtCore.QCoreApplication.translate
        CinemaWindow.setWindowTitle(_translate("CinemaWindow", "CinemaWindow"))
        self.btnadd_room.setText(_translate("CinemaWindow", "Добавить"))
        self.go_over_2.setText(_translate("CinemaWindow", "Перейти"))
        self.textBrowser.setHtml(_translate("CinemaWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Добавьте или выберите зал</span></p></body></html>"))
        self.name_room_wr.setText(_translate("CinemaWindow", "Название:"))
        self.label1.setText(_translate("CinemaWindow", "Кол-во рядов:"))
        self.label2.setText(_translate("CinemaWindow", "Кол-во мест в ряду:"))

