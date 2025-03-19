import unittest
import re

from textnode import TextNode, TextType, split_nodes_delimiter, extract_markdown_images, extract_markdown_links
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

    def test_split_nodes_single_delimiter_occurence(self):
        old_nodes = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_nodes], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_split_nodes_multiple_delimiter_occurence(self):
        old_nodes = TextNode("This is text with a `code block` and another `code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_nodes], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and another ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
            ],
        )

    def test_split_nodes_no_closing_delimiter(self):
        with self.assertRaises(Exception):
            split_nodes_delimiter([TextNode("This is text with a `code block", TextType.TEXT)], "`", TextType.CODE)

    def test_split_multiple_nodes_single_delimiter_occurence(self):
        old_nodes = [
            TextNode("This is text with a `code block`", TextType.TEXT),
            TextNode(" and another `code block`", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and another ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
            ],
        )        

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )

if __name__ == "__main__":
    unittest.main()