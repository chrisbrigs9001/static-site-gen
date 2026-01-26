import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import text_node_to_html_node

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    #def test_leaf_to_html_img(self):
    #    props = {
    #        "href": "https://google.com",
    #        "alt": "poopoopeepee"
    #    }
    #    node = LeafNode("img", props=props)
    def test_leaf_to_html_a_with_href(self):
        node = LeafNode("a", "Click me", {"href": "https://example.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://example.com">Click me</a>',
        )

    def test_leaf_to_html_a_with_href_and_alt(self):
        props = {
            "href": "https://google.com",
            "alt": "poopoopeepee"
        }
        node = LeafNode("a", "Fuck Me" , props)
        self.assertEqual(
            node.to_html(),
            '<a href="https://google.com" alt="poopoopeepee">Fuck Me</a>'
        )
        
        
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")
        
    def test_leaf_to_html_no_value_raises(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
            
            
    def test_props_to_html_formatting(self):
        node = LeafNode("span", "hi", {"class": "greeting", "id": "g1"})
        # You can assert that each piece is contained
        html = node.to_html()
        self.assertIn("class=\"greeting\"", html)
        self.assertIn("id=\"g1\"", html)
        
    def test_leaf_to_html_img_generic(self):
        node = LeafNode("img", "alt text", {"src": "cat.png"})
        self.assertEqual(
            node.to_html(),
            '<img src="cat.png">alt text</img>',
        )
        
        
    def test_leaf_empty_props(self):
        node = LeafNode("p", "Hello", {})
        self.assertEqual(node.to_html(), "<p>Hello</p>")

    def test_leaf_numeric_prop_value(self):
        node = LeafNode("div", "content", {"data-count": 5})
        html = node.to_html()
        self.assertIn('data-count="5"', html)

    def test_leaf_bool_prop_value(self):
        node = LeafNode("input", "ignored", {"disabled": True})
        html = node.to_html()
        self.assertIn('disabled="True"', html)

    def test_leaf_prop_with_spaces_and_symbols(self):
        node = LeafNode("span", "text", {"title": "hello world!", "data-x": "a&b"})
        html = node.to_html()
        self.assertIn('title="hello world!"', html)
        self.assertIn('data-x="a&b"', html)
        
    def test_leaf_raises_without_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
if __name__ == "__main__":
    unittest.main()