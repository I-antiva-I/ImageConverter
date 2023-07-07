from tkinter import *


class MyButton(Button):
    def __init__(self,
                 master,
                 callback=None,
                 text="Press Me",
                 font="Segoe_UI 9 bold"
                 ):
        super().__init__(master)
        self.callback=callback
        self["text"]=                text
        self["cursor"]=              "hand2"
        self["font"]=                font
        self["command"] =            self.on_button_pressed
        self["background"] =         "white"
        self["foreground"] =         "black"
        self["activebackground"] =   "royalblue"
        self["activeforeground"] =   "black"
        self["borderwidth"] =        0
        self["relief"] =             FLAT
        # (?) Events
        self.bind("<Enter>", lambda event: self.on_button_hover(event))
        self.bind("<Leave>", lambda event: self.on_button_leave(event))

    def on_button_hover(self, event):
        self["background"] = "dodgerblue"
        self["foreground"] = "white"

    def on_button_leave(self, event):
        self["background"] = "white"
        self["foreground"] = "black"

    def on_button_pressed(self):
        if callable(self.callback):
            self.callback()
