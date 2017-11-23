from src.Client import *
from src.Verlag import *
from PySide.QtCore import *
import sys


verlag = Verlag()

def drop_presse():
    verlag.update_observers('Presse')
    QTimer.singleShot(15000, lambda: drop_presse())

def drop_kurier():
    verlag.update_observers('Kurier')
    QTimer.singleShot(15000, lambda: drop_kurier())

def drop_standard():
    verlag.update_observers('Standard')
    QTimer.singleShot(15000, lambda: drop_standard())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vc = VerlagController()
    vc.move(0,450)
    vc.show()

    clients = []

    for i in range(0,3):
        cc = ClientController("Client" + str(i+1))
        cc.move(900,150+(i*300))
        cc.setWindowTitle(cc.get_name())
        cc.show()
        clients.append(cc)

        client = Client(cc)
        verlag.register(client)

    # src: http://stackoverflow.com/questions/16801007/sleep-is-not-working-on-pyqt4
    QTimer.singleShot(5000, lambda: drop_presse())
    QTimer.singleShot(10000, lambda: drop_kurier())
    QTimer.singleShot(15000, lambda: drop_standard())
    sys.exit(app.exec_())

def update(self):
    for cc in clients:
        if cc.is_abo['Presse']:
            vc.textbrowsers['Presse'].append(cc.get_name())
        if cc.is_abo['Kurier']:
            vc.textbrowsers['Kurier'].append(cc.get_name())
        if cc.is_abo['Standard']:
            vc.textbrowsers['Standard'].append(cc.get_name())