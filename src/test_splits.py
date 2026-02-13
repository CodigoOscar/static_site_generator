import unittest

from textnode import TextNode, TextType
from utils import split_nodes_image, split_nodes_link


class TestSplitNodeImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_image_at_start(self):
        node = TextNode(
            "![alt](https://example.com/img.png) starts the text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("alt", TextType.IMAGE, "https://example.com/img.png"),
                TextNode(" starts the text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_image_at_end(self):
        node = TextNode(
            "Text ends with an image ![alt](https://example.com/img.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Text ends with an image ", TextType.TEXT),
                TextNode("alt", TextType.IMAGE, "https://example.com/img.png"),
            ],
            new_nodes,
        )

    def test_no_images(self):
        node = TextNode("Just plain text", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

    def test_non_text_node_unchanged(self):
        node = TextNode("alt", TextType.IMAGE, "https://example.com/img.png")
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)


class TestSplitNodeLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is a [link](https://example.com) and another [second](https://example.org)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second", TextType.LINK, "https://example.org"),
            ],
            new_nodes,
        )

    def test_link_at_start(self):
        node = TextNode(
            "[link](https://example.com) starts here",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" starts here", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_link_at_end(self):
        node = TextNode(
            "Ends with a [link](https://example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Ends with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
            ],
            new_nodes,
        )

    def test_no_links(self):
        node = TextNode("Just text here", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_image_not_treated_as_link(self):
        node = TextNode(
            "This is an image ![alt](https://example.com/img.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)
