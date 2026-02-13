import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter: str, text_type):
    new_nodes = []
    for node in old_nodes:
        if delimiter not in node.text or node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            print("Delimiter:", delimiter)
            print("Problem text:", node.text)
            raise ValueError("Invalid markdown syntax, formatted section not closed")
        split_text = node.text.split(delimiter)
        for i, text in enumerate(split_text):
            if text == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(text, TextType.TEXT))
            else:
                new_nodes.append(TextNode(text, text_type))
    return new_nodes


def extract_markdown_images(text: str) -> list[tuple]:
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text: str) -> list[tuple]:
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        img_matches = extract_markdown_images(node.text)
        if not img_matches:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        for alt, url in img_matches:
            sections = remaining_text.split(f"![{alt}]({url})", 1)
            remaining_text = sections[1]
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        link_matches = extract_markdown_links(node.text)
        if not link_matches:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        for link_text, url in link_matches:
            sections = remaining_text.split(f"[{link_text}]({url})", 1)
            remaining_text = sections[1]
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, url))
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    nodes = split_nodes_delimiter([TextNode(text, TextType.TEXT)], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
