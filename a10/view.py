# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a10.ui'
#
# Created: Sun Dec 18 20:27:04 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(500, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
        widget.setSizePolicy(sizePolicy)
        widget.setMinimumSize(QtCore.QSize(500, 500))
        widget.setMaximumSize(QtCore.QSize(500, 500))
        widget.setStatusTip("")
        widget.setWhatsThis("")
        widget.setAccessibleDescription("")
        self.new_point = QtGui.QPushButton(widget)
        self.new_point.setGeometry(QtCore.QRect(50, 450, 111, 31))
        self.new_point.setObjectName("new_point")
        self.remove_point = QtGui.QPushButton(widget)
        self.remove_point.setGeometry(QtCore.QRect(300, 450, 111, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_point.sizePolicy().hasHeightForWidth())
        self.remove_point.setSizePolicy(sizePolicy)
        self.remove_point.setObjectName("remove_point")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        widget.setWindowTitle(QtGui.QApplication.translate("widget", "My Floating Points", None, QtGui.QApplication.UnicodeUTF8))
        self.new_point.setText(QtGui.QApplication.translate("widget", "New Point", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_point.setText(QtGui.QApplication.translate("widget", "Remove Last Point", None, QtGui.QApplication.UnicodeUTF8))

