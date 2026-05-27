from textnode import *
import os
import shutil


def copy_folder_to_folder(source: str, destination: str) -> None:
    to_do = os.listdir(source)
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    for item in to_do:
        if os.path.isfile(source + "/" + item):
            shutil.copy(source + "/" + item, destination)
        elif os.path.isdir(source + "/" + item):
            copy_folder_to_folder(source + "/" + item, destination + "/" + item)

def extract_title(markdown: str):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No header found")


def main():
    copy_folder_to_folder("./static", "./public")










main()
