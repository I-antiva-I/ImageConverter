from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont

from components.MyWidgetWithLayout import MyWidgetWithLayout


class MyPanelLabeled(QtWidgets.QGroupBox, MyWidgetWithLayout):
    def __init__(self, name=None, layout=None, label: str = None):
        super(MyPanelLabeled, self).__init__()

        # Name of the component
        if name is not None:
            self.setObjectName(name)

        # Layout of the component
        if layout is None:
            self.setLayout(QtWidgets.QVBoxLayout())
        else:
            self.setLayout(layout)
        self.removeLayoutMargins()

        # Label (text) of the component
        if label is not None:
            self.setTitle(label)




