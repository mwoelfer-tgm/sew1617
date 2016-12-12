import sys, ipcClientController
from PySide.QtGui import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = ipcClientController.Controller()
    c.show()

    sys.exit(app.exec_())
