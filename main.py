# (?) Imports
import ctypes
from tkinter import *

from classes.controller import Controller
from utility.setup_gui import prepare as prepare_gui
from utility.setup_logic import prepare as prepare_logic


def launch():
    ctypes.windll.shcore.SetProcessDpiAwareness(1)

    root = Tk()
    controller = Controller()

    prepare_logic(prepare_gui(root),controller)

    root.mainloop()


if __name__ == '__main__':
    launch()
