
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplemented
    
    def props_to_html(self):
        built = ""
        if self.props:
            for k in self.props:
                built+= f' {k}=\"{self.props[k]}\"'
        return built
    
    def __repr__(self):
        return f"HTMLNode object:\ntag={self.tag},\nvalue={self.value},\nchildren={self.children},\nprops={self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return f"{self.value}"
        #if self.tag == "img":
        #    s = f"<{self.tag}"
        #    s = s + self.props_to_html()
        #    s = s + " />"
        #    return s
        start = f"<{self.tag}"
        end = f"</{self.tag}>"
        return f"{start}{self.props_to_html()}>{self.value}{end}"

    def __repr__(self):
        return f"LeafNode object:\ntag={self.tag},\nvalue={self.value},\nprops={self.props}"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, "", children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError
        if self.children is None:
            raise ValueError("ParentNode object declared with no children")
        
        builder = f"<{self.tag}{self.props_to_html()}>"
        for c in self.children:
            builder = builder +c.to_html()
        builder=builder+f"</{self.tag}>"
        return builder