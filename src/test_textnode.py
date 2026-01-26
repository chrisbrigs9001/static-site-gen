import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_equal_urls(self):
        node = TextNode("This is a text node", TextType.ITALIC, "pornhub.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, "cornhub.com")
        self.assertNotEqual(node, node2)
    def test_not_equal_type(self):
        node = TextNode("testNode", TextType.BOLD)
        node2 = TextNode("testNode", TextType.IMAGE)
        self.assertNotEqual(node, node2)
    def test_print(self):
        node = TextNode("testNode", TextType.PLAIN, "moc.buhnroc")
        #self.as

if __name__ == "__main__":
    unittest.main()