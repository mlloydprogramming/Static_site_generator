import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_basic(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click here", {"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://example.com" target="_blank">Click here</a>')

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_to_html_empty_value(self):
        node = LeafNode("p", "")
        self.assertEqual(node.to_html(), "<p></p>")

    def test_to_html_raises_error_on_none_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()

if __name__ == "__main__":
    unittest.main()