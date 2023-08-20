from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTextEdit, QLineEdit

from .MyPanel import MyPanel
from .MyPushButton import MyPushButton
from .MyWidgetWithLayout import MyWidgetWithLayout


class MyPathSelector(MyPanel):
    def __init__(self, name=None, layout=None):
        super(MyPathSelector, self).__init__(name, layout)

        # File dialog button
        self.dialogButton = MyPushButton(text="Path")

        # Path line edit
        self.pathLineEdit = QLineEdit()
        self.pathLineEdit.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)

        # Placement
        self.placeAll(self.dialogButton, self.pathLineEdit)
