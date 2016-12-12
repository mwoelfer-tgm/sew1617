import sys, ipcServerController
from PySide.QtGui import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = ipcServerController.Controller()
    c.show()

    sys.exit(app.exec_())
