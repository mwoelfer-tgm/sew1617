from src.factory_musikdatenbank.MusikdatenbankFabrik import *
from src.product_musikstueck.MusikstueckFile import *
import pyglet
import os
import sys

class MusikdatenbankFileFabrik(MusikdatenbankFabrik):
    # Konkrete FileFactory implementiert abstrake MusikdatenFactory
    def __init__(self, dir, update_function):
        """
        Call super Constructor and assign class attributes

        :param dir: the directory where songs get searched to be added to the playlist

        :param set_data: callback function which can get called in order to update the data in the gui
        """
        MusikdatenbankFabrik.__init__(self)
        self.playlist = []
        self.dir = dir
        self.update_function = update_function

    def lade_musik(self):
        """
        Fügt der Playlistt MockupMusikstuecke hinzu welche automatisch ausgelesen werden

        :return: None
        """
        # iterate through given directory
        for dirname, subdirs, files in os.walk(self.dir):
            for filename in files:
                # get the file extension of each file
                extension = os.path.splitext(filename)[1][1:]
                # check if the extension is a music file
                if extension.lower() in ["mp3","wma", "wav","ra", "ram", "rm", "mid", "flac", "ogg"]:
                    # get each mp3 file in this directory
                    file = pyglet.media.load(dirname + os.path.sep + filename)

                    # get each specific info needed
                    song_laenge = file.duration
                    song_titel = file.info.title.decode()
                    song_interpret = file.info.author.decode()
                    song_album = file.info.album.decode()
                    # append each song with the informations to the playlist and the gui object
                    self.playlist.append(MusikstueckFile(file, song_laenge, song_titel, song_interpret, song_album, self.update_function))
                else:
                    print("%s is not a music file!" % filename)
        if len(self.playlist) == 0:
            # if no music file was found, print out error message and exit program
            print("No suitable Files found. Please restart Program and choose another Folder")
            sys.exit(0)
