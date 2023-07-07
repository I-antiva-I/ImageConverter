import os
from PIL import Image

'''       

   if self.check_vars():
       print("Variables checked")
       print(">>>", self.my_vars["path_from"].get())

       # (?) Convert entire directory
       if self.my_vars["option_all_dir"].get():
           # (?) Statistics
           files_found = 0
           files_converted = 0
           # (?) Directories
           in_path = self.my_vars["path_from"].get()
           out_path = self.my_vars["path_to"].get() if self.my_vars["option_out_dir"].get() else in_path
           # (?) File names
           all_files = os.listdir(in_path)
           print(all_files)
           for file in all_files:
               conversion_result = self.convert_image(file, in_path + "/", out_path + "/")
               if conversion_result <= 1:
                   files_found = files_found + 1
               if conversion_result == 0:
                   files_converted = files_converted + 1

           # (?) Statistics output
           if files_found == 0:
               self.status.change_text("No files found", None, "dodgerblue")
           elif files_found == files_converted:
               self.status.change_text("{} found | {} converted".format(files_found, files_converted), None, "mediumseagreen")
           else:
               self.status.change_text("{} found | {} converted".format(files_found, files_converted), None, "gold")
       # (?) Convert selected file
       else:
           # (?) Directories and File name
           in_path = os.path.dirname(self.my_vars.get("path_from").get())
           out_path = self.my_vars["path_to"].get() if self.my_vars["option_out_dir"].get() else in_path
           file = os.path.basename(self.my_vars.get("path_from").get())

           conversion_result = self.convert_image(file, in_path + "/", out_path + "/")

           # (?) Result output
           if conversion_result == 2:
               self.status.change_text("File has wrong extension", None, "gold")
           elif conversion_result == 1:
               self.status.change_text("Couldn't convert file", None, "crimson")
           else:
               self.status.change_text("Successfully converted", None, "mediumseagreen")

def convert_image(self, image_name, in_path, out_path):
   vf.check_file_extension(image_name, self.my_vars)


   # (?) File has right extension
   if self.check_file_extension(extension_from):
       extension_to = self.available_formats[self.my_vars["format_to"].get()]["extensions"][0]

       print("Converting:")
       print(image_name, in_path, out_path)
       print("\tFILE NAME   :", image_name)
       print("\tEXT  FROM   :", extension_from)
       print("\tEXT  TO     :", extension_to)
       print("\tPATH FROM   :", in_path)
       print("\tPATH TO     :", out_path)

       working_file = Image.open(in_path + image_name)
       if self.my_vars["option_replace"].get() or self.check_for_duplicate(out_path + name + extension_to):
           working_file.save(out_path + name + extension_to)
           return 0
       else:
           # (?) Another file with the same name and extension exists
           return 1
   # (?) File doesn't have right extension
   else:
       return 2
'''

from utility import available_formats as af
from utility import validation_functions as vf

#   C:\Users\A\Desktop\testing
"""
    option_all_dir   | True
    option_replace   | False
    option_delete    | False
    option_out_dir   | False
    option_out_log   | False
    format_from      | FROM
    format_to        | TO
    path_from        | Select or Insert path
    path_to          | Select or Insert path
"""
# (?) CHECKS:
#       OK      |    FROM File or Directory exists
#       OK      |    TO Directory exists
#       NO      |    TO File does not exist (if replace option is not selected)
#       NO      |    Selected file has right extension

class Controller():
    def __init__(self):
        self.my_vars = None
        self.status = None

    def convert(self):
        print("[INFO] Starting conversion...")
        print("[INFO] Checking parameters...")
        print("[INFO] Checking FROM format...")

        # (?) Initial checks:
        # (?) Is FROM format selected?
        if not vf.check_if_from_format_is_set(self.get_var("format_from")):
            self.status_change("FROM format is not set","ERROR")
            return -1
        # (?) Does FROM directory exist?
        if self.get_var("option_all_dir") and not vf.check_if_dir_exists(self.get_var("path_from")):
            self.status_change("FROM "*self.get_var("option_out_dir")+"Path is not a directory", "ERROR")
            return -1
        # (?) Does FROM file exist?
        if not self.get_var("option_all_dir") and not vf.check_if_file_exists(self.get_var("path_from")):
            self.status_change("FROM "*self.get_var("option_out_dir")+"Path is not a file", "ERROR")
            return -1
        # (?) Does TO directory exist?
        if self.get_var("option_out_dir") and not vf.check_if_dir_exists(self.get_var("path_to")):
            self.status_change("TO Path is not a directory", "ERROR")
            return -1
        # (?) Does File have supported extension?
        if not self.get_var("option_all_dir") and not vf.check_file_extension(self.get_var("path_from"), self.get_var("format_from")):
            self.status_change("File has unsupported extension", "ERROR")
            return -1

        # CONVERTs


    def get_var(self,var_key):
        return self.my_vars[var_key].get()

    def status_change(self, text, mode="INFO"):
        if mode == "INFORMATION":
            color = "dodgerblue"
        elif mode == "WARNING":
            color = "gold"
        elif mode == "ERROR":
            color = "crimson"
        elif mode == "CONFIRMATION":
            color = "mediumseagreen"
        else:
            color = "white"

        self.status.change_text(text, None, color)
