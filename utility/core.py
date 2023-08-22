import json
import re

from PyQt5.QtWidgets import QWidget


def filterStings(pattern, strings):
    return filter(re.compile(pattern).match, strings)


def applyCSS(widget: QWidget):
    # File (.css) that contains css rules (color: @example)
    pathToCSS = "./css/styles.css"
    # File (.json) that contains variables ("@example": "#000000")
    pathToJSON = "./css/variables.json"

    stringCSS = open(pathToCSS, "r").read()
    dataVars: dict = json.load(open(pathToJSON))

    for key, value in dataVars.items():
        stringCSS = stringCSS.replace(key, value)

    widget.setStyleSheet(stringCSS)

