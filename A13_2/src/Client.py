from src.Observer import Observer
from src.ClientView import *
from PySide.QtGui import *
from PySide.QtCore import *
from Main import *
import time

class Client(Observer):
    def __init__(self, cc):
        self.__cc = cc
    def update(self, *args, **kwargs):
        self.__cc.text_label.setText(args[0] + " ist gerade eingetroffen!")
        QTimer.singleShot(2000, lambda: self.__cc.text_label.setText(""))
        if self.__cc.is_abo[args[0]]: self.__cc.show_buttons[args[0]].setEnabled(True)


class ClientController(QWidget):
    def __init__(self, name, parent=None):
        super().__init__(parent)

        self.__name = name
        self.__gui = Ui_Form()
        self.__gui.setupUi(self)
        
        self.is_abo = {'Presse': False, 'Standard': False, 'Kurier': False}

        self.abo_buttons = {'Presse': self.__gui.pushButton, 'Standard': self.__gui.pushButton_3,
                              'Kurier': self.__gui.pushButton_5}
        self.abo_buttons['Presse'].clicked.connect(self.__abo_presse)
        self.abo_buttons['Kurier'].clicked.connect(self.__abo_kurier)
        self.abo_buttons['Standard'].clicked.connect(self.__abo_standard)


        self.deabo_buttons = {'Presse': self.__gui.pushButton_2, 'Standard': self.__gui.pushButton_4,
                                'Kurier': self.__gui.pushButton_6}
        self.deabo_buttons['Presse'].clicked.connect(self.__deabo_presse)
        self.deabo_buttons['Kurier'].clicked.connect(self.__deabo_kurier)
        self.deabo_buttons['Standard'].clicked.connect(self.__deabo_standard)

        self.show_buttons = {'Presse': self.__gui.pushButton_7, 'Standard': self.__gui.pushButton_8,
                               'Kurier': self.__gui.pushButton_9}

        self.show_buttons['Presse'].clicked.connect(self.__show_presse)
        self.show_buttons['Kurier'].clicked.connect(self.__show_kurier)
        self.show_buttons['Standard'].clicked.connect(self.__show_standard)

    def __abo_presse(self):
        self.is_abo['Presse'] = True

        self.abo_buttons['Presse'].setEnabled(False)
        self.deabo_buttons['Presse'].setEnabled(True)
        update()

    def __abo_kurier(self):
        self.is_abo['Kurier'] = True

        self.abo_buttons['Kurier'].setEnabled(False)
        self.deabo_buttons['Kurier'].setEnabled(True)

    def __abo_standard(self):
        self.is_abo['Standard'] = True

        self.abo_buttons['Standard'].setEnabled(False)
        self.deabo_buttons['Standard'].setEnabled(True)

    def __deabo_presse(self):
        self.is_abo['Presse'] = False

        self.abo_buttons['Presse'].setEnabled(True)
        self.deabo_buttons['Presse'].setEnabled(False)
        self.show_buttons['Presse'].setEnabled(False)

    def __deabo_kurier(self):
        self.is_abo['Kurier'] = False

        self.abo_buttons['Kurier'].setEnabled(True)
        self.deabo_buttons['Kurier'].setEnabled(False)
        self.show_buttons['Kurier'].setEnabled(False)

    def __deabo_standard(self):
        self.is_abo['Standard'] = False

        self.abo_buttons['Standard'].setEnabled(True)
        self.deabo_buttons['Standard'].setEnabled(False)
        self.show_buttons['Standard'].setEnabled(False)

    def __show_presse(self):
        print("Hier ist die Presse")

    def __show_kurier(self):
        print("Hier ist der Kurier")

    def __show_standard(self):
        print("Hier ist der Standard")

    def get_name(self):
        return self.__name