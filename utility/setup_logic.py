from utility import available_formats as af
from utility import  validation_functions as vf

def prepare(elements, controller):
    """
option_all_dir   | .!myframe.!mycheckbox
option_replace   | .!myframe.!mycheckbox5
option_delete    | .!myframe.!mycheckbox4
option_out_dir   | .!myframe.!mycheckbox3
option_out_log   | .!myframe.!mycheckbox2
formats          | .!myframe2.!myframelabeled.!frame.!myformats
search_from      | .!myframe2.!myframelabeled2.!frame.!mysearchbar
search_to        | .!myframe2.!myframelabeled3.!frame.!mysearchbar
container_from   | .!myframe2.!myframelabeled2
container_to     | .!myframe2.!myframelabeled3
button_convert   | .!myframe2.status_container.!mybutton
    """

    # (?) Variables of options
    my_vars ={
        "option_all_dir": elements["option_all_dir"].var,
        "option_replace": elements["option_replace"].var,
        "option_delete":  elements["option_delete"].var,
        "option_out_dir": elements["option_out_dir"].var,
        "option_out_log": elements["option_out_log"].var,

        "format_from":    elements["formats"].selected_format_from,
        "format_to":      elements["formats"].selected_format_to,

        "path_from":      elements["search_from"].input_field_text,
        "path_to":        elements["search_to"].input_field_text,
    }
    print(my_vars)

    # (?) Initial Status
    elements["status"].change_text("Waiting...", None, "dodgerblue")

    # (?) Callback for "Different output directory" option
    def callback_option_out_dir():
        elements["container_to"].place(relwidth=my_vars["option_out_dir"].get(),
                                       height=elements["container_to"]["height"] * my_vars["option_out_dir"].get())
        elements["container_from"].change_header_text("Location"*(not my_vars["option_out_dir"].get())+
                                                      "Location From"*my_vars["option_out_dir"].get())
    elements["option_out_dir"].callback = callback_option_out_dir

    # (?) Set correct state according to "Different output directory" option
    elements["container_to"].place(relwidth=my_vars["option_out_dir"].get(),
                                   height=elements["container_to"]["height"] * my_vars["option_out_dir"].get())
    elements["container_from"].change_header_text("Location" * (not my_vars["option_out_dir"].get()) +
                                                  "Location From" * my_vars["option_out_dir"].get())

    # (?) Callback for "Convert entire directory" option
    def callback_option_all_dir():
        elements["option_delete"].change_text("Delete original file" + "s" * my_vars["option_all_dir"].get())
        elements["option_replace"].change_text("Replace conflicting file" + "s" * my_vars["option_all_dir"].get())
    elements["option_all_dir"].callback = callback_option_all_dir

    # (?) Set correct state according to "Convert entire directory" option
    elements["option_delete"].change_text("Delete original file" + "s" * my_vars["option_all_dir"].get())
    elements["option_replace"].change_text("Replace conflicting file" + "s" * my_vars["option_all_dir"].get())

    # (?) Assign directory mode to "Convert entire directory" option
    elements["search_from"].directory_mode=my_vars["option_all_dir"]
    # (?) Callback - automatic change of FROM format
    def callback_search_from():
        if vf.check_if_file_exists(my_vars["path_from"].get()):
            for key,val in af.formats.items():
                if vf.check_file_extension(my_vars["path_from"].get(), key):
                    if val["transformations"] is not None:
                        my_vars["format_from"].set(key)
                        elements["formats"].change_to_state(True)
                        elements["formats"].restructure_to_menu(val["transformations"])
                        elements["formats"].adjust_to()
                        return
            controller.status_change("Unsupported FROM format", "WARNING")
    elements["search_from"].callback = callback_search_from

    # (?) Formats setup
    elements["formats"].change_to_state(False)
    # (?) Restructure FROM menu options with keys of available formats
    elements["formats"].restructure_from_menu(
        list(filter(lambda key: af.formats[key]["transformations"] is not None, af.formats.keys())), elements["search_from"])

    # (?) Callback for Convert button
    elements["button_convert"].callback = controller.convert

    # (?) Variables and Status for Controller
    controller.my_vars=my_vars
    controller.status=elements["status"]



