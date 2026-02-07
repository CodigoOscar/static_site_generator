from typing import Optional


class HTMLNode:
    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children=None,
        props: Optional[dict[str, str]] = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        return " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f"tag = {self.tag}\n value = {self.value}\n children = {self.children}\n props = {self.props}"


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: Optional[str] | None,
        value: str,
        props: Optional[dict[str, str]] = None,
    ):
        super().__init__(tag=tag, value=value, children=[], props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        if self.tag == "img":
            return f"<img {self.props_to_html()}/>"
        else:
            if self.props:
                return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"tag = {self.tag}\n value = {self.value}\n props = {self.props}"


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: Optional[str],
        children: Optional[list["HTMLNode"]],
        props: Optional[dict[str, str]] = None,
    ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if not self.children:
            raise ValueError("No children")
        html_text = f"<{self.tag}"
        if self.props:
            html_text += f" {self.props_to_html()}>"
        else:
            html_text += ">"
        for child in self.children:
            html_text += f"{child.to_html()}"
        html_text += f"</{self.tag}>"
        return html_text
