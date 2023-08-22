from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QComboBox, QSizePolicy

from components.MyCheckBox import MyCheckBox
from components.MyFormatSelector import MyFormatSelector
from components.MyLabel import MyLabel
from components.MyPanel import MyPanel
from components.MyPanelLabeled import MyPanelLabeled
from components.MyPathSelector import MyPathSelector
from components.MyPushButton import MyPushButton
from components.MyStatusLabel import MyStatusLabel

from utility.core import applyCSS
from utility.types import MainWindowComponents


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
        self.resize(900, 450)

        # MyPanel (Central Widget)
        self.mainPanel = MyPanel(name="MAIN_PANEL", layout=QtWidgets.QHBoxLayout())
        self.setCentralWidget(self.mainPanel)

        # CSS
        applyCSS(self)

        # Components
        self.components = None

        # Placement of all components
        self.placeComponents()

    def placeComponents(self):
        # [!] Some weird behaviour: a short delay before render if panels don't have child components
        #
        # (?) SizePolicy ------------------------------------------
        #   > QSizePolicy.Fixed
        #       * The sizeHint() is the only acceptable alternative, so the widget can never grow or shrink
        #   > QSizePolicy.Minimum
        #       * The sizeHint() is minimal, and sufficient. The widget can be expanded,
        #       but there is no advantage to it being larger (e.g. the horizontal direction of a push button).
        #       It cannot be smaller than the size provided by sizeHint().
        #   > QSizePolicy.Maximum
        #       * The sizeHint() is a maximum. The widget can be shrunk any amount
        #       without detriment if other widgets need the space (e.g. a separator line).
        #       It cannot be larger than the size provided by sizeHint()
        #   > QSizePolicy.Preferred
        #       * The sizeHint() is best, but the widget can be shrunk and still be useful.
        #       The widget can be expanded, but there is no advantage to
        #       it being larger than sizeHint() (the default QWidget policy).
        #   > QSizePolicy.Expanding
        #       * The sizeHint() is a sensible size, but the widget can be shrunk
        #       and still be useful. The widget can make use of extra space, so
        #       it should get as much space as possible
        #       (e.g. the horizontal direction of a horizontal slider).
        #   > QSizePolicy.MinimumExpanding
        #       * The sizeHint() is minimal, and sufficient.
        #       The widget can make use of extra space,
        #       so it should get as much space as possible
        #       (e.g. the horizontal direction of a horizontal slider).
        #   > QSizePolicy.Ignored
        #       * The sizeHint() is ignored. The widget will get as much space as possible.
        # ---------------------------------------------------------

        # Panel with options
        panelOptions = MyPanelLabeled(name="PANEL_OPTIONS", label="Options", layout=QtWidgets.QVBoxLayout())
        panelOptions.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        panelOptions.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        # Checkboxes for options
        checkboxConvertAll = MyCheckBox(text="Convert entire directory",
                                        iconPath="./images/checkboxes/entire.svg",
                                        initialState=True)
        checkboxDifferentOutput = MyCheckBox(text="Different output directory",
                                             iconPath="./images/checkboxes/different.svg",
                                             initialState=False)
        checkboxReplaceConflicts = MyCheckBox(text="Replace conflicting file",
                                              iconPath="./images/checkboxes/replace.svg",
                                              initialState=False)
        checkboxDeleteOriginals = MyCheckBox(text="Delete original file",
                                             iconPath="./images/checkboxes/delete.svg",
                                             initialState=False)
        # Placement of checkboxes
        panelOptions.placeAll(checkboxConvertAll,
                              checkboxDifferentOutput,
                              checkboxReplaceConflicts,
                              checkboxDeleteOriginals)

        # Panel with "conversion" widgets
        panelConversion = MyPanelLabeled(name="PANEL_CONVERSION", label="Convert", layout=QtWidgets.QVBoxLayout())
        panelConversion.layout().setSpacing(0)

        # Format selector
        panelFormats = MyPanelLabeled(name="PANEL_FORMATS", label="Formats")
        panelFormats.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        formatSelector = MyFormatSelector()
        panelFormats.place(formatSelector)

        # Path to source folder
        panelPathSource = MyPanelLabeled(name="PANEL_SOURCE", label="Source", layout=QtWidgets.QVBoxLayout())
        panelPathSource.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        pathSelectorSource = MyPathSelector()
        panelPathSource.place(pathSelectorSource)

        # Path to destination folder
        panelPathDestination = MyPanelLabeled(name="PANEL_DESTINATION", label="Destination", layout=QtWidgets.QVBoxLayout())
        panelPathDestination.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        pathSelectorDestination = MyPathSelector()
        panelPathDestination.place(pathSelectorDestination)

        # Separator - space between status + convert button and other components
        separator = MyPanel()
        separator.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        #  Panel with "convert" button and status panel
        panelControl = MyPanel(name="PANEL_CONTROL", layout=QtWidgets.QHBoxLayout())
        panelControl.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        # Convert button
        buttonConvert = MyPushButton(name="BUTTON_CONVERT", text=" Convert", iconPathDefault="./images/buttons/convert.svg")
        buttonConvert.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        # Status panel
        panelStatus = MyPanelLabeled(name="PANEL_STATUS", label="Status", layout=QtWidgets.QHBoxLayout())
        panelStatus.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        labelStatus = MyStatusLabel(text="Welcome!")
        # Placement
        panelStatus.place(labelStatus)
        panelControl.placeAll(panelStatus, buttonConvert)

        # Placement of "conversion" widgets
        panelConversion.placeAll(panelFormats,
                                 panelPathSource,
                                 panelPathDestination,
                                 separator,
                                 panelControl)

        # Placement (panelOptions+panelConversion)
        self.mainPanel.placeAll(panelOptions, panelConversion)

        self.components: MainWindowComponents  = {
            # "Convert" components
            "BUTTON_CONVERT":   buttonConvert,
            "FORMAT_SELECTOR":  formatSelector,
            "PATH_SOURCE":      pathSelectorSource,
            "PATH_DESTINATION": pathSelectorDestination,
            "LABEL_STATUS":     labelStatus,
            # "Options" components
            "OPTION_CONVERT_ALL":       checkboxConvertAll,
            "OPTION_DELETE_ORIGINALS":  checkboxDeleteOriginals,
            "OPTION_REPLACE_CONFLICTS": checkboxReplaceConflicts,
            "OPTION_DIFFERENT_OUTPUT":  checkboxDifferentOutput,
            # Panels
            "PANEL_DESTINATION": panelPathDestination,
        }

