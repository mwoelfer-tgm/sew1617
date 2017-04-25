from src.product_musikstueck.Musikstueck import *
import time

class MusikstueckFile(Musikstueck):
    # File Produkt Klasse implementiert abstrakte Produkte Klasse durch tatsächliche Ausgabe via pyglet

    def __init__(self, file, laenge, titel, interpret, album):
        Musikstueck.__init__(self, titel, interpret, album)
        self.file = file
        self.laenge = laenge

    def abspielen(self):
        """

        :return: None
        """
        self.file.play()
        print("Current Song: %s von %s aus dem Album %s" % (self.titel, self.interpret, self.album))
        time.sleep(self.laenge)