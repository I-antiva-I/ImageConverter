from PyQt5 import QtCore, QtGui, QtWidgets

from components.MyWidgetWithLayout import MyWidgetWithLayout


class MyIcon(QtWidgets.QLabel):
    def __init__(self, pathToImage, size=32, padding=4, border=2, name=None):
        super(MyIcon, self).__init__()

        # Widget name
        if name is not None:
            self.setObjectName(name)

        # Icon pixel map
        pixmap = QtGui.QPixmap(pathToImage).scaled(size, size, transformMode=QtCore.Qt.SmoothTransformation)
        self.setPixmap(pixmap)

        # Icon size
        self.defaultIconSize = size
        self.setMaximumSize(size+(padding+border)*2, size+(padding+border)*2)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet(f"padding: {padding}px; border-width: {border}px;")

    def updateIcon(self, pathToImage):
        pixmap = QtGui.\
            QPixmap(pathToImage).\
            scaled(self.defaultIconSize, self.defaultIconSize, transformMode=QtCore.Qt.SmoothTransformation)
        self.setPixmap(pixmap)
