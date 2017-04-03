from src.Observer import Observer
from PySide.QtGui import *
from PySide.QtCore import *
from src.Main import *
from src import ClientView

# Observer implements update method
class Client(Observer):
    def __init__(self, cc):
        """
        :param cc: the clientcontroller, used to update label on gui's when new newspaper gets released
        """
        self.__cc = cc
    def update(self, *args, **kwargs):
        """
        This gets called by the Observable, aka everytime a newspaper gets released
        :param args: List of arguments (array)
        :param kwargs: List of keywords arguments (dict)
        :return: None
        """
        # Update the label on each GUI to say which newspaper just got released
        self.__cc.text_label.setText(args[0] + " ist gerade eingetroffen!")
        # After 2 seconds clear that label again (src already cited in Main.py)
        QTimer.singleShot(2000, lambda: self.__cc.text_label.setText(""))
        # If the newspaper, which got released, is subscribed, enable to 'Zeitung anzeigen' Button in order to be able
        # to read the newspaper
        if self.__cc.is_abo[args[0]]: self.__cc.show_buttons[args[0]].setEnabled(True)

# This class controls each Client GUI
class ClientController(QWidget):
    def __init__(self, name, main, parent=None):
        super().__init__(parent)


        self.__main = main
        self.__name = name
        self.__gui = ClientView.Ui_Form()
        self.__gui.setupUi(self)

        self.ausgabe_presse = self.__gui.ausgabe_presse
        self.ausgabe_kurier = self.__gui.ausgabe_kurier
        self.ausgabe_standard = self.__gui.ausgabe_standard
        self.text_label = self.__gui.header_label

        # save information if certain newspapers are subscribed in dict
        self.is_abo = {'Presse': False, 'Standard': False, 'Kurier': False}

        # save each Subscribe Button in dict
        self.abo_buttons = {'Presse': self.__gui.pushButton, 'Standard': self.__gui.pushButton_3,
                              'Kurier': self.__gui.pushButton_5}
        # connect each button to its method in order to be able to subscribe
        self.abo_buttons['Presse'].clicked.connect(self.__abo_presse)
        self.abo_buttons['Kurier'].clicked.connect(self.__abo_kurier)
        self.abo_buttons['Standard'].clicked.connect(self.__abo_standard)

        # save each unubscribe Button in dict
        self.deabo_buttons = {'Presse': self.__gui.pushButton_2, 'Standard': self.__gui.pushButton_4,
                                'Kurier': self.__gui.pushButton_6}
        # connect each button to its method in order to be able to unsubscribe
        self.deabo_buttons['Presse'].clicked.connect(self.__deabo_presse)
        self.deabo_buttons['Kurier'].clicked.connect(self.__deabo_kurier)
        self.deabo_buttons['Standard'].clicked.connect(self.__deabo_standard)

        # save each show Button in dict
        self.show_buttons = {'Presse': self.__gui.pushButton_7, 'Standard': self.__gui.pushButton_8,
                               'Kurier': self.__gui.pushButton_9}

        # connect each button to its method in order to be able to show the newspapers
        self.show_buttons['Presse'].clicked.connect(self.__show_presse)
        self.show_buttons['Kurier'].clicked.connect(self.__show_kurier)
        self.show_buttons['Standard'].clicked.connect(self.__show_standard)

    def __abo_presse(self):
        """
        Set according bool, deactivate subscribe button, active unscubscribe button and call update Method from main class
        :return: None
        """
        self.is_abo['Presse'] = True

        self.abo_buttons['Presse'].setEnabled(False)
        self.deabo_buttons['Presse'].setEnabled(True)
        self.__main.update()

    def __abo_kurier(self):
        """
        Set according bool, deactivate subscribe button, active unscubscribe button and call update Method from main class
        :return: None
        """
        self.is_abo['Kurier'] = True

        self.abo_buttons['Kurier'].setEnabled(False)
        self.deabo_buttons['Kurier'].setEnabled(True)
        self.__main.update()

    def __abo_standard(self):
        """
        Set according bool, deactivate subscribe button, active unscubscribe button and call update Method from main class
        :return: None
        """
        self.is_abo['Standard'] = True

        self.abo_buttons['Standard'].setEnabled(False)
        self.deabo_buttons['Standard'].setEnabled(True)
        self.__main.update()

    def __deabo_presse(self):
        """
        Set according bool, activate subscribe button, deactivate unscubscribe button, deactive 'Zeitung anzeigen' button and also set newspaper text to ''.
        Call update Method from main class
        :return: None
        """
        self.is_abo['Presse'] = False

        self.abo_buttons['Presse'].setEnabled(True)
        self.deabo_buttons['Presse'].setEnabled(False)
        self.show_buttons['Presse'].setEnabled(False)
        self.ausgabe_presse.setText("")
        self.__main.update()

    def __deabo_kurier(self):
        """
        Set according bool, activate subscribe button, deactivate unscubscribe button, deactive 'Zeitung anzeigen' button and also set newspaper text to ''.
        Call update Method from main class
        :return: None
        """
        self.is_abo['Kurier'] = False

        self.abo_buttons['Kurier'].setEnabled(True)
        self.deabo_buttons['Kurier'].setEnabled(False)
        self.show_buttons['Kurier'].setEnabled(False)
        self.ausgabe_kurier.setText("")
        self.__main.update()

    def __deabo_standard(self):
        """
        Set according bool, activate subscribe button, deactivate unscubscribe button, deactive 'Zeitung anzeigen' button and also set newspaper text to ''.
        Call update Method from main class
        :return: None
        """
        self.is_abo['Standard'] = False

        self.abo_buttons['Standard'].setEnabled(True)
        self.deabo_buttons['Standard'].setEnabled(False)
        self.show_buttons['Standard'].setEnabled(False)
        self.ausgabe_standard.setText("")
        self.__main.update()


    def __show_presse(self):
        """
        Sets the text of the newspaper-output field
        :return: None
        """
        self.ausgabe_presse.setText(
            "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.")

    def __show_kurier(self):
        """
        Sets the text of the newspaper-output field
        :return: None
        """
        self.ausgabe_kurier.setText(
            "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.")

    def __show_standard(self):
        """
        Sets the text of the newspaper-output field
        :return: None
        """
        self.ausgabe_standard.setText(
            "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.")

    def get_name(self):
        """
        :return: name of the client
        """
        return self.__name

