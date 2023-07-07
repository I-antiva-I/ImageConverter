import os

from utility import available_formats as af


def check_if_file_exists(path):
    return os.path.isfile(path)


def check_if_dir_exists(path):
    return os.path.isdir(path)


def check_if_from_format_is_set(from_key):
    if from_key in af.formats:
        return True
    else:
        return False


# REDUNDANT
def check_if_to_format_is_set(from_key, to_key):
    if from_key in af.formats:
        if af.formats[from_key]["transformations"].__contains__(to_key):
            return True
    else:
        return False


def check_file_extension(file_name, from_key):
    extension = os.path.splitext(file_name)[1]
    return af.formats[from_key]["extensions"].__contains__(extension)


'''

def check_vars(self):
    if self.my_vars.get("option_all_dir").get() and not os.path.isdir(self.my_vars.get("path_from").get()):
        self.status.change_text("Path" + " FROM" * self.my_vars.get("option_out_dir").get() + " is not a directory", None, "crimson")
        return 0

    if not self.my_vars.get("option_all_dir").get() and not os.path.isfile(self.my_vars.get("path_from").get()):
        self.status.change_text("Path" + " FROM" * self.my_vars.get("option_out_dir").get() + " is not a file", None, "crimson")
        return 0

    if self.my_vars.get("option_out_dir").get() and not os.path.isdir(self.my_vars.get("path_to").get()):
        self.status.change_text("Path TO is not a directory", None, "crimson")
        return 0

    if self.my_vars.get("format_from").get() == "FROM":
        self.status.change_text("Format FROM is not selected", None, "crimson")
        return 0

    if self.my_vars.get("format_to").get() == "TO":
        self.status.change_text("Format TO is not selected", None, "crimson")
        return 0

    # (?)
    if not self.available_formats.get(self.my_vars.get("format_from").get())["to_formats"].__contains__(
            (self.my_vars.get("format_to").get())):
        self.status.change_text("Unsupported format", None, "crimson")
        return 0

    return 1



'''
