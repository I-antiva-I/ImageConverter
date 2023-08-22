from typing import TypedDict

from components.MyPushButton import MyPushButton
from components.MyFormatSelector import MyFormatSelector
from components.MyPathSelector import MyPathSelector
from components.MyCheckBox import MyCheckBox
from components.MyStatusLabel import MyStatusLabel
from components.MyPanelLabeled import MyPanelLabeled


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
    # Panels
    PANEL_DESTINATION:          MyPanelLabeled

