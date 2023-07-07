from tkinter import *

from PIL import ImageTk, Image

class MyCheckbox(Frame):
    def __init__(self,
                 master,
                 callback=None,
                 default_state=False,
                 text="Check Box",
                ):

        # (?) Frame
        super().__init__(master)
        self["padx"] =                  2
        self["pady"] =                  2
        self["background"] =            "seagreen" if default_state else "dimgray"
        self["height"] =                36
        self.pack_propagate(0)

        # (?) Checkbox
        self.var =                              BooleanVar(self, default_state)
        self.checkbox =                         Checkbutton(self, variable=self.var, command=self.on_click)
        self.checkbox["anchor"]=                W
        self.checkbox["text"]=                  text
        self.checkbox["font"]=                  "Segoe_UI 9 bold italic" if default_state else "Segoe_UI 9 bold"
        self.checkbox["background"] =           "mediumseagreen" if default_state else "silver"
        self.checkbox["activebackground"] =     "mediumseagreen" if default_state else "silver"
        self.checkbox["selectcolor"] =          "white"
        self.checkbox["cursor"] =               "hand2"
        self.icon=                              None

        # (?) Placement
        self.checkbox.pack(side=LEFT, fill=BOTH, expand=1)

        # (?) Events
        self.checkbox.bind("<Enter>", lambda event: self.on_hover(event))
        self.checkbox.bind("<Leave>", lambda event: self.on_leave(event))



        self.callback=callback

    def change_text(self,new_text):
        self.checkbox["text"] = new_text

    def on_hover(self, event):
        self.checkbox["background"] = "dodgerblue"
        self["background"] = "royalblue"

    def on_leave(self, event):
        if self.var.get():
            self.checkbox["background"] =       "mediumseagreen"
            self["background"] =                "seagreen"
        else:
            self.checkbox["background"] =       "silver"
            self["background"] =                "dimgray"



    def on_click(self):
        if callable(self.callback):
            print("CLICK CALLBACK")
            self.callback()

        if self.var.get():
            self.checkbox["font"] =             "Segoe_UI 9 bold italic"
            self.checkbox["background"] =       "mediumseagreen"
            self.checkbox["activebackground"] = "mediumseagreen"
            self["background"] =                "seagreen"
        else:
            self.checkbox["font"] =             "Segoe_UI 9 bold"
            self.checkbox["background"] =       "silver"
            self.checkbox["activebackground"] = "silver"
            self["background"] =                "dimgray"