## graph ##
## by JARJARBIN'S STUDIO ##
## v1.2 ##

from typing import Any

class Node:
    """
        Node of Graph
    """

    def __init__(self: object, name: str, *, data: Any = "\033[31mNo data\033[0m", pos: tuple[int | float | None, int | float | None] = (None, None)) -> None:

        """
            create a Node

            Parameter :
                - self (object) : Node object
                - name (str) : new Node's name

                - data (Any)(optional) = "\033[31mNo data\033[0m" : new Node's data
                - pos (tuple[int | float | None, int | float | None])(optional) = (None, None) : new Node's position (GUI)
        """

        self.name = name
        self.data = data
        self.links = []
        self.pos = pos

    def __str__(self: object) -> str:

        """
            get a string version of Node

            Parameter :
                - self (object) : Node object

            Return :
                str : Node
        """

        if not self.links:
            return f"{self.name} ({self.data}) -> \033[31mNo link\033[0m"
        s = f"{self.name} ({self.data}) -> "
        for item in self.links:
            s += f"{item.name} - "
        return s.removesuffix(" - ")

    def add(self: object, link2: object) -> None:

        """
            add a link from this Node to link2

            Parameter :
                - self (object) : Node object
                - link2 (object) : Node object
        """

        self.links.append(link2)

    def delete(self: object, link2: object) -> None:

        """
            delete link from this Node to node

            Parameter :
                - self (object) : Node object
                - link2 (object) : Node object
        """

        for link in self.links:
            if link.name == link2:
                self.links.remove(link)

    def delete_all(self: object) -> None:

        """
            delete all links from this Node

            Parameter :
                - self (object) : Node object
        """

        self.links = []

    def get_links(self: object) -> list:

        """
            get all links that goes from this Node

            Parameter :
                - self (object) : Node object

            Return :
                list : links
        """

        return self.links

    def get_data(self: object) -> Any:

        """
            get data of this Node

            Parameter :
                - self (object) : Node object

            Return :
                Any : data
        """

        return self.data