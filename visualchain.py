# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chain.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChainWindow(object):
    def setupUi(self, ChainWindow):
        ChainWindow.setObjectName("ChainWindow")
        ChainWindow.resize(280, 270)
        self.centralwidget = QtWidgets.QWidget(ChainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boxcinema = QtWidgets.QComboBox(self.centralwidget)
        self.boxcinema.setGeometry(QtCore.QRect(10, 90, 261, 31))
        self.boxcinema.setObjectName("boxcinema")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 261, 31))
        self.textEdit.setObjectName("textEdit")
        self.name_cinema = QtWidgets.QLineEdit(self.centralwidget)
        self.name_cinema.setGeometry(QtCore.QRect(140, 60, 131, 20))
        self.name_cinema.setObjectName("name_cinema")
        self.btnadd_cinema = QtWidgets.QPushButton(self.centralwidget)
        self.btnadd_cinema.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.btnadd_cinema.setObjectName("btnadd_cinema")
        self.go_over = QtWidgets.QPushButton(self.centralwidget)
        self.go_over.setGeometry(QtCore.QRect(10, 130, 71, 51))
        self.go_over.setObjectName("go_over")
        self.name_cinema_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.name_cinema_8.setGeometry(QtCore.QRect(90, 60, 41, 20))
        self.name_cinema_8.setObjectName("name_cinema_8")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(90, 130, 181, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.example = QtWidgets.QPushButton(self.centralwidget)
        self.example.setGeometry(QtCore.QRect(60, 190, 71, 31))
        self.example.setObjectName("example")
        ChainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 280, 21))
        self.menubar.setObjectName("menubar")
        ChainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ChainWindow)
        self.statusbar.setObjectName("statusbar")
        ChainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ChainWindow)
        QtCore.QMetaObject.connectSlotsByName(ChainWindow)

    def retranslateUi(self, ChainWindow):
        _translate = QtCore.QCoreApplication.translate
        ChainWindow.setWindowTitle(_translate("ChainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("ChainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Добавте или выберите кинотеатр</span></p></body></html>"))
        self.btnadd_cinema.setText(_translate("ChainWindow", "Добавить"))
        self.go_over.setText(_translate("ChainWindow", "Перейти"))
        self.name_cinema_8.setText(_translate("ChainWindow", "name"))
        self.textEdit_2.setHtml(_translate("ChainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; color:#ff0000;\">Warning! Кинотеатры не должны иметь одинаковые названия!</span></p></body></html>"))
        self.example.setText(_translate("ChainWindow", "Перейти"))

