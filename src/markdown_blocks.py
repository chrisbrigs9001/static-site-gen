from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERD_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    lines = block.split('\n')
    
    if block.startswith(("# ", "## ","### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines)>1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    
    if block.startswith(">"):
        for l in lines:
            if not l.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for l in lines:
            if not l.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERD_LIST
    if block.startswith("1. "):
        c = 1
        for l in lines:
            if not l.startswith(f"{c}. "):
                return BlockType.PARAGRAPH
            c+=1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH