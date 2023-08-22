from PyQt5 import QtCore, QtGui, QtWidgets


class MyPushButton(QtWidgets.QPushButton):
    def __init__(self, name=None, text=None, iconPathDefault=None, iconPathHovered=None, iconPathPressed=None):
        super(MyPushButton, self).__init__()

        if name is not None:
            self.setObjectName(name)

        if text is None:
            self.setText("My Button")
        else:
            self.setText(text)

        # Paths to icons
        self.iconPathDefault =  iconPathDefault
        self.iconPathHovered =  iconPathHovered
        self.iconPathPressed =  iconPathPressed

        # Cursor shape
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

        # Default icon
        self.prepareIcon(iconPathDefault)

    def enterEvent(self, QEvent):
        super().leaveEvent(QEvent)
        self.prepareIcon(self.iconPathHovered)

    def leaveEvent(self, QEvent):
        super().leaveEvent(QEvent)
        self.prepareIcon(self.iconPathDefault)

    def mousePressEvent(self, QEvent):
        super().mousePressEvent(QEvent)
        # Click via left button
        if QEvent.button() == 1:
            self.prepareIcon(self.iconPathPressed)

    def mouseReleaseEvent(self, QEvent):
        super().mouseReleaseEvent(QEvent)
        self.prepareIcon(self.iconPathDefault)

    def prepareIcon(self, path):
        if path is not None:
            icon = QtGui.QIcon(path)
            self.setIcon(icon)
            self.setIconSize(QtCore.QSize(24, 24))

    def prepareIcon(self, path):
        if path is not None:
            icon = QtGui.QIcon(path)
            self.setIcon(icon)
            self.setIconSize(QtCore.QSize(28, 28))
