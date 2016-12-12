# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created: Wed Nov 30 02:26:25 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(572, 569)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.clientMessage = QtGui.QLineEdit(Form)
        self.clientMessage.setObjectName("clientMessage")
        self.gridLayout.addWidget(self.clientMessage, 0, 1, 1, 1)
        self.clientSend = QtGui.QPushButton(Form)
        self.clientSend.setObjectName("clientSend")
        self.gridLayout.addWidget(self.clientSend, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.clientChat = QtGui.QTextEdit(Form)
        self.clientChat.setEnabled(True)
        self.clientChat.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.clientChat.setObjectName("clientChat")
        self.gridLayout.addWidget(self.clientChat, 3, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Client", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Message:", None, QtGui.QApplication.UnicodeUTF8))
        self.clientSend.setText(QtGui.QApplication.translate("Form", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Chat:", None, QtGui.QApplication.UnicodeUTF8))

