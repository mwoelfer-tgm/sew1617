from src.product_musikstueck.Musikstueck import *

class MusikstueckMockup(Musikstueck):
    # Mockup Produkt Klasse implementiert abstrakte Produkte Klasse durch simple Ausgabe
    def abspielen(self):
        """
        Gibt lediglich Titel, Interpret und Album des momentanten Stückes in der Konsole aus anstatt es tatsächlich abzuspielen

        :return: None
        """
        print("Sie hören den Titel %s von %s aus dem Album %s" % (self.titel, self.interpret, self.album))