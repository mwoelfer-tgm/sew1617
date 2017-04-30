from src.product_musikstueck.Musikstueck import *
import time

from PySide.QtCore import *

class MusikstueckFile(Musikstueck):
    # File Produkt Klasse implementiert abstrakte Produkte Klasse durch tatsächliche Ausgabe via pyglet

    def __init__(self, file, laenge, titel, interpret, album, update_function):
        """
        Adds 2 additional parameters to the super constructor

        :param file: Thile file object which gets played

        :param laenge: The length of the mp3 file in order to pause the playlist for this amount

        :param titel: Title of the song, read out of the mp3 file

        :param interpret: Artist of the song, read out of the mp3 file

        :param album: Album of the song, read out of the mp3 file

        :param update_function: function of the gui object to update the data
        """
        # call super constructor
        Musikstueck.__init__(self, titel, interpret, album)
        # set the 3 additional parameters to class attributes
        self.file = file
        self.laenge = laenge
        self.update_function = update_function

    def abspielen(self):
        """
        Play the file object given and update information

        In order for the playlist not to play every song at the same time, everytime a song is played, time.sleep for the length of the song

        :return: None
        """
        self.file.play()
        self.update_function(str(self.interpret), str(self.titel), str(self.album))
        time.sleep(self.laenge)