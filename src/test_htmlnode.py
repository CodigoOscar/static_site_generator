import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_init_defaults(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_init_with_values(self):
        node = HTMLNode(tag="p", value="Hello", children=[], props={"class": "text"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "text"})

    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_prop(self):
        node = HTMLNode(props={"class": "container"})
        self.assertEqual(node.props_to_html(), 'class="container"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={"class": "container", "id": "main"})
        result = node.props_to_html()
        self.assertIn('class="container"', result)
        self.assertIn('id="main"', result)

    def test_to_html_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_repr(self):
        node = HTMLNode(tag="div", value="hi")
        repr_str = repr(node)
        self.assertIn("tag = div", repr_str)
        self.assertIn("value = hi", repr_str)


if __name__ == "__main__":
    unittest.main()
