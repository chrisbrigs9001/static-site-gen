
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
    def __init__(self, value, tag=None, props=None):
        self.super(tag, value, props=props)
        
    def to_html(self):
        if self.value is not None:
            if self.tag is None:
                return self.value
            start = f"<"
            end = ""
            if self.tag=="img":
                end = f"</>"
            else:
                end = f"</{self.tag}>"
            return f"{start}{self.value}{end}"
        raise ValueError