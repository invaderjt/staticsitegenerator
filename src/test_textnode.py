import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("", TextType.BOLD)
        node2 = TextNode("", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("Text node", TextType.BOLD, None)
        node2 = TextNode("Text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This might be a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_noteq2(self):
        node = TextNode("This is a text node", TextType.LINK, "www.google.com")
        node2 = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()