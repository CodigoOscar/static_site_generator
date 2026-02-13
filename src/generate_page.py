import os
from pathlib import Path

from block import markdown_to_blocks
from block_to_html import markdown_to_html_node
from htmlnode import HTMLNode


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    title_lines = list(filter(lambda x: x.startswith("# "), blocks))
    if len(title_lines) != 1:
        raise Exception("Wrong quantity of titles.")
    return title_lines[0].strip("# ")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as file:
        markdown_content = file.read()
    with open(template_path, "r", encoding="utf-8") as file:
        template_content = file.read()
    html_node: HTMLNode = markdown_to_html_node(markdown_content)
    html_string = html_node.to_html()
    page_title = extract_title(markdown_content)
    new_html_page = template_content.replace("{{ Title }}", page_title)
    new_html_page = new_html_page.replace("{{ Content }}", html_string)
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(new_html_page)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isdir(content_path):
            generate_pages_recursive(content_path, template_path, dest_path)
        else:
            if content_path.endswith(".md"):
                dest_path = Path(dest_path).with_suffix(".html")
                generate_page(content_path, template_path, dest_path)
