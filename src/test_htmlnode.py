import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single(self):
        node = HTMLNode(tag="div", props={"class": "container"})
        self.assertEqual(node.props_to_html(), ' class="container"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(tag="a", props={"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://boot.dev" target="_blank"')

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p", props={})
        self.assertEqual(node.props_to_html(), '')
    
    def test_props_to_html_none(self):
        node = HTMLNode(tag="p")
        self.assertEqual(node.props_to_html(), '')
    
    def test_props_to_html_boolean(self):
        node = HTMLNode(tag="input", props={"disabled": True, "checked": False})
        self.assertEqual(node.props_to_html(), ' disabled="True" checked="False"')

    def test_props_to_html_special_characters(self):
        node = HTMLNode(tag="button", props={"aria-label": 'Click "here"', "data-value": "some'value"})
        self.assertEqual(node.props_to_html(), ' aria-label="Click \"here\"" data-value="some\'value"')

if __name__ == "__main__":
    unittest.main()