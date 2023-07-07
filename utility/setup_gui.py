from tkinter import *

from classes.gui.my_button import MyButton
from classes.gui.my_checkbox import MyCheckbox
from classes.gui.my_formats import MyFormats
from classes.gui.my_frame import MyFrame
from classes.gui.my_frame_labeled import MyFrameLabeled
from classes.gui.my_label import MyLabel
from classes.gui.my_searchbar import MySearchbar


def prepare(root):
    root.title("Image Converter")
    root.wm_attributes('-transparentcolor', '#000001')
    root.iconbitmap("images/app_icon.ico")
    root.geometry("{}x{}+{}+{}".format(
        640,
        360,
        root.winfo_screenwidth()  // 2 - 640  // 2,
        root.winfo_screenheight() // 2 - 360  // 2
    ))
    root.resizable(False,False)

    # (?) Default font for all child elements
    root.option_add("*Font", "Segoe_UI 9 normal")

    # (?) Main containers
    frame_options=MyFrame(root,(640*6.5)//16)
    frame_convert=MyFrame(root,(640*9.5)//16)
    frame_options.place(x=0, y=0)
    frame_convert.place(x=frame_options["width"],y=0)

    # (?) Headers for main containers
    fo_header=MyLabel(frame_options,
                      text="Options",
                      color="dodgerblue",
                      border_color="royalblue",
                      border_width=4,
                      width=170,
                      height=40,
                      padding=8,
                      font="Segoe_UI 15 bold"
                      )
    fc_header=MyLabel(frame_convert,
                      text="Convert",
                      color="dodgerblue",
                      border_color="royalblue",
                      border_width=4,
                      width=170,
                      height=40,
                      padding=8,
                      font="Segoe_UI 15 bold"
                      )
    fo_header.place(x=0, y=0)
    fc_header.place(x=0, y=0)

    # (?) Options
    option_all_dir = MyCheckbox(frame_options,
                                default_state=True,
                                text="Convert entire directory",
                                )
    option_out_log = MyCheckbox(frame_options,
                                text="Create output log",
                                )
    option_out_dir = MyCheckbox(frame_options,
                                text="Different output directory"
                                )
    option_delete = MyCheckbox(frame_options,
                               text="Delete original file",
                                )
    option_replace = MyCheckbox(frame_options,
                                text="Replace conflicting file",
                                )
    place_vertically([option_all_dir,option_out_dir,option_out_log,option_replace,option_delete],
                     offset=fo_header["height"]+20,
                     separator=8)

    # (?) Wrapper for Status container and Convert button 7
    wrapper=Frame(frame_convert,name="status_container")

    # (?) Containers with labels
    frame_formats = MyFrameLabeled(frame_convert,text="Formats")
    frame_search_from = MyFrameLabeled(frame_convert, text="Location From")
    frame_search_to = MyFrameLabeled(frame_convert, text="Location To")
    frame_status = MyFrameLabeled(wrapper, text="Status")

    # (?) Inner elements
    formats = MyFormats(frame_formats.body)
    searchbar_from = MySearchbar(frame_search_from.body)
    searchbar_to = MySearchbar(frame_search_to.body)
    status=MyLabel(frame_status.body,
                   text="Status...",
                   anchor=CENTER,
                   font="Segoe_UI 9 bold"
                   )
    button_convert=MyButton(wrapper,
                            text="Convert",
                            font="Segoe_UI 11 bold italic"
                            )

    # (?) Placement of Inner elements
    formats.place(x=0, y=0, relwidth=1)
    searchbar_from.place(x=0, y=0, relwidth=1)
    searchbar_to.place(x=0, y=0, relwidth=1)
    frame_status.place(x=0, y=0, relwidth=0.7,relheight=1)
    status.place(x=0, y=0, relwidth=1)
    button_convert.place(relx=0.75, y=12, relwidth=0.25,height=frame_status["height"])

    # (?) Container and Wrapper adjustment
    frame_formats.adjust_size()
    frame_search_from.adjust_size()
    frame_search_to.adjust_size()
    frame_status.adjust_size()
    wrapper["background"] = frame_convert["background"]
    wrapper["height"] = frame_status["height"]

    # (?) Placement of Containers
    place_vertically([frame_formats,frame_search_from,frame_search_to,wrapper],
                     offset=fc_header["height"]+8,
                     separator=4)

    # (?) All elements
    elements = {
        "option_all_dir":   option_all_dir,
        "option_replace":   option_replace,
        "option_delete":    option_delete,
        "option_out_dir":   option_out_dir,
        "option_out_log":   option_out_log,
        "formats":          formats,
        "search_from":      searchbar_from,
        "search_to":        searchbar_to,
        "container_from":   frame_search_from,
        "container_to":     frame_search_to,
        "status":           status,
        "button_convert":   button_convert,
    }
    return elements


def place_vertically(elements, offset=0,separator=0, relwidth=1):
    position=offset
    for element in elements:
        element.place(x=0,y=position,relwidth=relwidth)
        position=position+separator+element["height"]






