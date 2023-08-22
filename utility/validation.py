import os


def checkIfFileExists(path):
    return os.path.isfile(path)


def checkIfDirectoryExists(path):
    return os.path.isdir(path)


def checkFileExtension(filename, allowed_extensions):
    extension = os.path.splitext(filename)[1]
    return allowed_extensions.__contains__(extension)
