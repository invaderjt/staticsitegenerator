import os
import shutil
from generate_pages import *



dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    copy_folder_to_folder("./static", "./public")
    page_maker(dir_path_content, template_path, dir_path_public)
    









main()
