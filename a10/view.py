# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a10.ui'
#
# Created: Mon Dec 12 10:54:49 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(684, 556)
        self.gridLayout = QtGui.QGridLayout(widget)
        self.gridLayout.setObjectName("gridLayout")
        self.size_slider = QtGui.QSlider(widget)
        self.size_slider.setOrientation(QtCore.Qt.Horizontal)
        self.size_slider.setObjectName("size_slider")
        self.gridLayout.addWidget(self.size_slider, 1, 1, 1, 1)
        self.canvas_preview = QtGui.QGraphicsView(widget)
        self.canvas_preview.setObjectName("canvas_preview")
        self.gridLayout.addWidget(self.canvas_preview, 2, 0, 1, 2)
        self.canvas_main = QtGui.QGraphicsView(widget)
        self.canvas_main.setObjectName("canvas_main")
        self.gridLayout.addWidget(self.canvas_main, 0, 0, 1, 3)
        self.new_point = QtGui.QPushButton(widget)
        self.new_point.setObjectName("new_point")
        self.gridLayout.addWidget(self.new_point, 3, 0, 1, 2)
        self.remove_point = QtGui.QPushButton(widget)
        self.remove_point.setObjectName("remove_point")
        self.gridLayout.addWidget(self.remove_point, 3, 2, 1, 1)
        self.label = QtGui.QLabel(widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtGui.QLabel(widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.r_slider = QtGui.QSlider(widget)
        self.r_slider.setOrientation(QtCore.Qt.Horizontal)
        self.r_slider.setObjectName("r_slider")
        self.horizontalLayout_3.addWidget(self.r_slider)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.g_slider = QtGui.QSlider(widget)
        self.g_slider.setOrientation(QtCore.Qt.Horizontal)
        self.g_slider.setObjectName("g_slider")
        self.horizontalLayout_2.addWidget(self.g_slider)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtGui.QLabel(widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.b_slider = QtGui.QSlider(widget)
        self.b_slider.setOrientation(QtCore.Qt.Horizontal)
        self.b_slider.setObjectName("b_slider")
        self.horizontalLayout.addWidget(self.b_slider)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 2, 1)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        widget.setWindowTitle(QtGui.QApplication.translate("widget", "My Floating Points", None, QtGui.QApplication.UnicodeUTF8))
        self.new_point.setText(QtGui.QApplication.translate("widget", "New Point", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_point.setText(QtGui.QApplication.translate("widget", "Remove Last Point", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("widget", "Size:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("widget", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("widget", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("widget", "B", None, QtGui.QApplication.UnicodeUTF8))

