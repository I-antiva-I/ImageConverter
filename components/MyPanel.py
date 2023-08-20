from PyQt5 import QtWidgets

from .MyWidgetWithLayout import MyWidgetWithLayout


class MyPanel(QtWidgets.QFrame, MyWidgetWithLayout):
    def __init__(self, name=None, layout=None):
        super(MyPanel, self).__init__()

        # Name of the component
        if name is not None:
            self.setObjectName(name)

        # Layout of the component
        if layout is None:
            self.setLayout(QtWidgets.QVBoxLayout())
        else:
            self.setLayout(layout)
        self.removeLayoutMargins()
