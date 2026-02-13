import unittest
from enum import Enum

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")

    def test_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")

    def test_code(self):
        node = TextNode("print('hello')", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('hello')")

    def test_link(self):
        node = TextNode("Click here", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_image(self):
        node = TextNode("Alt text", TextType.IMAGE, "https://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "Alt text")
        self.assertEqual(
            html_node.props, {"src": "https://example.com/image.png", "alt": "Alt text"}
        )

    def test_invalid_text_type(self):
        class InvalidTextType(Enum):
            INVALID = "invalid"

        node = TextNode("Some text", InvalidTextType.INVALID)
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(node)
        self.assertTrue("Not a Valid Text Type" in str(context.exception))

    def test_empty_text(self):
        node = TextNode("", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "")

    def test_link_with_special_characters(self):
        node = TextNode(
            "Special & <chars>", TextType.LINK, "https://example.com?param=1&other=2"
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Special & <chars>")
        self.assertEqual(
            html_node.props, {"href": "https://example.com?param=1&other=2"}
        )


if __name__ == "__main__":
    unittest.main()
