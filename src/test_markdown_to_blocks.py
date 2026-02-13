import unittest

from block import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_single_paragraph(self):
        markdown = "This is a single paragraph."
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            ["This is a single paragraph."],
            blocks,
        )

    def test_multiple_paragraphs(self):
        markdown = "First paragraph.\n\nSecond paragraph.\n\nThird paragraph."
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            [
                "First paragraph.",
                "Second paragraph.",
                "Third paragraph.",
            ],
            blocks,
        )

    def test_multiline_block(self):
        markdown = "Line one of block\nLine two of block\n\nNext block"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            [
                "Line one of block\nLine two of block",
                "Next block",
            ],
            blocks,
        )

    def test_leading_blank_lines(self):
        markdown = "\n\nActual content"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            ["Actual content"],
            blocks,
        )

    def test_trailing_blank_lines(self):
        markdown = "Actual content\n\n\n"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            ["Actual content"],
            blocks,
        )

    def test_multiple_consecutive_blank_lines(self):
        markdown = "Block one\n\n\n\nBlock two"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            [
                "Block one",
                "Block two",
            ],
            blocks,
        )

    def test_empty_string(self):
        markdown = ""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual([], blocks)

    def test_only_blank_lines(self):
        markdown = "\n\n\n"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual([], blocks)
