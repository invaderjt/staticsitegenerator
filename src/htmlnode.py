from textnode import TextType

class HTMLNode():
    def __init__(self, tag: str | None = None, value: str | None = None, children: list[HTMLNode] | None = None, props: dict[str, str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == [] or self.props is None:
            return ""
        result = ""
        for prop in self.props:
            result += f' {prop}="{self.props[prop]}"'
        return result

    def __repr__(self):
        return f"tag: {self.tag} | value: {self.value} | children: {self.children.__repr__() if self.children is not None else None} | props: {self.props}"
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )
    


class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str | None = None, props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        
    def __repr__(self):
        return f"tag: {self.tag} | value: {self.value} | props: {self.props}"
    
    
    
class ParentNode(HTMLNode):
    def __init__(self, tag: str | None, children: list[HTMLNode] | None, props: dict[str, str] | None = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent nodes must have a tag")
        if self.children is None:
            raise ValueError("Children missing value")
        children_string = ""
        for child in self.children:
            children_string += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>'
    
    def __repr__(self):
        return f"tag: {self.tag} | children: {self.children} | props: {self.props}"
    


def text_node_to_html_node(text_node):
    tag = None
    value = None
    props = None
    match text_node.text_type:
        case TextType.TEXT:
            value = text_node.text
        case TextType.BOLD:
            tag = "b"
            value = text_node.text
        case TextType.ITALIC:
            tag = "i"
            value = text_node.text
        case TextType.CODE:
            tag = "code"
            value = text_node.text
        case TextType.LINK:
            tag = "a"
            value = text_node.text
            props = {"href" : text_node.url}
        case TextType.IMAGE:
            tag = "img"
            value = ""
            props = {"src" : text_node.url, "alt" : text_node.text}
    return LeafNode(tag, value, props)

