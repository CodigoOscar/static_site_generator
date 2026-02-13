from enum import Enum


def markdown_to_blocks(markdown):
    block_strings = []
    split_md = markdown.splitlines()
    temp_str = ""
    for line in split_md:
        if line == "":
            if temp_str != "":
                block_strings.append(temp_str.strip())
            temp_str = ""
            continue
        temp_str += f"{line}\n"
    if temp_str != "":
        block_strings.append(temp_str.strip())
    return block_strings


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(single_block: str):
    if single_block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if single_block.startswith("```\n") and single_block.endswith("```"):
        return BlockType.CODE
    split_block = single_block.split("\n")
    if all(block.startswith(">") for block in split_block):
        return BlockType.QUOTE
    if all(block.startswith("- ") for block in split_block):
        return BlockType.UNORDERED_LIST
    for i, line in enumerate(split_block, start=1):
        if not line.startswith(f"{i}. "):
            return BlockType.PARAGRAPH
        if line == split_block[-1]:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
