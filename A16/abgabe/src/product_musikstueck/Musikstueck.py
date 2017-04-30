from abc import ABCMeta, abstractmethod
__author__ = 'DD'

class Musikstueck(metaclass=ABCMeta):
    """ Die basisklasse fuer alle Musikstuecke
    """

    def __init__(self, titel, interpret, album):
        self.titel = titel
        self.interpret = interpret
        self.album = album

    @abstractmethod
    def abspielen(self):
        pass
