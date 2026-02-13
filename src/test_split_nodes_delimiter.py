import unittest

from textnode import TextNode, TextType
from utils import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_no_delimiter_returns_original_node(self):
        nodes = [TextNode("hello world", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, nodes)

    def test_non_text_node_is_ignored(self):
        nodes = [TextNode("hello", TextType.BOLD)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, nodes)

    def test_single_delimited_section(self):
        nodes = [TextNode("hello **world**", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)

        expected = [
            TextNode("hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
        ]
        self.assertEqual(result, expected)

    def test_multiple_delimited_sections(self):
        nodes = [TextNode("a **b** c **d** e", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)

        expected = [
            TextNode("a ", TextType.TEXT),
            TextNode("b", TextType.BOLD),
            TextNode(" c ", TextType.TEXT),
            TextNode("d", TextType.BOLD),
            TextNode(" e", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_delimiter_at_start_and_end(self):
        nodes = [TextNode("**bold**", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)

        expected = [
            TextNode("bold", TextType.BOLD),
        ]
        self.assertEqual(result, expected)

    def test_multiple_nodes(self):
        nodes = [
            TextNode("hello **world**", TextType.TEXT),
            TextNode("!", TextType.TEXT),
        ]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)

        expected = [
            TextNode("hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode("!", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_invalid_markdown_raises_exception(self):
        nodes = [TextNode("hello **world", TextType.TEXT)]
        with self.assertRaises(Exception):
            split_nodes_delimiter(nodes, "**", TextType.BOLD)


if __name__ == "__main__":
    unittest.main()
