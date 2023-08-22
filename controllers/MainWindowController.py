import glob
import json
import os
import re

from utility.core import filterStings
from utility.enums import StatusLabelColor, DialogMode
from utility.types import MainWindowComponents
import utility.validation as valid
import conversions


class MainWindowController:
    def __init__(self, components: MainWindowComponents):
        # Store components
        self.components = components
        self.availableFormats = {}

    # Initial preparations
    def setup(self):
        # Read file (.json) that contains all available formats
        pathToJSON = "./formats.json"
        self.availableFormats: dict = json.load(open(pathToJSON))

        # Initial states of components
        self.components["FORMAT_SELECTOR"].setStateComboBoxOriginal(True)
        self.components["FORMAT_SELECTOR"].setStateComboBoxTarget(True)
        self.components["PANEL_DESTINATION"].setVisible(False)

        # Set availableFormats (FORMAT_SELECTOR)
        for key, value in self.availableFormats.items():
            self.components["FORMAT_SELECTOR"].availableFormats[key] = value.get("transformations", [])

        # Fill combobox for original format (FORMAT_SELECTOR)
        self.components["FORMAT_SELECTOR"].fillComboBoxOriginal(self.availableFormats.keys())

        # Set plural/singular text and dialog mode
        if self.components["OPTION_CONVERT_ALL"].currentState :
            self.components["PATH_SOURCE"].setDialogMode(DialogMode.DIRECTORY)
            self.components["OPTION_DELETE_ORIGINALS"].label.changeText("Delete original files")
            self.components["OPTION_REPLACE_CONFLICTS"].label.changeText("Replace conflicting files")
        else:
            self.components["PATH_SOURCE"].setDialogMode(DialogMode.FILE)
            self.components["OPTION_DELETE_ORIGINALS"].label.changeText("Delete original file")
            self.components["OPTION_REPLACE_CONFLICTS"].label.changeText("Replace conflicting file")

        # Set correct extensions
        self.components["PATH_SOURCE"].resetNameFilterOptions(
            self.components["FORMAT_SELECTOR"].comboBoxOriginal.currentText(),
            self.availableFormats[self.components["FORMAT_SELECTOR"].comboBoxOriginal.currentText()]
                .get("extensions", None))

    # Connect functions
    def connectFunctions(self):
        # Plural/singular text and dialog mode change on click
        self.components["OPTION_CONVERT_ALL"].onClickFunction = (
            lambda:
            [
                self.components["PATH_SOURCE"].setDialogMode(DialogMode.DIRECTORY),
                self.components["OPTION_DELETE_ORIGINALS"].label.changeText("Delete original files"),
                self.components["OPTION_REPLACE_CONFLICTS"].label.changeText("Replace conflicting files")
            ]
            if self.components["OPTION_CONVERT_ALL"].currentState else
            [
                self.components["PATH_SOURCE"].setDialogMode(DialogMode.FILE),
                self.components["OPTION_DELETE_ORIGINALS"].label.changeText("Delete original file"),
                self.components["OPTION_REPLACE_CONFLICTS"].label.changeText("Replace conflicting file")
            ]
        )

        # Show/Hide panel (PANEL_DESTINATION) depending on option ("OPTION_DIFFERENT_OUTPUT)
        self.components["OPTION_DIFFERENT_OUTPUT"].onClickFunction = (
            lambda:
            self.components["PANEL_DESTINATION"].setVisible(
                self.components["OPTION_DIFFERENT_OUTPUT"].currentState)
        )

        # Reset name filter extensions on change of original combobox (FORMAT_SELECTOR)
        self.components["FORMAT_SELECTOR"].comboBoxOriginal.currentIndexChanged.connect(
            lambda:
            self.components["PATH_SOURCE"].resetNameFilterOptions(
                self.components["FORMAT_SELECTOR"].comboBoxOriginal.currentText(),
                self.availableFormats[self.components["FORMAT_SELECTOR"].comboBoxOriginal.currentText()].
                get("extensions", None)
            )
        )

        # Connect convert button
        self.components["BUTTON_CONVERT"].clicked.connect(self.onConvertClicked)

    # Perform conversion
    def onConvertClicked(self):

        # Formats
        originalFormat = self.components["FORMAT_SELECTOR"].comboBoxOriginal.currentText()
        targetFormat = self.components["FORMAT_SELECTOR"].comboBoxTarget.currentText()

        # Options
        isConvertingEntireDirectory = self.components["OPTION_CONVERT_ALL"].currentState
        isUsingDifferentOutputDirectory = self.components["OPTION_DIFFERENT_OUTPUT"].currentState
        isReplacingConflicts =  self.components["OPTION_REPLACE_CONFLICTS"].currentState
        isDeletingOriginals = self.components["OPTION_DELETE_ORIGINALS"].currentState

        # Paths
        pathToSource = self.components["PATH_SOURCE"].pathLineEdit.text()
        pathToDestination = self.components["PATH_DESTINATION"].pathLineEdit.text()

        print("CONVERT CHECKING")
        # --------------------
        print(f'''
        CONVERT: {originalFormat} --> {targetFormat}
        OPTIONS:
        \tisConvertingEntireDirectory? {isConvertingEntireDirectory}
        \tisUsingDifferentOutputDirectory? {isUsingDifferentOutputDirectory}
        \tisReplacingConflicts? {isReplacingConflicts}
        \tisDeletingOriginals? {isDeletingOriginals}
        SOURCE: {pathToSource}
        DESTINATION: {pathToDestination}
                ''')
        # --------------------

        # Validation: existence of source directory
        if isConvertingEntireDirectory:
            isValid = valid.checkIfDirectoryExists(pathToSource)
            if not isValid:
                self.components["LABEL_STATUS"].updateLabel(
                    "Selected source directory doesn't exists", StatusLabelColor.ERROR)
                return
        # Validation: existence of source file
        else:
            isValid = valid.checkIfFileExists(pathToSource)
            if not isValid:
                self.components["LABEL_STATUS"].updateLabel(
                    "Selected source file doesn't exists", StatusLabelColor.ERROR)
                return
            # Validation: extension of file
            isValid = valid.checkFileExtension(pathToSource, self.availableFormats[originalFormat]["extensions"])
            if not isValid:
                self.components["LABEL_STATUS"].updateLabel(
                    "Selected source file has incorrect extension", StatusLabelColor.ERROR)
                return

        # Validation: existence of destination directory
        if isUsingDifferentOutputDirectory:
            isValid = valid.checkIfDirectoryExists(pathToDestination)
            if not isValid:
                self.components["LABEL_STATUS"].updateLabel(
                    "Selected destination directory doesn't exists", StatusLabelColor.ERROR)
                return

        self.components["LABEL_STATUS"].updateLabel("All's well", StatusLabelColor.INFORMATION)


        print("CONVERT START")

        if isConvertingEntireDirectory:
            print("Converting directory...")
            self.convertAll(pathToSource, self.availableFormats[originalFormat]["extensions"], targetFormat)
        else:
            print("Converting file...")
            self.convertOne(pathToSource, targetFormat)

    def convertAll(self, pathToSource, extensions, targetFormat):
        # Regular expression
        # [!] RegEx must be valid
        pattern = ".*"
        for extension in extensions:
            pattern += f"(\\{extension}) |"
        pattern = pattern.strip(" |")

        # Go through all files with valid extensions
        files = list(filterStings(pattern, os.listdir(pathToSource)))
        filesTotal = len(files)
        # No files found
        if filesTotal == 0:
            self.components["LABEL_STATUS"].updateLabel(
                "No suitable files found in selected directory", StatusLabelColor.WARNING)
            return
        # Convert found files
        else:
            filesConverted = 0
            for filename in files:
                print("[>]", pathToSource+"/"+filename)
                # Perform conversion
                self.convertOne(pathToSource+"/"+filename, targetFormat)
                # Output information
                filesConverted = filesConverted + 1
                self.components["LABEL_STATUS"].updateLabel(
                    f"Converting ({filesConverted}/{filesTotal})", StatusLabelColor.INFORMATION)



    def convertOne(self, pathToImage, targetFormat):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        # Vars
        imageName, imageExtension = os.path.splitext(pathToImage)
        imageName = os.path.basename(imageName)
        savePath =  os.path.dirname(pathToImage)
        newExtension = self.availableFormats[targetFormat]["extensions"][0]

        # REMOVES ORIG ??????????????

        print("SINGLE CONVERT CHECKING")
        # --------------------
        print(f'''
        CONVERTING: {imageName} | {imageExtension}
        DATA:
        \tTarget? {targetFormat}
        \tPath to IMG (FILE)? {pathToImage}
        \tSave Path (DIR)? {savePath}
        \tNew Extension? {newExtension}
                ''')
        # --------------------

        # Image
        openedImage = conversions.openImage(pathToImage)
        conversions.saveImage(openedImage, imageName, imageExtension, newExtension, savePath)

