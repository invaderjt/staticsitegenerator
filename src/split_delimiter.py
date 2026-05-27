from textnode import TextNode, TextType



def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type):
    split_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        new_nodes = []
        split_string = node.text.split(sep = delimiter)
        if len(split_string) % 2 == 0:
            raise Exception("Invalid Markdown syntax")
        for i in range(len(split_string)):
            if split_string[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split_string[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_string[i], text_type))
        split_nodes.extend(new_nodes)
    return new_nodes