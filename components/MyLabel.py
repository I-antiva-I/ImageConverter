from PyQt5 import QtCore, QtGui, QtWidgets

from components.MyWidgetWithLayout import MyWidgetWithLayout


class MyLabel(QtWidgets.QLabel):
    def __init__(self, text="Placeholder text", name=None, color=None):
        super(MyLabel, self).__init__()

        # Widget name
        if name is not None:
            self.setObjectName(name)

        # Label text
        self.setText(text)

        # Text color
        if color is not None:
            self.setStyleSheet(f"color: {color};")

    def changeText(self, text):
        self.setText(text)

    def changeColor(self, color):
        self.setStyleSheet(f"color: {color};")


