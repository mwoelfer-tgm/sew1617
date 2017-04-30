# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Tue Apr 25 14:53:37 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(485, 124)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.interpret_label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.interpret_label.setFont(font)
        self.interpret_label.setAlignment(QtCore.Qt.AlignCenter)
        self.interpret_label.setObjectName("interpret_label")
        self.gridLayout.addWidget(self.interpret_label, 0, 0, 1, 1)
        self.title_label = QtGui.QLabel(Form)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.gridLayout.addWidget(self.title_label, 1, 0, 1, 1)
        self.album_albel = QtGui.QLabel(Form)
        self.album_albel.setAlignment(QtCore.Qt.AlignCenter)
        self.album_albel.setObjectName("album_albel")
        self.gridLayout.addWidget(self.album_albel, 2, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.interpret_label.setText(QtGui.QApplication.translate("Form", "Interpret", None, QtGui.QApplication.UnicodeUTF8))
        self.title_label.setText(QtGui.QApplication.translate("Form", "Titel", None, QtGui.QApplication.UnicodeUTF8))
        self.album_albel.setText(QtGui.QApplication.translate("Form", "Album", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Select Folder for Playlist", None, QtGui.QApplication.UnicodeUTF8))

