import unittest

from generate_page import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_single_valid_title(self):
        markdown = "# My Title"
        result = extract_title(markdown)
        self.assertEqual(result, "My Title")

    def test_title_with_other_content(self):
        markdown = """# My Title

This is a paragraph.

## Subtitle
More text.
"""
        result = extract_title(markdown)
        self.assertEqual(result, "My Title")

    def test_no_title_raises_exception(self):
        markdown = """This is a paragraph.

## Subtitle
"""
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "Wrong quantity of titles.")

    def test_multiple_titles_raises_exception(self):
        markdown = """# First Title

Some text.

# Second Title
"""
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "Wrong quantity of titles.")

    def test_only_h2_is_not_valid_title(self):
        markdown = """## Not The Main Title

Content here.
"""
        with self.assertRaises(Exception):
            extract_title(markdown)


if __name__ == "__main__":
    unittest.main()
