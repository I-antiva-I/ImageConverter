from tkinter import *
from tkinter import filedialog

from classes.gui.my_button import MyButton





class MySearchbar(Frame):
    def __init__(self, master, callback=None):

        # (?) Frame
        super().__init__(master)
        self["padx"] =                  5
        self["pady"] =                  5
        self["height"] =                38
        self["background"] =            "#424242"

        self.file_dialog_button =               MyButton(self)
        self.file_dialog_button["text"] =       "Select"
        self.file_dialog_button["command"] =    self.on_click
        self.directory_mode =                   BooleanVar(self,True)

        self.input_field_text = StringVar(self, "")
        self.filetypes = [("All files", "")]

        self.input_field =                      Entry(self)
        self.input_field["textvariable"]=       self.input_field_text
        self.input_field["font"] =              "Segoe_UI 9 normal italic"
        self.input_field["borderwidth"] =       4
        self.input_field["relief"] =            FLAT
        self.input_field.insert(0,"Select or Insert path")

        # (?) Placement
        self.file_dialog_button.place(x=0,y=0,relwidth=0.2,relheight=1)
        self.input_field.place(relx=0.25,y=0,relwidth=0.75,relheight=1)

        self.callback= callback

    def update_filetypes(self, item):   # (?) Only two options: 1st - All files, 2nd - Selected extension
        if len(self.filetypes) == 2:
            self.filetypes[1] = item
        else:
            self.filetypes.append(item)

    def on_click(self):
        if self.directory_mode.get():
            answer = filedialog.askdirectory()
        else:
            answer = filedialog.askopenfilename(filetypes=self.filetypes)
        self.input_field_text.set(answer)

        if not self.directory_mode.get():
            if callable(self.callback):
                self.callback()