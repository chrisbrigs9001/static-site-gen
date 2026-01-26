import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import text_node_to_html_node

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
    
    #test value error no children
    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
            
    
    #test value error no tag
    def test_to_html_tag_none(self):
        grandchild_node = LeafNode("b", "grandchild")
        child = ParentNode("a", [grandchild_node])
        parent_node = ParentNode(None, child)
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    
    #test value error none tag AND none children
    def test_to_html_tag_none_child_none(self):
        parent_node = ParentNode(None, None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    #test parent with single props
    def test_to_html_parent_with_single_props(self):
        grandchild_node = LeafNode("b", "grandchild")
        grandchild_node2 = LeafNode("img", "grandchild2")
        child = ParentNode("a", [grandchild_node, grandchild_node2])
        p = {
            "href": "https://pornhub.com"
        }
        parent_node = ParentNode("div", [child], props=p)
        self.assertEqual(
            parent_node.to_html(),
            '<div href="https://pornhub.com"><a><b>grandchild</b><img>grandchild2</img></a></div>'
        )
    #test parent with multiple props
    def test_to_html_parent_with_multi_props(self):
        grandchild_node = LeafNode("b", "grandchild")
        grandchild_node2 = LeafNode("img", "grandchild2")
        child = ParentNode("a", [grandchild_node, grandchild_node2])
        p = {
            "alt": "fucky wucky",
            "href": "https://pornhub.com"
        }
        parent_node = ParentNode("div", [child], props=p)
        self.assertEqual(
            parent_node.to_html(),
            '<div alt="fucky wucky" href="https://pornhub.com"><a><b>grandchild</b><img>grandchild2</img></a></div>'
        )
    
    #test parent with sing props, children with props
    def test_to_html_parent_single_props_child_single_props(self):
        p = {
            "href": "https://pornhub.com"
        }
        grandchild_node = LeafNode("b", "grandchild", props=p)
        grandchild_node2 = LeafNode("img", "grandchild2")
        child = ParentNode("a", [grandchild_node, grandchild_node2], props=p)
        parent_node = ParentNode("div", [child], props=p)
        self.assertEqual(
            parent_node.to_html(),
            '<div href="https://pornhub.com"><a href="https://pornhub.com"><b href="https://pornhub.com">grandchild</b><img>grandchild2</img></a></div>'
        )
    
    
    
    
    #test parent with mult props, children multi props
    def test_to_html_parent_multi_props_children_multi_props(self):
        p = {
            "alt": "fucky wucky",
            "href": "https://pornhub.com",
            "pizza": "pineapple goes on it"
        }
        grandchild_node = LeafNode("b", "grandchild", props=p)
        grandchild_node2 = LeafNode("img", "grandchild2")
        child = ParentNode("a", [grandchild_node, grandchild_node2], props=p)
        parent_node = ParentNode("div", [child], props=p)
        self.assertEqual(
            parent_node.to_html(),
            '<div alt="fucky wucky" href="https://pornhub.com" pizza="pineapple goes on it"><a alt="fucky wucky" href="https://pornhub.com" pizza="pineapple goes on it"><b alt="fucky wucky" href="https://pornhub.com" pizza="pineapple goes on it">grandchild</b><img>grandchild2</img></a></div>'
        )
    
    #test multiple of same tag
    #second occurence of same key will override the first
    def test_duplicate_tags(self):
        p = {
            "alt": "fucky wucky",
            "alt": "shebang shebang"
        }
        child = LeafNode("a", "child", props=p)
        parent_node = ParentNode("div", [child], props=p)
        self.assertEqual(
            parent_node.to_html(),
            '<div alt="shebang shebang"><a alt="shebang shebang">child</a></div>'
        )
    
        


if __name__ == "__main__":
    unittest.main()