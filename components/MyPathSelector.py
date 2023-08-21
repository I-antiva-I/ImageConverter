import pyperclip

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QFileDialog

from .MyPanel import MyPanel
from .MyPushButton import MyPushButton
from utility.enums import DialogMode


class MyPathSelector(MyPanel):
    def __init__(self, name=None, dialogMode=DialogMode.FILE):
        super(MyPathSelector, self).__init__(name, layout=QtWidgets.QHBoxLayout())

        # File dialog button
        self.dialogMode = dialogMode
        self.dialogButton = MyPushButton(text="Path")
        self.dialogButton.clicked.connect(self.onDialogButtonClicked)
        self.nameFilterOptions = ""

        # Controls for line edit
        clearButton = MyPushButton(text="DELETE")
        pasteButton = MyPushButton(text="PASTE")
        clearButton.clicked.connect(self.onClearButtonClicked)
        pasteButton.clicked.connect(self.onPasteButtonClicked)

        # Path line edit
        self.pathLineEdit = QLineEdit()
        self.pathLineEdit.textChanged.connect(self.onPathEditLineChanged)
        self.pathLineEdit.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)

        # Placement
        self.placeAll(self.dialogButton, self.pathLineEdit, clearButton, pasteButton)

    def resetNameFilterOptions(self, label, extensions):
        if extensions is None:
            self.nameFilterOptions = "Any (*);;"
        else:
            options = f"{label} ("
            for extension in extensions:
                options += "*"+extension+" "
            options += ");;"

            self.nameFilterOptions = options

    def onClearButtonClicked(self):
        self.pathLineEdit.setText("")

    def onPasteButtonClicked(self):
        text = pyperclip.paste()
        if text != "":
            self.pathLineEdit.setText(text)
        else:
            self.pathLineEdit.setText("?")

    def onPathEditLineChanged(self):
        print(">", self.pathLineEdit.displayText())

    def onDialogButtonClicked(self):
        # Create file dialog
        dialog = QFileDialog(self)

        # Select dialog mode (directory/file)
        if self.dialogMode == DialogMode.DIRECTORY:
            dialog.setFileMode(QFileDialog.FileMode.DirectoryOnly)
        elif self.dialogMode == DialogMode.FILE:
            dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
            dialog.setNameFilter(self.nameFilterOptions+"All (*)")
        else:
            return

        # More detailed view
        dialog.setViewMode(QFileDialog.ViewMode.Detail)

        dialogPath = ""
        # Open dialog window and select path
        if dialog.exec():
            dialogPath = dialog.selectedFiles()[0]

        print(dialogPath)
        self.pathLineEdit.setText(dialogPath)

