from PyQt5 import QtCore, QtGui, QtWidgets

from components.MyIcon import MyIcon
from components.MyLabel import MyLabel
from components.MyPanel import MyPanel
from components.MyWidgetWithLayout import MyWidgetWithLayout


class MyCheckBox(MyPanel):
    def __init__(self, name=None, text="Some Text", iconPath=None, initialState=False):
        super(MyCheckBox, self).__init__(name, QtWidgets.QHBoxLayout())

        # Icon
        self.icon = MyIcon(iconPath, 28+4+2, 4, 2)
        self.place(self.icon)

        # Label
        self.label = MyLabel(text)
        self.label.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.place(self.label)

        # Current state
        self.currentState = initialState

        # Property for CSS
        self.setProperty("currentState", initialState)

        # Cursor shape
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

        # OnClick callback function
        self.onClickFunction = None

    def updateIcon(self, path):
        self.icon.updateIcon("./images/warning.ico")

    # Update property and recompute CSS
    def updateCurrentState(self, value):
        self.currentState = value
        self.setProperty("currentState", value)
        self.setStyleSheet(self.styleSheet())

    # Mouse events
    def enterEvent(self, QEvent):
        super().enterEvent(QEvent)
        # Some action here

    def leaveEvent(self, QEvent):
        super().leaveEvent(QEvent)
        # Some action here

    def mousePressEvent(self, QEvent):
        super().mousePressEvent(QEvent)
        # Click via left button
        if QEvent.button() == 1:
            self.updateCurrentState(not self.currentState)
            if callable(self.onClickFunction):
                self.onClickFunction()

    def mouseReleaseEvent(self, QEvent):
        super().mouseReleaseEvent(QEvent)
        # Some action here
