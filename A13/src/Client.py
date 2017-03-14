from src.Observer import Observer
from src.ClientView import *
from PySide.QtGui import *
from PySide.QtCore import *

class Client(Observer):
    def update(self, *args, **kwargs):
        pass

class ClientController(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__gui = Ui_Form()
        self.__gui.setupUi(self)

        self.__abo_buttons = {'Presse': self.__gui.pushButton, 'Standard': self.__gui.pushButton_3,
                              'Kurier': self.__gui.pushButton_5}
        self.__deabo_buttons = {'Presse': self.__gui.pushButton_2, 'Standard': self.__gui.pushButton_4,
                                'Kurier': self.__gui.pushButton_6}
        self.__show_buttons = {'Presse': self.__gui.pushButton_7, 'Standard': self.__gui.pushButton_8,
                               'Kurier': self.__gui.pushButton_9}