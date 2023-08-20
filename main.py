import sys
import time

from PyQt5 import QtWidgets

from components.MyMainWindow import MyMainWindow


def launchApp():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyMainWindow()

    # mainWindowController = MainWindowController(mainWindow)
    # mainWindowController.connectFunctions()

    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launchApp()
