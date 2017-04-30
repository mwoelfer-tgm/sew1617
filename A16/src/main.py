from src.factory_musikdatenbank.MusikdatenbankMockupFabrik import *
from src.factory_musikdatenbank.MusikdatenbankFileFabrik import *
from multiprocessing import Process, Value
from threading import *
from src.gui.gui import *
import sys
from PySide.QtGui import *
from PySide.QtCore import *
import pyglet

class gui(QWidget):
    # gui class which acts as a controller for the view
    def __init__(self, parent=None):
        """
        calls super constructor, initializes the gui and assigns class attributes
        also makes sure the button has the correct function assigned to it

        :param parent:
        """
        super().__init__(parent)

        self.__gui = Ui_Form()
        self.__gui.setupUi(self)
        self.interpret = self.__gui.interpret_label
        self.titel = self.__gui.title_label
        self.album = self.__gui.album_albel
        self.__button = self.__gui.pushButton

        self.__button.clicked.connect(self.file_select)
        self.fp = None


    def file_select(self):
        """
        gets called when the button is pressed

        disables the button and starts the factory process
        the factory process takes the dir (which gets returned by the QFileDialog) and the function to update the data

        :return: None
        """
        self.__button.setEnabled(False)
        self.fp = FactoryThread(QFileDialog.getExistingDirectory(self, "Ordner für Playlist auswählen"), self.set_data)
        self.fp.start()

    def set_data(self, interpret, title, album):
        """
        Updates the data on the gui

        :param interpret: the intepret of the current song

        :param title: title of the current song

        :param album: album of the current song

        :return: None
        """
        self.interpret.setText(interpret)
        self.album.setText(album)
        self.titel.setText(title)

class FactoryThread(Thread):
    # factorythread for starting the factory process aka playing the music
    # has to implemented as thread and can't be written plain in the main thread because
    # else the gui freezes
    def __init__(self,dir,update_function):
        """
        Calls super constructor and initializes class attributes

        if self.deamon is set to True, the thread automatically becomes a 'Deamon-Thread'
        this basically means that if no other Threads are left, this Deamon Threads also automatically
        closes itself, which is incredibly helpful because the gui Thread gets terminated by closing the window
        but the factory_thread will always keep on running unless its a daemon thread

        :param dir: directory with which the factory gets initialized

        :param update_function:
        """
        Thread.__init__(self)
        self.dir = dir
        self.update_function = update_function
        self.daemon = True

    def run(self):
        """
        gets called with .start()

        initializes the factory, plays the playlist and starts the pyglet app

        :return: None
        """
        fabrik = MusikdatenbankFileFabrik(self.dir,self.update_function)
        # fabrik = MusikdatenbankMockupFabrik()
        fabrik.abspielen()
        pyglet.app.run()

if __name__ == '__main__':
    # start the gui
    app = QApplication(sys.argv)
    vc = gui()
    vc.show()
    app.exec_()

