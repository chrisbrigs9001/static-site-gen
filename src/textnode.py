from enum import Enum
from htmlnode import ParentNode, LeafNode, HTMLNode

class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    CODE = 'code'
    IMAGE = "image"
    LINK = "link"
    TEXT = "text"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other):
        return (self.text==other.text) and (self.text_type == other.text_type) and (self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    the_tag = None
    any_props = None
    val = text_node.text
    if text_node.text_type == TextType.BOLD:
        the_tag = 'b'
    elif text_node.text_type == TextType.CODE:
        the_tag = 'code'
    elif text_node.text_type == TextType.IMAGE:
        the_tag = 'img'
        val=''
        any_props = {
            "src": text_node.url,
            "alt": text_node.text
        }
    elif text_node.text_type == TextType.ITALIC:
        the_tag = 'i'
    elif text_node.text_type == TextType.LINK:
        the_tag = 'a'
        if text_node.url:
            any_props = {'href': text_node.url}
    elif text_node.text_type == TextType.TEXT:
        pass
    else:
        raise Exception("In test_node_to_html_node, provided text_node.TextType is invalid")
    
    return LeafNode(the_tag, val ,props=any_props)