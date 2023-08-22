from enum import Enum


class DialogMode(Enum):
    DIRECTORY = 0
    FILE = 1


class StatusLabelColor(Enum):
    DEFAULT =       "#FFFFFF"       # white
    INFORMATION =   "#1E90EE"       # blue
    SUCCESS =       "#3CB371"       # green
    WARNING =       "#EEC700"       # yellow
    ERROR =         "#EE0000"       # red

