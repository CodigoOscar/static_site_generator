from block import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import HTMLNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from utils import text_to_textnodes


def text_to_children(text):
    html_nodes = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        # print("DEBUG text_node:", repr(text_node), "type:", repr(text_node.text_type))
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            # normalize whitespace in the paragraph block
            lines = [line.strip() for line in block.split("\n")]
            lines = [line for line in lines if line]  # remove empty lines
            if not lines:
                continue  # skip empty paragraph
            para_text = " ".join(lines)
            block_nodes.append(ParentNode("p", text_to_children(para_text)))
        elif block_type == BlockType.HEADING:
            hash, text = block.split(" ", 1)
            block_nodes.append(ParentNode(f"h{len(hash)}", text_to_children(text)))
        elif block_type == BlockType.QUOTE:
            quote_list = block.split("\n>")
            quote_list = [quote.strip("> ") for quote in quote_list]
            block_nodes.append(
                ParentNode("blockquote", text_to_children("\n".join(quote_list)))
            )
        elif block_type == BlockType.UNORDERED_LIST:
            li_nodes = []
            for line in block.split("\n"):
                if line == "":
                    continue
                stripped_text = line[2:]
                children = text_to_children(stripped_text)
                li_nodes.append(ParentNode("li", children))
            block_nodes.append(ParentNode("ul", li_nodes))
        elif block_type == BlockType.ORDERED_LIST:
            li_nodes = []
            for line in block.split("\n"):
                line = line.strip()
                if not line:
                    continue
                _, text = line.split(" ", 1)
                children = text_to_children(text)
                li_nodes.append(ParentNode("li", children))
            block_nodes.append(ParentNode("ol", li_nodes))
        elif block_type == BlockType.CODE:
            lines = block.split("\n")
            inner_lines = lines[1:-1]
            clean_lines = [line.lstrip() for line in inner_lines]
            inner_text = "\n".join(clean_lines) + "\n"
            code_node = TextNode(inner_text, TextType.CODE)
            code_child = text_node_to_html_node(code_node)
            block_nodes.append(ParentNode("pre", [code_child]))
    return ParentNode("div", block_nodes)
