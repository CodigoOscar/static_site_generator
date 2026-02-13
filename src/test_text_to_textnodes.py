import unittest

from textnode import TextNode, TextType
from utils import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):
    def test_plain_text(self):
        text = "Just plain text"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [TextNode("Just plain text", TextType.TEXT)],
            nodes,
        )

    def test_bold_text(self):
        text = "This is **bold** text"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
            nodes,
        )

    def test_italic_text(self):
        text = "This is _italic_ text"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
            ],
            nodes,
        )

    def test_code_text(self):
        text = "This is `code` text"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" text", TextType.TEXT),
            ],
            nodes,
        )

    def test_image(self):
        text = "Image here ![alt](https://example.com/img.png)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("Image here ", TextType.TEXT),
                TextNode("alt", TextType.IMAGE, "https://example.com/img.png"),
            ],
            nodes,
        )

    def test_link(self):
        text = "Click [here](https://example.com)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("Click ", TextType.TEXT),
                TextNode("here", TextType.LINK, "https://example.com"),
            ],
            nodes,
        )

    def test_mixed_formatting(self):
        text = "This is **bold** and _italic_ with `code`"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" with ", TextType.TEXT),
                TextNode("code", TextType.CODE),
            ],
            nodes,
        )

    def test_complex_mixed_content(self):
        text = (
            "Start **bold** text with "
            "![img](https://example.com/img.png) and "
            "[link](https://example.com)"
        )
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("Start ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text with ", TextType.TEXT),
                TextNode("img", TextType.IMAGE, "https://example.com/img.png"),
                TextNode(" and ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
            ],
            nodes,
        )

    def test_unclosed_delimiter_raises(self):
        text = "This is **bold"
        with self.assertRaises(ValueError):
            text_to_textnodes(text)
