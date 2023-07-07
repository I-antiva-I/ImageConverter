import tkinter as tk
from tkinter import *

from classes.gui.my_label import MyLabel
from utility import available_formats as af


class MyFormats(Frame):
    def __init__(self, master):

        # (?) Frame
        super().__init__(master)
        self["background"] = "#424242"
        self["height"] = 48
        self["padx"] = 24
        #

        # (?) Menu From
        self.selected_format_from = StringVar(self, "FROM")                 # (?) Stores KEY
        self.formats_from = OptionMenu(self, self.selected_format_from, *[None])
        self.formats_from["font"] = "Segoe_UI 9 bold"
        self.formats_from["cursor"] = "hand2"
        self.formats_from["menu"]["activebackground"] = "#424242"
        self.formats_from["background"] = "white"
        self.formats_from["activebackground"] = "dodgerblue"
        self.formats_from["activeforeground"] = "white"
        self.formats_from["indicatoron"] = 0
        self.formats_from["highlightthickness"] = 0
        self.formats_from["relief"] = FLAT
        self.formats_from["borderwidth"] = 0

        # (?) Menu To
        self.selected_format_to = StringVar(self, "TO")                     # (?) Stores KEY
        self.formats_to = OptionMenu(self, self.selected_format_to, *[None])
        self.formats_to["font"] = "Segoe_UI 9 bold"
        self.formats_to["cursor"] = "hand2"
        self.formats_to["menu"]["activebackground"] = "#424242"
        self.formats_to["background"] = "white"
        self.formats_to["activebackground"] = "dodgerblue"
        self.formats_to["activeforeground"] = "white"
        self.formats_to["indicatoron"] = 0
        self.formats_to["highlightthickness"] = 0
        self.formats_to["relief"] = FLAT
        self.formats_to["borderwidth"] = 0

        self.label_from = MyLabel(self,
                                  text="Convert from",
                                  font="Segoe_UI 9 bold italic",
                                  color="silver",
                                  )

        self.label_to = MyLabel(self,
                                text="Convert to",
                                font="Segoe_UI 9 bold italic",
                                color="silver",
                                )

        # (?) Placement
        self.label_from.place(relx=0, rely=0, relheight=0.48, relwidth=0.5)
        self.label_to.place(relx=0, rely=0.52, relheight=0.48, relwidth=0.5)
        self.formats_from.place(relx=0.55, rely=0, relheight=0.48, relwidth=0.45)
        self.formats_to.place(relx=0.55, rely=0.52, relheight=0.48, relwidth=0.45)

    # (?) Change state (NORMAL/DISABLED) and styles of To Menu
    def change_to_state(self, state):
        cur_state = True if self.formats_to["state"] == NORMAL else False
        if cur_state != state:
            if state:
                self.formats_to["state"] = NORMAL
                self.formats_to["background"] = "white"
                self.formats_to["cursor"] = "hand2"
            else:
                self.formats_to["state"] = DISABLED
                self.formats_to["background"] = "silver"
                self.formats_to["cursor"] = "arrow"

    # (?) Checks if To Menu has valid selected value
    def adjust_to(self):
        if not af.formats[self.selected_format_from.get()]["transformations"].__contains__(self.selected_format_to.get()):
            self.selected_format_to.set(af.formats[self.selected_format_from.get()]["transformations"][0])

    # (?) Restructure of menus
    # (?) Command for To Menu only changes variable
    # (?) Command for From Menu:
    #       changes variable,
    #       restructures To Menu,
    #       enables To Menu,
    #       checks if To var is valid,
    #       sets correct filetypes for searchbar
    def restructure_to_menu(self, menu_items):
        self.formats_to["menu"].delete("0", tk.END)
        for item in menu_items:
            self.formats_to["menu"].add_command(label=item, command=tk._setit(self.selected_format_to, item))


    def restructure_from_menu(self, menu_items, searchbar):     # (?) menu_items are keys of formats that can be transformed
        self.formats_from["menu"].delete("0", tk.END)
        for item in menu_items:
            self.formats_from["menu"].add_command(
                label=item,
                command=tk._setit(self.selected_format_from, item, lambda key:    # (?) key has a value of item
                [
                    self.restructure_to_menu(af.formats[key]["transformations"]),
                    self.change_to_state(True),
                    self.adjust_to(),
                    searchbar.update_filetypes((key, af.formats[key]["extensions"]))
                ]))
