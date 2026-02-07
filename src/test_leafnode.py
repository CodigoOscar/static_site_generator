import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_no_tag_returns_value(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_with_props(self):
        node = LeafNode(
            "a",
            "Click me",
            props={"href": "https://example.com", "target": "_blank"},
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://example.com" target="_blank">Click me</a>',
        )

    def test_leaf_img_tag(self):
        node = LeafNode(
            "img",
            "",
            props={"src": "image.png", "alt": "An image"},
        )
        self.assertEqual(
            node.to_html(),
            '<img src="image.png" alt="An image"/>',
        )

    def test_leaf_empty_props(self):
        node = LeafNode("span", "Text", props={})
        self.assertEqual(node.to_html(), "<span>Text</span>")

    def test_leaf_value_none_raises_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
