from enum import Enum
from shared_funcs import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    extract_markdown_images,
    extract_markdown_links,
    text_to_textnodes
    )
from textnode import (
    text_node_to_html_node,
    TextNode,
    TextType,
    )
from htmlnode import ParentNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERD_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def extract_title(markdown):
    #It should pull the h1 header from the markdown file (the line that starts with a single #) and return it.
    #If there is no h1 header, raise an exception.
    #extract_title("# Hello") should return "Hello" (strip the # and any leading or trailing whitespace)
    blocks = markdown_to_blocks(markdown)
    for b in blocks:
        if block_to_block_type(b) == BlockType.HEADING:
            if b.startswith(("# ")):
                return b[2:]
    raise Exception("No h1")
            



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


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    chld = []
    for block in blocks:
        node = block_to_html_node(block)
        chld.append(node)
    return ParentNode("div", chld, None)
        

def block_to_html_node(block):
    btype = block_to_block_type(block)
    if btype == BlockType.PARAGRAPH:
        return paragraph_to_html(block)
    elif btype == BlockType.HEADING:
        return heading_to_html(block)
    elif btype == BlockType.CODE:
        return code_to_html(block)
    elif btype == BlockType.QUOTE:
        return quote_to_html(block)
    elif btype == BlockType.UNORDERD_LIST:
        return ulist_to_html(block)
    elif btype == BlockType.ORDERED_LIST:
        return olist_to_html(block)
    else:
        raise Exception("Unhandled block type")
         
#Split the markdown into blocks (you already have a function for this)
#Loop over each block:
#   Determine the type of block (you already have a function for this)
#   Based on the type of block, create a new HTMLNode with the proper data
#   Assign the proper child HTMLNode objects to the block node. I created a shared text_to_children(text) function that works for all block types. It takes a string of text and returns a list of HTMLNodes that represent the inline markdown using previously created functions (think TextNode -> HTMLNode).
#   The "code" block is a bit of a special case: it should not do any inline markdown parsing of its children. I didn't use my text_to_children function for this block type, I manually made a TextNode and used text_node_to_html_node.
#Make all the block nodes children under a single parent HTML node (which should just be a div) and return it.
#Create unit tests. Here are two to get you started:

def text_to_childs(t):
    t_nodes = text_to_textnodes(t)
    chld = []
    for tn in t_nodes:
        html_node = text_node_to_html_node(tn)
        chld.append(html_node)
    return chld

def paragraph_to_html(block):
    l = block.split("\n")
    p = " ".join(l)
    c = text_to_childs(p)
    return ParentNode("p", c)
    
def heading_to_html(block):
    i = 0
    for c in block:
        if c == "#":
            i+=1
        else:
            break
    if i+1 >= len(block):
        raise ValueError("big head")
    t = block[i+1:]
    chld = text_to_childs(t)
    return ParentNode(f"h{i}", chld)
    
def code_to_html(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("not code block")
    t = block[4:-3]
    rt = TextNode(t, TextType.TEXT)
    chld = text_node_to_html_node(rt)
    c = ParentNode("code", [chld])
    return ParentNode("pre", [c])
    
    
def olist_to_html(block):
    items = block.split("\n")
    html_items = []
    for i in items:
        parts = i.split(". ", 1)
        text = parts[1]
        children = text_to_childs(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)
    
def ulist_to_html(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_childs(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)
    
    
def quote_to_html(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_childs(content)
    return ParentNode("blockquote", children)