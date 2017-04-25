from src.factory_musikdatenbank.MusikdatenbankMockupFabrik import *
from src.factory_musikdatenbank.MusikdatenbankFileFabrik import *
import pyglet


__author__ = 'DD'

if __name__ == '__main__':
    fabrik = MusikdatenbankFileFabrik("F:\\Users\Bernd\Music\my_playlist")
    #fabrik = MusikdatenbankMockupFabrik()
    fabrik.abspielen()

    pyglet.app.run()
