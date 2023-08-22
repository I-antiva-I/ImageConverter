from PyQt5 import QtCore, QtGui, QtWidgets

from utility.enums import StatusLabelColor
from .MyLabel import MyLabel


class MyStatusLabel(MyLabel):
    def __init__(self, text="Placeholder text", name=None, color=None):
        super(MyStatusLabel, self).__init__(text, name, color)

    def updateLabel(self, text, statusColor: StatusLabelColor):
        self.changeText(text)
        self.changeColor(statusColor.value)

    def changeText(self, text):
        self.setText(text)

    def changeColor(self, color):
        self.setStyleSheet(f"color: {color};")


