# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chain.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(278, 234)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boxcinema = QtWidgets.QComboBox(self.centralwidget)
        self.boxcinema.setGeometry(QtCore.QRect(20, 90, 241, 31))
        self.boxcinema.setObjectName("boxcinema")
        self.name_cinema = QtWidgets.QLineEdit(self.centralwidget)
        self.name_cinema.setGeometry(QtCore.QRect(132, 60, 131, 20))
        self.name_cinema.setObjectName("name_cinema")
        self.btnadd_cinema = QtWidgets.QPushButton(self.centralwidget)
        self.btnadd_cinema.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.btnadd_cinema.setObjectName("btnadd_cinema")
        self.go_over = QtWidgets.QPushButton(self.centralwidget)
        self.go_over.setGeometry(QtCore.QRect(20, 130, 71, 21))
        self.go_over.setObjectName("go_over")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 261, 31))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 278, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnadd_cinema.setText(_translate("MainWindow", "Добавить"))
        self.go_over.setText(_translate("MainWindow", "Перейти"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Добавьте или выберите кинотеатр</span></p></body></html>"))

