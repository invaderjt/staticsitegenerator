from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown: str) -> list[str]:
    result = []
    lines = list(map(lambda x : x.strip(), markdown.split("\n\n")))
    for line in lines:
        if line == "":
            continue
        result.append(line)
    return result



