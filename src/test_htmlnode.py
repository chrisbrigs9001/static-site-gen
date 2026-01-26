import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_not_none(self):
        node1 = HTMLNode(tag="<a>", props={"poop":"flarp"})
        #print(node1.props_to_html())
        self.assertIsNotNone(node1.props_to_html())
    
    def test_props_to_html_is_empty(self):
        node1 = HTMLNode()
        self.assertEqual(node1.props_to_html(),'')
        
    def test_repr_none(self):
        expected = f"HTMLNode object:\ntag={None},\nvalue={None},\nchildren={None},\nprops={None}"
        node1 = HTMLNode()
        self.assertEqual(expected, repr(node1))
        
    def test_repr_tagonly(self):
        expected = f"HTMLNode object:\ntag=a,\nvalue={None},\nchildren={None},\nprops={None}"
        node1 = HTMLNode(tag="a")
        self.assertEqual(expected, repr(node1))
        
    def test_repr_valueonly(self):
        expected = f"HTMLNode object:\ntag={None},\nvalue=never gonna give you up,\nchildren={None},\nprops={None}"
        node1 = HTMLNode(value="never gonna give you up")
        self.assertEqual(expected, repr(node1))
        
    def test_repr_children(self):
        chilren = []
        for i in range (3):
            chilren.append(HTMLNode())
        expected = f"HTMLNode object:\ntag={None},\nvalue={None},\nchildren={chilren},\nprops={None}"
        node1 = HTMLNode(children=chilren)
        self.assertEqual(expected, repr(node1))



if __name__ == "__main__":
    unittest.main()