from engine import *
from zipfile import *
import zipfile
from tarfile import *
import zlib
import bz2
import lzma


class TarGZIP(ArchiveEngine):
    def __init__(self, filename, dest):
        """
        This class Archives the data via the TAR class with the GZIP Method

        More here: https://docs.python.org/3/library/tarfile.html

        :param filename: Name of the archive

        :param dest: Where the archive is going to be placed
        """
        ArchiveEngine.__init__(self, filename, dest)
        self.extension = ".tar.gz"
        self.filename += self.extension

    def __str__(self):
        """
        Useful description of the Engine used

        :return: String with a description
        """
        return "This engine uses GZIP for compression"

    def write(self):
        """
        Write to a archive file

        :return: None
        """
        # Get the directory with os.walk() => Can iterate through it with a truple
        dir = os.walk(self.source)
        # get the name of the archive to compare it to the current file which gets iterated through to avoid endless recursion
        archive_name = self.filename[self.filename.rfind(os.path.sep) + 1:]

        # open a TarFile in 'Write-mode'
        with TarFile.open(self.filename, 'w:gz') as mytar:
            # src: http://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory/
            for dirname, subdirs, files in dir:
                for filename in files:
                    # check if current file equals the archive which gets created to avoid recursion
                    if not archive_name == filename: mytar.add(os.path.join(dirname, filename))



class ZipStored(ArchiveEngine):
    def __init__(self, filename, dest):
        """
        This class Archives the data via the ZIP class with the no compression

        More here: https://docs.python.org/3/library/zipfile.html

        :param filename: Name of the archive

        :param dest: Where the archive is going to be placed
        """
        ArchiveEngine.__init__(self, filename, dest)
        self.extension = ".zip"
        self.filename += self.extension

    def __str__(self):
        """
        Useful description of the Engine used

        :return: String with a description
        """
        return "This engine doesn't use compression"

    def write(self):
        """
        Write to a archive file

        :return: None
        """
        # Get the directory with os.walk() => Can iterate through it with a truple
        dir = os.walk(self.source)
        # get the name of the archive to compare it to the current file which gets iterated through to avoid endless recursion
        archive_name = self.filename[self.filename.rfind(os.path.sep) + 1:]

        # open a ZipFile in 'Write-mode'
        with ZipFile(self.filename, 'w', zipfile.ZIP_STORED, allowZip64=True) as myzip:
            # src: http://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory/
            for dirname, subdirs, files in dir:
                myzip.write(dirname)
                for filename in files:
                    # check if current file equals the archive which gets created to avoid recursion
                    if not archive_name == filename: myzip.write(os.path.join(dirname, filename))


class ZipLZMA(ArchiveEngine):
    def __init__(self, filename, dest):
        """
        This class Archives the data via the ZIP class with the LZMA Method

        More here: https://docs.python.org/3/library/tarfile.html

        :param filename: Name of the archive

        :param dest: Where the archive is going to be placed
        """
        ArchiveEngine.__init__(self, filename, dest)
        self.extension = ".7z"
        self.filename += self.extension

    def __str__(self):
        """
        Useful description of the Engine used

        :return: String with a description
        """
        return "This engine uses LZMA for compression"

    def write(self):
        """
        Write to a archive file

        :return: None
        """
        # Get the directory with os.walk() => Can iterate through it with a truple
        dir = os.walk(self.source)
        # get the name of the archive to compare it to the current file which gets iterated through to avoid endless recursion
        archive_name = self.filename[self.filename.rfind(os.path.sep) + 1:]

        # open a ZipFile in 'Write-mode'
        with ZipFile(self.filename, 'w', zipfile.ZIP_LZMA, allowZip64=True) as myzip:
            # src: http://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory/
            for dirname, subdirs, files in dir:
                myzip.write(dirname)
                for filename in files:
                    # check if current file equals the archive which gets created to avoid recursion
                    if not archive_name == filename: myzip.write(os.path.join(dirname, filename))

class TarStored(ArchiveEngine):
    def __init__(self, filename, dest):
        """
        This class Archives the data via the TAR class with no compression

        More here: https://docs.python.org/3/library/tarfile.html

        :param filename: Name of the archive

        :param dest: Where the archive is going to be placed
        """
        ArchiveEngine.__init__(self, filename, dest)
        self.extension = ".tar"
        self.filename += self.extension

    def __str__(self):
        """
        Useful description of the Engine used

        :return: String with a description
        """
        return "This engine doesn't use compression"

    def write(self):
        """
        Write to a archive file

        :return: None
        """
        # Get the directory with os.walk() => Can iterate through it with a truple
        dir = os.walk(self.source)
        # get the name of the archive to compare it to the current file which gets iterated through to avoid endless recursion
        archive_name = self.filename[self.filename.rfind(os.path.sep) + 1:]

        # open a Tar File in 'write-mode'
        with TarFile.open(self.filename, 'w') as mytar:
            # src: http://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory/
            for dirname, subdirs, files in dir:
                for filename in files:
                    # check if current file equals the archive which gets created to avoid recursion
                    if not archive_name == filename: mytar.add(os.path.join(dirname, filename))


class ZipBzip2(ArchiveEngine):
    def __init__(self, filename, dest):
        """
        This class Archives the data via the ZIP class with the BZIP2 Method

        More here: https://docs.python.org/3/library/tarfile.html

        :param filename: Name of the archive

        :param dest: Where the archive is going to be placed
        """
        ArchiveEngine.__init__(self, filename, dest)
        self.extension = ".bz2"
        self.filename += self.extension

    def __str__(self):
        """
        Useful description of the Engine used

        :return: String with a description
        """
        return "This engine uses BZIP2 for compression"

    def write(self):
        """
        Write to a archive file

        :return: None
        """
        # Get the directory with os.walk() => Can iterate through it with a truple
        dir = os.walk(self.source)
        # get the name of the archive to compare it to the current file which gets iterated through to avoid endless recursion
        archive_name = self.filename[self.filename.rfind(os.path.sep) + 1:]

        # open a ZipFile in 'Write-mode'
        with ZipFile(self.filename, 'w', zipfile.ZIP_BZIP2, allowZip64=True) as myzip:
            # src: http://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory/
            for dirname, subdirs, files in dir:
                myzip.write(dirname)
                for filename in files:
                    # check if current file equals the archive which gets created to avoid recursion
                    if not archive_name == filename: myzip.write(os.path.join(dirname, filename))


class ZipDeflated(ArchiveEngine):
    def __init__(self, filename, dest):
        """
        This class Archives the data via the ZIP class with the Deflated-Method

        More here: https://docs.python.org/3/library/tarfile.html

        :param filename: Name of the archive

        :param dest: Where the archive is going to be placed
        """
        ArchiveEngine.__init__(self, filename, dest)
        self.extension = ".zip"
        self.filename += self.extension

    def __str__(self):
        """
        Useful description of the Engine used

        :return: String with a description
        """
        return "This engine uses ZIP for compression"

    def write(self):
        """
        Write to a archive file

        :return: None
        """
        # Get the directory with os.walk() => Can iterate through it with a truple
        dir = os.walk(self.source)
        # get the name of the archive to compare it to the current file which gets iterated through to avoid endless recursion
        archive_name = self.filename[self.filename.rfind(os.path.sep) + 1:]

        # open a ZipFile in 'Write-mode'
        with ZipFile(self.filename, 'w', zipfile.ZIP_DEFLATED, allowZip64=True) as myzip:
            # src: http://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory/
            for dirname, subdirs, files in dir:
                myzip.write(dirname)
                for filename in files:
                    # check if current file equals the archive which gets created to avoid recursion
                    if not archive_name == filename: myzip.write(os.path.join(dirname, filename))


class TarLzma(ArchiveEngine):
    def __init__(self, filename, dest):
        """
        This class Archives the data via the TAR class with the LZMA Method

        More here: https://docs.python.org/3/library/tarfile.html

        :param filename: Name of the archive

        :param dest: Where the archive is going to be placed
        """
        ArchiveEngine.__init__(self, filename, dest)
        self.extension = ".tar.xz"
        self.filename += self.extension

    def __str__(self):
        """
        Useful description of the Engine used

        :return: String with a description
        """
        return "This engine uses TAR and LZMA for compression"

    def write(self):
        """
        Write to a archive file

        :return: None
        """
        # Get the directory with os.walk() => Can iterate through it with a truple
        dir = os.walk(self.source)
        # get the name of the archive to compare it to the current file which gets iterated through to avoid endless recursion
        archive_name = self.filename[self.filename.rfind(os.path.sep) + 1:]

        # open a ZipFile in 'Write-mode'
        with TarFile.open(self.filename, 'w:xz') as mytar:
            # src: http://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory/
            for dirname, subdirs, files in dir:
                for filename in files:
                    # check if current file equals the archive which gets created to avoid recursion
                    if not archive_name == filename: mytar.add(os.path.join(dirname, filename))

class TarBzip2(ArchiveEngine):
    def __init__(self, filename, dest):
        """
        This class Archives the data via the TAR class with the BZIP2 Method

        More here: https://docs.python.org/3/library/tarfile.html

        :param filename: Name of the archive

        :param dest: Where the archive is going to be placed
        """
        ArchiveEngine.__init__(self, filename, dest)
        self.extension = ".tar.bz2"
        self.filename += self.extension

    def __str__(self):
        """
        Useful description of the Engine used

        :return: String with a description
        """
        return "This engine uses TAR and BZIP2 for compression"

    def write(self):
        """
        Write to a archive file

        :return: None
        """
        # Get the directory with os.walk() => Can iterate through it with a truple
        dir = os.walk(self.source)
        # get the name of the archive to compare it to the current file which gets iterated through to avoid endless recursion
        archive_name = self.filename[self.filename.rfind(os.path.sep) + 1:]

        # open a ZipFile in 'Write-mode'
        with TarFile.open(self.filename, 'w:bz2') as mytar:
            # src: http://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory/
            for dirname, subdirs, files in dir:
                for filename in files:
                    # check if current file equals the archive which gets created to avoid recursion
                    if not archive_name == filename: mytar.add(os.path.join(dirname, filename))