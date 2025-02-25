import unittest

from textnode import TextNode, TextType
from htmlnode import text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node1, node2)

    def test_text_type_not_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertNotEqual(node1, node2)
    
    def test_url_not_equal(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev/2")
        self.assertNotEqual(node1, node2)

    def test_url_none(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_text_node_to_html_node_text(self):
        text_node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "")
        self.assertEqual(html_node.value, "Hello, world!")

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("Hello, world!", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Hello, world!</b>")

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("Hello, world!", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Hello, world!</i>")

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("Hello, world!", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>Hello, world!</code>")
    
    def test_text_node_to_html_node_link(self):
        text_node = TextNode("Hello, world!", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://boot.dev">Hello, world!</a>')
    
    def test_text_node_to_html_node_img(self):
        text_node = TextNode("Hello, world!", TextType.IMAGE, "https://boot.dev/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://boot.dev/image.png" alt="Hello, world!"></img>')

if __name__ == "__main__":
    unittest.main()