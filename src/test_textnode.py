import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()