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
        FilmWindow.resize(294, 286)
        FilmWindow.setMinimumSize(QtCore.QSize(0, 0))
        FilmWindow.setMaximumSize(QtCore.QSize(294, 286))
        FilmWindow.setMouseTracking(True)
        FilmWindow.setStyleSheet("background-color: rgb(26, 255, 236);")
        self.btn_choose = QtWidgets.QPushButton(FilmWindow)
        self.btn_choose.setGeometry(QtCore.QRect(170, 200, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_choose.sizePolicy().hasHeightForWidth())
        self.btn_choose.setSizePolicy(sizePolicy)
        self.btn_choose.setStyleSheet("background-color: rgb(24, 241, 0);")
        self.btn_choose.setObjectName("btn_choose")
        self.place_coords = QtWidgets.QLineEdit(FilmWindow)
        self.place_coords.setGeometry(QtCore.QRect(10, 150, 271, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.place_coords.sizePolicy().hasHeightForWidth())
        self.place_coords.setSizePolicy(sizePolicy)
        self.place_coords.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.place_coords.setObjectName("place_coords")
        self.coords_wr = QtWidgets.QLabel(FilmWindow)
        self.coords_wr.setGeometry(QtCore.QRect(20, 200, 51, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coords_wr.sizePolicy().hasHeightForWidth())
        self.coords_wr.setSizePolicy(sizePolicy)
        self.coords_wr.setObjectName("coords_wr")
        self.coords = QtWidgets.QLabel(FilmWindow)
        self.coords.setGeometry(QtCore.QRect(60, 200, 61, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coords.sizePolicy().hasHeightForWidth())
        self.coords.setSizePolicy(sizePolicy)
        self.coords.setStyleSheet("background-color: transparent;")
        self.coords.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.coords.setObjectName("coords")
        self.inscription_statuc = QtWidgets.QLabel(FilmWindow)
        self.inscription_statuc.setGeometry(QtCore.QRect(20, 240, 41, 19))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inscription_statuc.sizePolicy().hasHeightForWidth())
        self.inscription_statuc.setSizePolicy(sizePolicy)
        self.inscription_statuc.setObjectName("inscription_statuc")
        self.status = QtWidgets.QTextBrowser(FilmWindow)
        self.status.setGeometry(QtCore.QRect(70, 240, 211, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        self.status.setStyleSheet("background-color: transparent;")
        self.status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.status.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.status.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.status.setObjectName("status")
        self.room_session = QtWidgets.QLabel(FilmWindow)
        self.room_session.setGeometry(QtCore.QRect(10, 10, 271, 131))
        self.room_session.setMaximumSize(QtCore.QSize(271, 131))
        self.room_session.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.room_session.setMouseTracking(True)
        self.room_session.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.room_session.setFrameShape(QtWidgets.QFrame.Box)
        self.room_session.setText("")
        self.room_session.setObjectName("room_session")

        self.retranslateUi(FilmWindow)
        QtCore.QMetaObject.connectSlotsByName(FilmWindow)

    def retranslateUi(self, FilmWindow):
        _translate = QtCore.QCoreApplication.translate
        FilmWindow.setWindowTitle(_translate("FilmWindow", "FilmWindow"))
        self.btn_choose.setText(_translate("FilmWindow", "Забронировать"))
        self.coords_wr.setText(_translate("FilmWindow", "Место:"))
        self.coords.setText(_translate("FilmWindow", "---"))
        self.inscription_statuc.setText(_translate("FilmWindow", "Статус:"))
        self.status.setHtml(_translate("FilmWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#ff0000;\">Ожидание бронирования</span></p></body></html>"))

