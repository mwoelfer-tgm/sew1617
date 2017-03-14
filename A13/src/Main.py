from src.Client import *
from src.Verlag import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    verlag = VerlagController()
    verlag.move(0,450)
    verlag.show()

    clients = []

    for i in range(0,3):
        cg = ClientController()
        cg.move(900,150+(i*300))
        cg.show()
        clients.append(cg)

    sys.exit(app.exec_())


