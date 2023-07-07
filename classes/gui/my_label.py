
from tkinter import *
from tkinter import font as tk_font


class MyLabel(Frame):
    def __init__(self,
                 master,
                 border_width=0,
                 width=40,
                 height=20,
                 border_color="#424242",
                 background="#424242",
                 padding=1,
                 anchor=W,
                 text="Label",
                 color="white",
                 font="Segoe_UI 9 normal",
                 ):

        # (?) Frame
        super().__init__(master)
        self["padx"] =                  border_width
        self["pady"] =                  border_width
        self["background"] =            border_color

        # (?) Label
        self.label=Label(self)
        self.label["padx"] =            padding
        self.label["font"] =            font
        self.label["anchor"] =          anchor
        self.label["text"] =            text
        self.label["background"] =      background
        self.label["foreground"] =      color

        self.adjust_width(width)
        self.adjust_height(height)

        # (?) Placement of Label
        self.pack_propagate(0)  # This method prevents the resizing of frame
        self.label.pack(fill=BOTH, expand=1)

    def change_text(self, text, font=None, color=None):
        self.label["text"] = text

        if font is not None:
            self.label["font"] = font

        if color is not None:
            self.label["foreground"] = color

        self.adjust_width()
        self.adjust_height()

    def adjust_width(self, preferred_width=0):
        # (?) According to FONT measure WIDTH required for TEXT + add PADDING from BOTH sides
        required_width= (tk_font.Font(font=self.label["font"])).measure(self.label["text"]) + self.label["padx"]*2
        self["width"]= max(required_width,preferred_width)

    def adjust_height(self, preferred_height=0):
        # (?) According to FONT get METRICS where LINESPACE is maximal height in pixels
        required_height=tk_font.Font(font=self.label["font"]).metrics()["linespace"]
        self["height"] = max(required_height, preferred_height)