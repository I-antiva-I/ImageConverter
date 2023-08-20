from PyQt5 import QtWidgets

from .MyLabel import MyLabel
from .MyPanel import MyPanel
from .MyWidgetWithLayout import MyWidgetWithLayout


class MyFormatSelector(MyPanel):
    def __init__(self, name=None):
        super(MyFormatSelector, self).__init__(name, QtWidgets.QGridLayout())

        # Combo boxes for formats
        comboBoxOriginal = QtWidgets.QComboBox()
        comboBoxTarget = QtWidgets.QComboBox()

        # Labels for formats
        labelOriginal = MyLabel("Original format")
        labelTarget = MyLabel("Target format")

        # Combo boxes items TEMP
        comboBoxOriginal.addItem("Alpha")
        comboBoxOriginal.addItem("Beta")
        comboBoxOriginal.addItem("Gamma")
        comboBoxOriginal.addItem("Delta")
        comboBoxOriginal.addItem("Epsilon")
        comboBoxTarget.addItem("Zetta")
        comboBoxTarget.addItem("Omega")
        comboBoxTarget.addItem("Lambda")
        comboBoxTarget.addItem("Theta")
        comboBoxTarget.addItem("Phi")

        # Placement
        self.place(labelOriginal,       1, 1, 1, 2)
        self.place(comboBoxOriginal,    1, 3, 1, 1)
        self.place(labelTarget,         2, 1, 1, 2)
        self.place(comboBoxTarget,      2, 3, 1, 1)


