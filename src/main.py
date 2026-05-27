from htmlnode import *
from block_functions import *
import os
import shutil


def copy_folder_to_folder(source: str, destination: str) -> None:
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    to_do = os.listdir(source)
    for item in to_do:
        from_path = os.path.join(source, item)
        to_path = os.path.join(destination, item)
        if os.path.isfile(from_path):
            shutil.copy(from_path, destination)
        elif os.path.isdir(from_path):
            copy_folder_to_folder(from_path, to_path)

def extract_title(markdown: str):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    title = extract_title(markdown)
    html_node = markdown_to_html_node(markdown)
    html_string = html_node.to_html()
    new_template = template.replace("{{ Title }}", title)
    final_template = new_template.replace("{{ Content }}", html_string)
    with open(dest_path, 'x') as f:
        f.write(final_template)


    

def main():
    copy_folder_to_folder("./static", "./public")
    generate_page("./content/index.md", "template.html", "./public/index.html")










main()
