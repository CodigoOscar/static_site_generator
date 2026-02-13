import unittest

from block import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        block = "This is a normal paragraph of text."
        self.assertEqual(
            BlockType.PARAGRAPH,
            block_to_block_type(block),
        )

    def test_multiline_paragraph(self):
        block = "This is line one\nThis is line two"
        self.assertEqual(
            BlockType.PARAGRAPH,
            block_to_block_type(block),
        )

    def test_heading_level_1(self):
        block = "# Heading 1"
        self.assertEqual(
            BlockType.HEADING,
            block_to_block_type(block),
        )

    def test_heading_level_6(self):
        block = "###### Heading 6"
        self.assertEqual(
            BlockType.HEADING,
            block_to_block_type(block),
        )

    def test_code_block(self):
        block = "```\nprint('hello')\n```"
        self.assertEqual(
            BlockType.CODE,
            block_to_block_type(block),
        )

    def test_code_block_multiple_lines(self):
        block = "```\nline one\nline two\n```"
        self.assertEqual(
            BlockType.CODE,
            block_to_block_type(block),
        )

    def test_quote_single_line(self):
        block = "> This is a quote"
        self.assertEqual(
            BlockType.QUOTE,
            block_to_block_type(block),
        )

    def test_quote_multiple_lines(self):
        block = "> Quote line one\n> Quote line two"
        self.assertEqual(
            BlockType.QUOTE,
            block_to_block_type(block),
        )

    def test_unordered_list_single_item(self):
        block = "- Item one"
        self.assertEqual(
            BlockType.UNORDERED_LIST,
            block_to_block_type(block),
        )

    def test_unordered_list_multiple_items(self):
        block = "- Item one\n- Item two\n- Item three"
        self.assertEqual(
            BlockType.UNORDERED_LIST,
            block_to_block_type(block),
        )

    def test_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(
            BlockType.ORDERED_LIST,
            block_to_block_type(block),
        )

    def test_ordered_list_wrong_numbers(self):
        block = "1. First item\n3. Second item"
        self.assertEqual(
            BlockType.PARAGRAPH,
            block_to_block_type(block),
        )

    def test_ordered_list_missing_number(self):
        block = "1. First item\nSecond item"
        self.assertEqual(
            BlockType.PARAGRAPH,
            block_to_block_type(block),
        )

    def test_unordered_list_mixed_content(self):
        block = "- Item one\nNot an item"
        self.assertEqual(
            BlockType.PARAGRAPH,
            block_to_block_type(block),
        )

    def test_quote_mixed_content(self):
        block = "> Quote line\nNot a quote"
        self.assertEqual(
            BlockType.PARAGRAPH,
            block_to_block_type(block),
        )


if __name__ == "__main__":
    unittest.main()
