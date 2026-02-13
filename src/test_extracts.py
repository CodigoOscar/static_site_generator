import unittest

from utils import extract_markdown_images, extract_markdown_links


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_multiple_images(self):
        text = "![one](one.jpg) and ![two](two.png)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("one", "one.jpg"), ("two", "two.png")])

    def test_no_images(self):
        text = "Just some text with no images"
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

    def test_images_and_links_only_images_returned(self):
        text = "![img](img.png) and [link](site.com)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("img", "img.png")])


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_single_link(self):
        text = "Here is a [link](https://example.com)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("link", "https://example.com")])

    def test_multiple_links(self):
        text = "[one](one.com) and [two](two.com)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("one", "one.com"), ("two", "two.com")])

    def test_no_links(self):
        text = "Just some text"
        result = extract_markdown_links(text)
        self.assertEqual(result, [])

    def test_images_are_not_links(self):
        text = "![image](img.png)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [])

    def test_images_and_links_only_links_returned(self):
        text = "![img](img.png) and [link](site.com)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("link", "site.com")])


if __name__ == "__main__":
    unittest.main()
