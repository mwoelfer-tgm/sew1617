from src.Observable import Observable
from PySide.QtGui import *
from PySide.QtCore import *
from src.VerlagView import *

# verlag implements Observable, there is nothing that has to be changed for this exercise
class Verlag(Observable):
    pass

# class which controlls GUI of verlag
class VerlagController(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__gui = Ui_Form()
        self.__gui.setupUi(self)

        self.textbrowsers = {'Presse': self.__gui.textBrowser, 'Standard': self.__gui.textBrowser_2,
                               'Kurier': self.__gui.textBrowser_3}
