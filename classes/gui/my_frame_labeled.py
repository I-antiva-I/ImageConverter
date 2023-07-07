from tkinter import *

from classes.gui.my_label import MyLabel


class MyFrameLabeled(Frame):
    def __init__(self,
                 master,
                 text="Title",
                 height=32,
                 padding=8,
                ):
        # (?) Frame (Wrapper)
        super().__init__(master)
        self["height"] =                        height+12   # (?) Half of the Header
        self["background"] =                    "#424242"

        # (?) Body (Container)
        self.body=Frame(self)
        self.body["padx"] =                     padding
        self.body["pady"] =                     10          # (?) Half of the Header - Border Width
        self.body["height"] =                   height
        self.body["background"] =               "#424242"
        self.body["highlightbackground"] =      "dimgray"
        self.body["highlightthickness"] =       2           # (?) Border Width
        self.body.place(x=0, y=12, relwidth=1)

        # (?) Header
        self.header = MyLabel(self,
                              text=text,
                              height=24,
                              anchor=CENTER,
                              padding=16,
                              font="Segoe_UI 11 bold",
                              color="silver",
                              )
        self.header.place(x=42, y=0)

    def change_header_text(self,new_text):
        self.header.change_text(new_text)

    def adjust_size(self):
        height=0
        for child in list(self.body.children.values()):    # (?) List of child-elements
            height=height+child["height"]
        self.body["height"]=height+self.body["pady"]*2     # (?) Height of children + Padding
        self["height"]=self.body["height"]+12              # (?) Height of Body + Half of Header