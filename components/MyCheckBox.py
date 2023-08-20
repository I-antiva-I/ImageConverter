from PyQt5 import QtCore, QtGui, QtWidgets

from components.MyIcon import MyIcon
from components.MyLabel import MyLabel
from components.MyWidgetWithLayout import MyWidgetWithLayout


class MyCheckBox(QtWidgets.QFrame, MyWidgetWithLayout):
    def __init__(self, name=None, text="Some Text", iconPath=None, defaultState=False):
        super(MyCheckBox, self).__init__()

        # Name of the component
        if name is not None:
            self.setObjectName(name)

        # Layout of the component
        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.removeLayoutMargins()

        # Icon of the component
        self.icon = MyIcon(iconPath, 32+6+2, 6, 2)
        self.place(self.icon)

        # Label of the component
        self.label = MyLabel(text)
        self.label.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.place(self.label)

        # State
        self.setProperty("currentState", defaultState)

    def getCurrentState(self):
        return self.property("currentState")

    def updateIcon(self, path):
        self.icon.updateIcon("./images/warning.ico")

    # Update property and recompute CSS
    def updateCurrentState(self, value):
        self.setProperty("currentState", value)
        self.setStyleSheet(self.styleSheet())

    # Mouse events
    def enterEvent(self, QEvent):
        super().enterEvent(QEvent)
        # print(self, "ENTER_EVENT")
        # self.prepareIcon(self.iconPathHovered)

    def leaveEvent(self, QEvent):
        super().leaveEvent(QEvent)
        # print(self, "LEAVE_EVENT")
        # self.prepareIcon(self.iconPathDefault)

    def mousePressEvent(self, QEvent):
        super().mousePressEvent(QEvent)
        # print(self, "PRESS_EVENT")
        # Click via left button
        if QEvent.button() == 1:
            self.updateCurrentState(not self.getCurrentState())



    def mouseReleaseEvent(self, QEvent):
        super().mouseReleaseEvent(QEvent)
        # print(self, "RELEASE_EVENT")
