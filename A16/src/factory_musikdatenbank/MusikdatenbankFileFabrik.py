from src.factory_musikdatenbank.MusikdatenbankFabrik import *
from src.product_musikstueck.MusikstueckFile import *
import pyglet
import os
from mutagen.mp3 import MP3

class MusikdatenbankFileFabrik(MusikdatenbankFabrik):
    # Konkrete MockupFactory implementiert abstrake MusikdatenFactory
    def __init__(self, dir):
        """
        Ruft Super Konstruktor auf und erstellt eine leere Playlist als Array
        """
        MusikdatenbankFabrik.__init__(self)
        self.playlist = []
        self.dir = dir

    # overwrite
    def lade_musik(self):
        """
        Fügt der Playlistt MockupMusikstuecke hinzu welche automatisch ausgelesen werden
        :return: None
        """
        for dirname, subdirs, files in os.walk(self.dir):
            for filename in files:
                file = pyglet.media.load(dirname + os.path.sep + filename)
                info = MP3(dirname + os.path.sep + filename)

                song_laenge = info.info.length
                song_titel = info["TIT2"]
                song_interpret = info["TPE1"]
                song_album = info["TALB"]

                self.playlist.append(MusikstueckFile(file, song_laenge, song_titel, song_interpret, song_album))

