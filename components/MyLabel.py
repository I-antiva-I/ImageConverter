from PyQt5 import QtCore, QtGui, QtWidgets

from components.MyWidgetWithLayout import MyWidgetWithLayout


class MyLabel(QtWidgets.QLabel):
    def __init__(self, text="Placeholder text", name=None):
        super(MyLabel, self).__init__()

        # Widget name
        if name is not None:
            self.setObjectName(name)

        # Text
        self.setText(text)

