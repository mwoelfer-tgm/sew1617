from PySide.QtGui import *
from PySide.QtCore import *
import ipcClientView
import ipcModel
import socket



class Controller(QWidget):
    #The Main Windows of this Application
    def __init__(self, parent=None):
        """
        Initializes Variables and also connects socket and button. Signal and method get connected too

        :param parent: Parent window of this QWidget
        """
        super().__init__(parent)

        self.__view = ipcClientView.Ui_Form()
        self.__model = ipcModel.Model()

        self.__view.setupUi(self)
        self.input = self.__view.clientMessage
        self.button = self.__view.clientSend
        self.output = self.__view.clientChat


        self.socket = socket.socket()

        try:
            self.socket.connect(('localhost', 50000))
            self.button.clicked.connect(self.__send_message)



        except socket.error as serr:
            print("Socket error: " + serr.strerror)
        self.lt = ListeningThread(self.socket)

        self.connect(self.lt, SIGNAL("add_chat(QString)"), self.add_chat)
        self.lt.start()

    def add_chat(self, data):
        """
        Adds text to the chat window, gets called by a signal

        :param data: Data to be added to the chat

        :return: void
        """
        self.output.append(data)

    def __send_message(self):
        """
        Method which is connected to the button, gets text from the QLineEdit object and sends it to the server

        :return: void
        """
        try:
            self.socket.send(self.input.text().encode())
            self.input.clear()
        except socket.error as serr:
            print("Socket Error: " + serr.strerror)


class ListeningThread(QThread):
    def __init__(self,clientsocket):
        """
        Initializes object of ListeningThread

        :param clientsocket: The clientsocket which was initialized and connected already
        """
        QThread.__init__(self)
        self.__socket = clientsocket


    def run(self):
        """
        Wait for received data from server and send a signal to the add_chat(text) function with the data sent

        :return: void
        """
        try:
            while True:
                data = self.__socket.recv(1024).decode()
                if not data:
                    self.__socket.close()
                    print("Nichts empfangen")
                    break
                self.emit(SIGNAL('add_chat(QString)'), data)
        except socket.error as serr:
            print("Socket Error: " + serr.strerror)