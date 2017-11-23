from src.Observable import Observable
from PySide.QtGui import *
from PySide.QtCore import *
from src.VerlagView import *

class Verlag(Observable):
    pass

class VerlagController(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__gui = Ui_Form()
        self.__gui.setupUi(self)

        self.textbrowsers = {'Presse': self.__gui.textBrowser, 'Standard': self.__gui.textBrowser_2,
                               'Kurier': self.__gui.textBrowser_3}
