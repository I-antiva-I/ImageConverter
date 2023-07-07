from tkinter import *


class MyFrame(Frame):
    def __init__(self, master, width):

        # (?) Frame
        super().__init__(master)
        self["borderwidth"] =           2
        self["relief"] =                GROOVE
        self["padx"] =                  10
        self["pady"] =                  10
        self["width"] =                 width
        self["height"] =                360
        self["background"] =            "#424242"