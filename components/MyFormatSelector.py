from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSizePolicy

from .MyLabel import MyLabel
from .MyPanel import MyPanel


class MyFormatSelector(MyPanel):
    def __init__(self, name=None):
        super(MyFormatSelector, self).__init__(name, QtWidgets.QGridLayout())

        # Combo boxes for formats
        self.comboBoxOriginal = QtWidgets.QComboBox()
        self.comboBoxTarget = QtWidgets.QComboBox()

        # Size policies
        self.comboBoxOriginal.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.comboBoxTarget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        # Connect onChanged for comboBoxOriginal
        self.comboBoxOriginal.currentIndexChanged.connect(self.onComboBoxOriginalChanged)

        # Labels for formats
        labelOriginal = MyLabel("Original format")
        labelTarget = MyLabel("Target format")

        # Available formats (keys for comboBoxOriginal, values for comboBoxTarget)
        self.availableFormats = {}

        # Placement of components
        self.place(labelOriginal,               1, 1, 1, 2)
        self.place(self.comboBoxOriginal,       1, 3, 1, 1)
        self.place(labelTarget,                 2, 1, 1, 2)
        self.place(self.comboBoxTarget,         2, 3, 1, 1)

        # Default state
        self.comboBoxTarget.setEnabled(False)

    # ComboBoxOriginal functions
    def clearComboBoxOriginal(self):
        self.comboBoxOriginal.clear()

    def setStateComboBoxOriginal(self, state: bool):
        self.comboBoxOriginal.setEnabled(state)

    def fillComboBoxOriginal(self, items):
        self.comboBoxOriginal.addItems(items)

    def onComboBoxOriginalChanged(self):
        self.clearComboBoxTarget()
        self.fillComboBoxTarget(self.availableFormats[self.comboBoxOriginal.currentText()])

    # ComboBoxTarget functions
    def clearComboBoxTarget(self):
        self.comboBoxTarget.clear()

    def setStateComboBoxTarget(self, state: bool):
        self.comboBoxTarget.setEnabled(state)

    def fillComboBoxTarget(self, items):
        self.comboBoxTarget.addItems(items)






