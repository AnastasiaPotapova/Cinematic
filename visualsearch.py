# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Search(object):
    def setupUi(self, Search):
        Search.setObjectName("Search")
        Search.resize(283, 234)
        self.cinem_room = QtWidgets.QTextBrowser(Search)
        self.cinem_room.setGeometry(QtCore.QRect(10, 51, 261, 181))
        self.cinem_room.setObjectName("cinem_room")
        self.btnsearch = QtWidgets.QPushButton(Search)
        self.btnsearch.setGeometry(QtCore.QRect(214, 10, 61, 31))
        self.btnsearch.setObjectName("btnsearch")
        self.name_cinema = QtWidgets.QLineEdit(Search)
        self.name_cinema.setGeometry(QtCore.QRect(10, 10, 191, 31))
        self.name_cinema.setObjectName("name_cinema")

        self.retranslateUi(Search)
        QtCore.QMetaObject.connectSlotsByName(Search)

    def retranslateUi(self, Search):
        _translate = QtCore.QCoreApplication.translate
        Search.setWindowTitle(_translate("Search", "Form"))
        self.btnsearch.setText(_translate("Search", "Найти!"))
