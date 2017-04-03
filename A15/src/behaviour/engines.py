from behaviour.engine import *
from zipfile import *
from tarfile import *

class EngineTarGZIP(ArchiveEngine):
    def __init__(self, filename, dest):
        """
        This class Archives the data via the TAR class with the GZIP Method

        More here: https://docs.python.org/3/library/tarfile.html

        :param filename: Name of the archive

        :param dest: Where the archive is going to be placed
        """
        ArchiveEngine.__init__(self, filename, dest)

    def __str__(self):
        """
        Useful description of the Engine used

        :return: String with a description
        """
        ArchiveEngine.__str__(self)

        return "This engine uses GZIP for compression"

    def write(self):
        """
        Write to a archive file

        :return: None
        """
        ArchiveEngine.write(self)



class EngineZipStored(ArchiveEngine):
    def __init__(self, filename, dest):
        """
        This class Archives the data via the TAR class with the GZIP Method

        More here: https://docs.python.org/3/library/tarfile.html

        :param filename: Name of the archive

        :param dest: Where the archive is going to be placed
        """
        ArchiveEngine.__init__(self, filename, dest)

    def __str__(self):
        """
        Useful description of the Engine used

        :return: String with a description
        """
        ArchiveEngine.__str__(self)

        return "This engine doesn't use compression"

    def write(self):
        """
        Write to a archive file

        :return: None
        """
        ArchiveEngine.write(self)

        with ZipFile(self.filename, 'w', ZIP_STORED, allowZip64=True) as myzip:
            myzip.write('test.txt')

class EngineZipLMZA(ArchiveEngine):
    def __init__(self, filename, dest):
        """
        This class Archives the data via the TAR class with the GZIP Method

        More here: https://docs.python.org/3/library/tarfile.html

        :param filename: Name of the archive

        :param dest: Where the archive is going to be placed
        """
        ArchiveEngine.__init__(self, filename, dest)

    def __str__(self):
        """
        Useful description of the Engine used

        :return: String with a description
        """
        ArchiveEngine.__str__(self)

        return "This engine uses LMZA for compression"

    def write(self):
        """
        Write to a archive file

        :return: None
        """
        ArchiveEngine.write(self)


class EngineTarStored(ArchiveEngine):
    def __init__(self, filename, dest):
        """
        This class Archives the data via the TAR class with the GZIP Method

        More here: https://docs.python.org/3/library/tarfile.html

        :param filename: Name of the archive

        :param dest: Where the archive is going to be placed
        """
        ArchiveEngine.__init__(self, filename, dest)

    def __str__(self):
        """
        Useful description of the Engine used

        :return: String with a description
        """
        ArchiveEngine.__str__(self)

        return "This engine doesn't use compression"

    def write(self):
        """
        Write to a archive file

        :return: None
        """
        ArchiveEngine.write(self)


class EngineZipBZIP2(ArchiveEngine):
    def __init__(self, filename, dest):
        """
        This class Archives the data via the TAR class with the GZIP Method

        More here: https://docs.python.org/3/library/tarfile.html

        :param filename: Name of the archive

        :param dest: Where the archive is going to be placed
        """
        ArchiveEngine.__init__(self, filename, dest)

    def __str__(self):
        """
        Useful description of the Engine used

        :return: String with a description
        """
        ArchiveEngine.__str__(self)

        return "This engine uses BZIP2 for compression"

    def write(self):
        """
        Write to a archive file

        :return: None
        """
        ArchiveEngine.write(self)

class EngineZipDeflated(ArchiveEngine):
    def __init__(self, filename, dest):
        """
        This class Archives the data via the TAR class with the GZIP Method

        More here: https://docs.python.org/3/library/tarfile.html

        :param filename: Name of the archive

        :param dest: Where the archive is going to be placed
        """
        ArchiveEngine.__init__(self, filename, dest)

    def __str__(self):
        """
        Useful description of the Engine used

        :return: String with a description
        """
        ArchiveEngine.__str__(self)

        return "This engine uses ZIP for compression"

    def write(self):
        """
        Write to a archive file

        :return: None
        """
        ArchiveEngine.write(self)