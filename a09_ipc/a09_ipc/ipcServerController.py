from PySide.QtGui import *
from PySide.QtCore import *
import ipcServerView
import ipcModel
import socket


class Controller(QWidget):
    def __init__(self, parent=None):
        """
        Initializes variables and also connects signals to methods

        :param parent: Parent Window of this this QWidget
        """
        super().__init__(parent)
        self.__view = ipcServerView.Ui_Form()
        self.__model = ipcModel.Model()

        self.__view.setupUi(self)
        self.__connected = self.__view.serverConnected
        self.__chat = self.__view.serverChat
        self.listening = ListeningThread(self.__chat,self.__model,self)
        self.listening.start()
        self.connect(self.listening, SIGNAL("update_clients()"), self.update_clients)

    def update_clients(self):
        """
        Updates the client window. Iterates through the clients list from the model and prints each one out

        :return: void
        """
        self.__connected.clear()
        for c in self.__model.clients:
            self.__connected.append(c.get_name())


    def add_chat(self, client, text):
        """
        Adds a text from a client to the chat window

        :param client: Client which sent the text

        :param text: The text which got sent

        :return: void
        """
        self.__chat.append(client + ": " + text)


class ListeningThread(QThread):
    def __init__(self,chat,model,controller):
        """
        Initializes the scoket and variables

        :param chat: The chat window

        :param model: Model where the client list is saved

        :param controller: Controller class for calling the methods updating the GUI
        """
        QThread.__init__(self)
        self.__model = model
        self.__controller = controller
        self.socket = socket.socket()
        self.socket.bind(('localhost', 50000))
        self.socket.listen(5)
        self.__chat = chat
        self.i = 0

    def run(self):
        """
        Accepts the client and then creates a Thread for each client.

        This clientThread gets added to a clients list from the model and also gets connected to
         the add_chat() and the update_clients() function. After the threads was started a signal is sent to update the clients list on the GUI

        :return: void
        """
        try:
            while True:
                (clientsocket, address) = self.socket.accept()
                self.i+=1
                c = ClientThread(self.__model,"Client " + str(self.i),clientsocket,self)
                self.__model.clients.append(c)
                self.connect(c, SIGNAL("add_chat(QString,QString)"), self.__controller.add_chat)
                self.connect(c, SIGNAL("update_clients()"), self.__controller.update_clients)
                c.start()
                self.emit(SIGNAL('update_clients()'))
        except socket.error as serr:
            print("Socket closed.")



class ClientThread(QThread):
    def __init__(self,model,name,clientsocket,lt):
        """
        Initialize variables

        :param model: Model where client list is saved

        :param name: Name of the client, e.g. Client 1

        :param clientsocket: Clientsocket from this client

        :param lt: Listening thread object
        """
        QThread.__init__(self)
        self.__model = model
        self.__name = name
        self.__clientsocket = clientsocket
        self.__lt = lt

    def run(self):
        """
        Wait for receiving data from the client, if data is received, a signal is sent to update the chat and also every client in the clients list gets the message

        If the Client was disconnected, this object is removed from the list and the list is updated

        :return: void
        """
        while True:
            data = self.__clientsocket.recv(1024).decode()
            if not data:
                self.__clientsocket.close()
                self.__model.clients.remove(self)
                self.emit(SIGNAL('update_clients()'))
                self.__lt.i -= 1
                break

            self.emit(SIGNAL('add_chat(QString,QString)'), self.__name, data)
            for c in self.__model.clients:
                c.send_message(self.__name + ": " + data)

    def get_name(self):
        """
        :return: void
        """
        return self.__name

    def send_message(self,msg):
        """
        Sends an encoded message

        :param msg: message to be sent

        :return: void
        """
        self.__clientsocket.send(msg.encode())