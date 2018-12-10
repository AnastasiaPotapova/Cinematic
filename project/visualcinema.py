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
        CinemaWindow.resize(299, 280)
        self.centralwidget = QtWidgets.QWidget(CinemaWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 261, 31))
        self.textEdit.setObjectName("textEdit")
        self.btnadd_room = QtWidgets.QPushButton(self.centralwidget)
        self.btnadd_room.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.btnadd_room.setObjectName("btnadd_room")
        self.name_room = QtWidgets.QLineEdit(self.centralwidget)
        self.name_room.setGeometry(QtCore.QRect(150, 60, 131, 20))
        self.name_room.setObjectName("name_room")
        self.x_input = QtWidgets.QLineEdit(self.centralwidget)
        self.x_input.setGeometry(QtCore.QRect(150, 90, 131, 20))
        self.x_input.setObjectName("x_input")
        self.y_input = QtWidgets.QLineEdit(self.centralwidget)
        self.y_input.setGeometry(QtCore.QRect(150, 120, 131, 20))
        self.y_input.setObjectName("y_input")
        self.name_cinema_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.name_cinema_5.setGeometry(QtCore.QRect(100, 60, 41, 20))
        self.name_cinema_5.setObjectName("name_cinema_5")
        self.name_cinema_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.name_cinema_6.setGeometry(QtCore.QRect(20, 90, 121, 20))
        self.name_cinema_6.setObjectName("name_cinema_6")
        self.name_cinema_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.name_cinema_7.setGeometry(QtCore.QRect(20, 120, 121, 20))
        self.name_cinema_7.setObjectName("name_cinema_7")
        self.boxrooms = QtWidgets.QComboBox(self.centralwidget)
        self.boxrooms.setGeometry(QtCore.QRect(20, 150, 261, 31))
        self.boxrooms.setObjectName("boxrooms")
        self.go_over_2 = QtWidgets.QPushButton(self.centralwidget)
        self.go_over_2.setGeometry(QtCore.QRect(20, 190, 71, 51))
        self.go_over_2.setObjectName("go_over_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(100, 190, 181, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        CinemaWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CinemaWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 299, 21))
        self.menubar.setObjectName("menubar")
        CinemaWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CinemaWindow)
        self.statusbar.setObjectName("statusbar")
        CinemaWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CinemaWindow)
        QtCore.QMetaObject.connectSlotsByName(CinemaWindow)

    def retranslateUi(self, CinemaWindow):
        _translate = QtCore.QCoreApplication.translate
        CinemaWindow.setWindowTitle(_translate("CinemaWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("CinemaWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Добавте или выберите зал</span></p></body></html>"))
        self.btnadd_room.setText(_translate("CinemaWindow", "Добавить"))
        self.name_cinema_5.setText(_translate("CinemaWindow", "name"))
        self.name_cinema_6.setText(_translate("CinemaWindow", "количество рядов"))
        self.name_cinema_7.setText(_translate("CinemaWindow", "кол-во мест в ряду"))
        self.go_over_2.setText(_translate("CinemaWindow", "Перейти"))
        self.textEdit_2.setHtml(_translate("CinemaWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; color:#ff0000;\">Warning! Залы не должны иметь одинаковые названия!</span></p></body></html>"))

