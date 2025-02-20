import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_parent_node_basic(self):
        child1 = LeafNode("p", "Hello")
        child2 = LeafNode("p", "world")
        node = ParentNode("div", [child1, child2])
        self.assertEqual(node.to_html(), "<div><p>Hello</p><p>world</p></div>")

    def test_parent_node_with_props(self):
        child = LeafNode("p", "Hello")
        node = ParentNode("div", [child], props={"class": "container"})
        self.assertEqual(node.to_html(), '<div class="container"><p>Hello</p></div>')

    def test_parent_node_nested(self):
        inner_child = LeafNode("span", "Nested")
        inner_parent = ParentNode("div", [inner_child])
        outer_parent = ParentNode("section", [inner_parent])
        self.assertEqual(outer_parent.to_html(), "<section><div><span>Nested</span></div></section>")

    def test_parent_node_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "Text")]).to_html()

    def test_parent_node_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()

if __name__ == "__main__":
    unittest.main()