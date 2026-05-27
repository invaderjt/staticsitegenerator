import unittest
from textnode import *
from split_delimiter import *



class TestSplitDelimiter(unittest.TestCase):
    def test_code_block_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        match_nodes = [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT)]
        self.assertEqual(new_nodes, match_nodes)

    def test_bold_split(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        match_nodes = [TextNode("This is text with a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" word", TextType.TEXT)]
        self.assertEqual(new_nodes, match_nodes)

    def test_italic_split(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        match_nodes = [TextNode("This is text with an ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT)]
        self.assertEqual(new_nodes, match_nodes)

    def test_multiple_nodes(self):
        nodes = [TextNode("This is text with a **bold** word", TextType.TEXT), TextNode("This text also has a **bold** word", TextType.TEXT), TextNode("This text ends in a bold **word**.", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        match_nodes = [
                        TextNode("This is text with a ", TextType.TEXT),
                        TextNode("bold", TextType.BOLD),
                        TextNode(" word", TextType.TEXT),
                        TextNode("This text also has a ", TextType.TEXT),
                        TextNode("bold", TextType.BOLD),
                        TextNode(" word", TextType.TEXT),
                        TextNode("This text ends in a bold ", TextType.TEXT),
                        TextNode("word", TextType.BOLD),
                        TextNode(".", TextType.TEXT)
                ]
        self.assertEqual(new_nodes, match_nodes)


if __name__ == "__main__":
    unittest.main()