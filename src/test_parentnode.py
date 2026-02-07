import unittest

from htmlnode import LeafNode, ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_single_leaf_child(self):
        child = LeafNode("p", "Hello world")
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><p>Hello world</p></div>")

    def test_multiple_leaf_children(self):
        children = [
            LeafNode("span", "One"),
            LeafNode("span", "Two"),
            LeafNode("span", "Three"),
        ]
        parent = ParentNode("div", children)
        self.assertEqual(
            parent.to_html(),
            "<div><span>One</span><span>Two</span><span>Three</span></div>",
        )

    def test_parent_with_props(self):
        child = LeafNode("p", "Content")
        parent = ParentNode("div", [child], props={"class": "container", "id": "main"})
        self.assertEqual(
            parent.to_html(), '<div class="container" id="main"><p>Content</p></div>'
        )

    def test_nested_parent_nodes(self):
        inner_child = LeafNode("span", "Nested")
        inner_parent = ParentNode("p", [inner_child])
        outer_parent = ParentNode("div", [inner_parent])

        self.assertEqual(
            outer_parent.to_html(), "<div><p><span>Nested</span></p></div>"
        )

    def test_mixed_children(self):
        children = [
            LeafNode(None, "Plain text"),
            LeafNode("strong", "Bold"),
        ]
        parent = ParentNode("p", children)

        self.assertEqual(parent.to_html(), "<p>Plain text<strong>Bold</strong></p>")

    def test_child_with_props(self):
        child = LeafNode("a", "Link", props={"href": "https://example.com"})
        parent = ParentNode("div", [child])

        self.assertEqual(
            parent.to_html(), '<div><a href="https://example.com">Link</a></div>'
        )

    def test_raises_error_when_no_tag(self):
        child = LeafNode("p", "Text")
        parent = ParentNode(None, [child])

        with self.assertRaises(ValueError):
            parent.to_html()

    def test_raises_error_when_no_children(self):
        parent = ParentNode("div", [])

        with self.assertRaises(ValueError):
            parent.to_html()

    def test_children_render_in_order(self):
        child1 = LeafNode("span", "First")
        child2 = LeafNode("span", "Second")
        parent = ParentNode("div", [child1, child2])

        html = parent.to_html()
        self.assertTrue(html.index("First") < html.index("Second"))

    if __name__ == "__main__":
        unittest.main()
