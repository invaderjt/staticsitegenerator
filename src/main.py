import os
import shutil
import sys
from generate_pages import *


basepath = "/"
if len(sys.argv) > 1:
    basepath = sys.argv[1]



dir_path_static = "./static"
dir_path_content = "./content"
template_path = "./template.html"
dir_path_docs = "./docs"






def main():
    copy_folder_to_folder("./static", "./docs")
    page_maker(dir_path_content, template_path, dir_path_docs, basepath)
    









main()
