from typing import TypedDict

from PyQt5.QtWidgets import QWidget

from components.MyPushButton import MyPushButton
from components.MyFormatSelector import MyFormatSelector
from components.MyPathSelector import MyPathSelector
from components.MyCheckBox import MyCheckBox
from components.MyStatusLabel import MyStatusLabel


class MainWindowComponents(TypedDict):
    # "Convert" components
    BUTTON_CONVERT:         MyPushButton
    FORMAT_SELECTOR:        MyFormatSelector
    PATH_SOURCE:            MyPathSelector
    PATH_DESTINATION:       MyPathSelector
    LABEL_STATUS:           MyStatusLabel
    # "Options" components
    OPTION_CONVERT_ALL:         MyCheckBox
    OPTION_DELETE_ORIGINALS:    MyCheckBox
    OPTION_REPLACE_CONFLICTS:   MyCheckBox
    OPTION_DIFFERENT_OUTPUT:    MyCheckBox
    # "Convert" panels
    PANEL_DESTINATION:          QWidget

