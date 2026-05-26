import unittest
from htmlnode import *
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_eq_props_to_html(self):
        node = HTMLNode(props = {"href": "https://www.google.com", "target": "_blank"})
        output = node.props_to_html()
        string = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(output, string)

    def test_eq(self):
        node = HTMLNode(tag = "p", value = "Contents text", children = None, props = {"href": "https://www.google.com"})
        node2 = HTMLNode(tag = "p", value = "Contents text", props = {"href": "https://www.google.com"})
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode(tag = "None", value = "words words")
        node2 = HTMLNode(tag = None, value = "words words")
        self.assertNotEqual(node,node2)

    def test_not_eq2(self):
        node = HTMLNode()
        node2 = None
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        output = node.to_html()
        self.assertEqual(output, "<p>Hello, world!</p>")

    def test_leaf_link(self):
        node = LeafNode("a", value = "Click me!", props = {"href": "https://www.google.com"})
        output = node.to_html()
        self.assertEqual(output, '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )
        
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text2(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.imgur.com/example")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(str(html_node), "tag: img | value:  | props: {'src': 'https://www.imgur.com/example', 'alt': 'This is an image'}")


if __name__ == "__main__":
    unittest.main()