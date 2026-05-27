import re
from textnode import TextNode, TextType



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text: str) -> list[tuple]:
    alt_text = re.findall(r"!\[(.*?)\]", text)
    url_text = re.findall(r"\((.*?)\)", text)
    result = []
    for i in range(len(alt_text)):
        result.append((alt_text[i], url_text[i]))
    return result


def extract_markdown_links(text: str) -> list[tuple]:
    anchor_text = re.findall(r"(?<!!)\[(.*?)\]", text)
    url_text = re.findall(r"\((.*?)\)", text)
    result = []
    for i in range(len(anchor_text)):
        result.append((anchor_text[i], url_text[i]))
    return result


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        text_to_split = node.text
        for item in images:
            split_text = text_to_split.split(f"![{item[0]}]({item[1]})", maxsplit = 1)
            if len(split_text) != 2:
                print(node.text)
                print(split_text)
                raise ValueError("invalid markdown, image section not closed")
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            new_nodes.append(TextNode(item[0], TextType.IMAGE, item[1]))
            text_to_split = split_text[1]      
        if text_to_split != "":
                new_nodes.append(TextNode(text_to_split, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        text_to_split = node.text
        for item in links:
            split_text = text_to_split.split(f'[{item[0]}]({item[1]})', maxsplit = 1)
            if len(split_text) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            new_nodes.append(TextNode(item[0], TextType.LINK, item[1]))
            text_to_split = split_text[1]
        if text_to_split != "":
                new_nodes.append(TextNode(text_to_split, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    starting_text = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(starting_text, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return(nodes)