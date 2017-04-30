from src.factory_musikdatenbank.MusikdatenbankFabrik import *
from src.product_musikstueck.MusikstueckMockup import *


class MusikdatenbankMockupFabrik(MusikdatenbankFabrik):
    # Konkrete MockupFactory implementiert abstrake MusikdatenFactory
    def __init__(self):
        """
        Ruft Super Konstruktor auf und erstellt eine leere Playlist als Array
        """
        MusikdatenbankFabrik.__init__(self)
        self.playlist = []

    # overwrite
    def lade_musik(self):
        """
        Fügt der Playlistt MockupMusikstuecke hinzu welche Manuell generiert werden

        :return: None
        """
        self.playlist.append(MusikstueckMockup("1st day out tha feds", "Gucci Mane", "Everybody Looking"))
        self.playlist.append(MusikstueckMockup("10 Bands", "Drake", "If you're reading this, it's too late"))

