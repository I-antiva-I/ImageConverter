
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QComboBox, QSizePolicy

from components.MyCheckBox import MyCheckBox
from components.MyFormatSelector import MyFormatSelector
from components.MyLabel import MyLabel
from components.MyPanel import MyPanel
from components.MyPanelLabeled import MyPanelLabeled
from components.MyPathSelector import MyPathSelector

from utility.core import applyCSS


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # The super function in Python takes two optional parameters:
        # 1st -  name of the subclass
        # 2nd -  object of the subclass
        super(MyMainWindow, self).__init__()

        # Main Window properties
        self.setObjectName("MAIN_WINDOW")
        self.setWindowTitle("Image Converter")

        # Size of Main Window
        self.resize(800, 600)

        # MyPanel (Central Widget)
        self.mainPanel = MyPanel(name="MAIN_PANEL", layout=QtWidgets.QHBoxLayout())
        self.setCentralWidget(self.mainPanel)

        # CSS
        applyCSS(self)

        # Placement of all components
        self.placeComponents()

    def placeComponents(self):
        # [!] Some weird behaviour: a short delay before render if panels don't have child components
        panelOptions = MyPanelLabeled(name="PANEL_OPTIONS", label="Options", layout=QtWidgets.QVBoxLayout())
        panelConversion = MyPanelLabeled(name="PANEL_CONVERSION", label="Convert", layout=QtWidgets.QVBoxLayout())


        # Checkboxes
        checkboxConvertAll =        MyCheckBox(text="Convert entire directory",
                                               iconPath="./images/checkboxes/folder_entire.svg",
                                               defaultState=True)
        checkboxDifferentOutput =   MyCheckBox(text="Different output directory",
                                               iconPath="./images/checkboxes/folder_destination.svg",
                                               defaultState=False)
        checkboxReplaceConflicts =  MyCheckBox(text="Replace conflicting file",
                                               iconPath="./images/checkboxes/file_replace.svg",
                                               defaultState=False)
        checkboxDeleteOriginals =   MyCheckBox(text="Delete original file",
                                               iconPath="./images/checkboxes/delete.svg",
                                               defaultState=False)

        # Placement
        panelOptions.setMaximumWidth(320)
        panelOptions.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        panelOptions.placeAll(checkboxConvertAll,
                              checkboxDifferentOutput,
                              checkboxReplaceConflicts,
                              checkboxDeleteOriginals)

        # Formats
        panelFormats = MyPanelLabeled(name="PANEL_FORMATS", label="Formats", layout=QtWidgets.QHBoxLayout())
        panelFormats.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        selectorFormats = MyFormatSelector()
        panelFormats.place(selectorFormats)

        # Path to source folder
        panelPathSource = MyPanelLabeled(name="PANEL_SOURCE", label="Source", layout=QtWidgets.QVBoxLayout())
        panelPathSource.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        selectorSource = MyPathSelector(layout=QtWidgets.QHBoxLayout())
        panelPathSource.place(selectorSource)

        # Path to destination folder
        panelPathDestination = MyPanelLabeled(name="PANEL_DESTINATION", label="Destination", layout=QtWidgets.QVBoxLayout())
        panelPathDestination.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        selectorDestination = MyPathSelector(layout=QtWidgets.QHBoxLayout())
        panelPathDestination.place(selectorDestination)

        # Placeholder
        placeholder = MyPanel()

        # Status
        panelStatus = MyPanelLabeled(name="PANEL_STATUS", label="Status", layout=QtWidgets.QHBoxLayout())
        panelStatus.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        labelStatus = MyLabel()
        panelStatus.place(labelStatus)

        # Conversion placement
        panelConversion.placeAll(panelFormats, panelPathSource, panelPathDestination, placeholder, panelStatus)

        # Main panel Placement
        self.mainPanel.placeAll(panelOptions, panelConversion)

