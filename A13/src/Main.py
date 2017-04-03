from src.Verlag import *
from PySide.QtCore import *
from src.Client import *
import sys

# main class that manages clients and 'Verlag'
class Main():
    """
    Opens up 4 Windows - 3 Clients and the Verlag
    """
    def __init__(self):
        self.verlag = Verlag()
        self.clients = []
        app = QApplication(sys.argv)
        self.vc = VerlagController()
        self.vc.move(0, 450)
        self.vc.show()

        for i in range(0, 3):
            # give each client a unique name for identification
            cc = ClientController("Client" + str(i + 1), self)
            # move each client so they don't stack up
            cc.move(900, 50 + (i * 300))
            cc.setWindowTitle(cc.get_name())
            cc.show()
            # add to clients array for easier management
            self.clients.append(cc)

            # create new Observer
            client = Client(cc)
            # add new Observer to the Observable (Verlag)
            self.verlag.register(client)
        # After 5 seconds, the 'Presse' gets released
        # 5 Seconds after that, the 'Kurier' gets released
        # Finally, in the last 5 Seconds after that the 'Standard' gets released
        # src: http://stackoverflow.com/questions/16801007/sleep-is-not-working-on-pyqt4
        QTimer.singleShot(5000, lambda: self.drop_presse())
        QTimer.singleShot(10000, lambda: self.drop_kurier())
        QTimer.singleShot(15000, lambda: self.drop_standard())
        sys.exit(app.exec_())

    def drop_presse(self):
        """
        Recursively release the 'Presse' each 15 seconds
        :return: None
        """
        self.verlag.update_observers('Presse')
        QTimer.singleShot(15000, self.drop_presse)

    def drop_kurier(self):
        """
        Recursively release the 'Kurier' each 15 seconds
        :return: None
        """
        self.verlag.update_observers('Kurier')
        QTimer.singleShot(15000, lambda: self.drop_kurier())

    def drop_standard(self):
        """
        Recursively release the 'Standard' each 15 seconds
        :return: None
        """
        self.verlag.update_observers('Standard')
        QTimer.singleShot(15000, lambda: self.drop_standard())

    def update(self):
        """
        Update the clients list of each newspaper
        Gets called everytime a newspaper gets subscribed or unsubsuscribed
        :return:
        """
        for tb in self.vc.textbrowsers.values():
            tb.setText("")
        for cc in self.clients:
            if cc.is_abo['Presse']:
                self.vc.textbrowsers['Presse'].append(cc.get_name())
            if cc.is_abo['Kurier']:
                self.vc.textbrowsers['Kurier'].append(cc.get_name())
            if cc.is_abo['Standard']:
                self.vc.textbrowsers['Standard'].append(cc.get_name())

if __name__ == '__main__':
    # start the Main class
    Main()