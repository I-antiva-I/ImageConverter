import sys
import time

from PyQt5 import QtWidgets

from components.MyMainWindow import MyMainWindow
from controllers.MainWindowController import MainWindowController


def launchApp():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyMainWindow()

    mainWindowController = MainWindowController(mainWindow.components)
    mainWindowController.setup()
    mainWindowController.connectFunctions()

    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launchApp()
