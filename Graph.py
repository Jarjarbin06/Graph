## graph ##
## by JARJARBIN'S STUDIO ##
## v1.2 ##

from typing import Any
from CMDError import CMDError
from GUI import GUI
from Node import Node

class Graph(GUI):
    """
        Graph object
    """

    def __init__(self: object) -> None:

        """
            create a Graph

            Parameter :
                - self (object) : Node object
        """

        self.nodes = {}
        self.size = 0

    def __str__(self: object) -> str:

        """
            get a string version of Graph

            Parameter :
                - self (object) : Graph object

            Return :
                str : Graph
        """

        s = ""
        if len(self.nodes) == 0:
            s += "\n      No nodes yet"
        else:
            for item in self.nodes:
                s += f"\n    - {self.nodes[item].__str__()}"
        return s

    def __getitem__(self: object, node: str) -> Node:

        """
            get node

            Parameter :
                - self (object) : Graph object
                - node (str) : Node's name

            Return :
                object : Node
        """

        if not node in self.nodes:
            self.nodes[node] = Node(node)
        return self.nodes[node]

    def add(self: object, name: str, data: Any = "\033[31mNo data\033[0m") -> None:

        """
            create and add a Node to this Graph

            Parameter :
                - self (object) : Graph object
                - name (str) : new Node's name
                - data (Any) = "\033[31mNo data\033[0m" : new Node's data
        """

        if not (name in self.nodes):
            self.nodes[name] = Node(name, data=data)

    def link(self: object, link_from: str, link2: str | list[str]) -> None:

        """
            add a link from link_from to link2

            Parameter :
                - self (object) : Graph object
                - link_from (str) : name of Node
                - link2 (str | list[str]) : name(s) of Node(s)
        """

        self.add(link_from)
        if type(link2) == str:
            link2 = [link2]
        for item in link2:
            self.add(item)
            self.nodes[link_from].add(self.nodes[item])

    def unlink(self: object, link_from: str, *, link2: str | list[str] | None = None) -> None:

        """
            delete a link from link_from to link2 (all if link2 = None)

            Parameter :
                - self (object) : Graph object
                - link_from (str) : name of Node
                - link2 (str | list[str] | None)(optional) = None : name(s) of Node(s)
        """

        if not type(link2):
            self.nodes[link_from].delete_all()
        if type(link2) == str:
            link2 = [link2]
        for item in link2:
            self.nodes[link_from].delete(item)

    def delete(self: object, node: str) -> None:

        """
            delete node and all links to it from this Graph

            Parameter :
                - self (object) : Graph object
                - node (str) : Node's name
        """

        self.nodes.pop(node)
        for n in self.nodes:
            self.nodes[n].delete(node)

    def new_data(self: object, node: str, data: Any = "\033[31mNo data\033[0m") -> None:

        """
            change node's data to new data

            Parameter :
                - self (object) : Graph object
                - node (str) : Node's name
                - data (Any) = "\033[31mNo data\033[0m" : new node's data
        """

        self.add(node)
        self.nodes[node].data = data

    def new_pos(self: object, node: str, pos_x: int | float | None, pos_y: int | float | None) -> None:

        """
            change node's position to new position

            Parameter :
                - self (object) : Graph object
                - node (str) : Node's name
                - pos_x (int | float | None) : new node's position (x)
                - pos_y (int | float | None) : new node's position (y)
        """

        self.add(node)
        self.nodes[node].pos = (float(pos_x), float(pos_y))

    def update(self: object) -> None:

        """
            update Graph info

            Parameter :
                - self (object) : Graph object
        """

        self.size = len(self.nodes)

    def get_nodes(self: object) -> list[str]:

        """
            get all Nodes' name in this Graph

            Parameter :
                - self (object) : Graph object

            Return :
                list : Nodes' name
        """

        nodes_name = []
        for x in self.nodes:
            nodes_name.append(x)
        return nodes_name

    def get_size(self: object) -> int:

        """
            get quantity of Nodes in this Graph

            Parameter :
                - self (object) : Graph object

            Return :
                int : Nodes' quantity
        """

        return self.size

    def get_links(self: object, node: str) -> list:

        """
            get all links that goes from node

            Parameter :
                - self (object) : Graph object
                - node (str) : Node's name

            Return :
                list : links
        """

        links = None
        if node in self.nodes:
            links = []
            for link in self.nodes[node].get_links():
                links.append(link.name)
        return links

    def get_data(self: object, node: str) -> Any:

        """
            get data from node

            Parameter :
                - self (object) : Graph object
                - node (str) : Node's name

            Return :
                Any : data
        """

        data = None
        if node in self.nodes:
            data = self.nodes[node].get_data()
        return data

    def __call__(self: object, instructions_list: list[str]) -> Any:

        """
            respond to given command line when calling a Graph object

            Parameter :
                - self (object) : Graph object
                - instructions (str) : command line

            Return :
                Any : return of command
        """

        ret = None
        inst_copy = instructions_list
        inst = instructions_list[1:]
        try:
            if len(inst) == 0:
                return f"{inst_copy[0]} contain {self.get_size()} nodes"
            if inst[0] == "add":
                if len(inst) < 2 or len(inst) > 3:
                    raise CMDError(inst_copy, None, f'argument error (needs 1 or 2, gave {len(inst) - 1})')
                if len(inst) == 2:
                    self.add(inst[1])
                else:
                    self.add(inst[1], inst[2])
            elif inst[0] == "add:l":
                if len(inst) != 3:
                    raise CMDError(inst_copy, None, f'argument error (needs 2, gave {len(inst) - 1})')
                self.link(inst[1], inst[2])
            elif inst[0] == "del":
                if len(inst) != 2:
                    raise CMDError(inst_copy, None, f'argument error (needs 1, gave {len(inst) - 1})')
                self.delete(inst[1])
            elif inst[0] == "del:l":
                if len(inst) < 2 or len(inst) > 3:
                    raise CMDError(inst_copy, None, f'argument error (needs 2, gave {len(inst) - 1})')
                if len(inst) == 2:
                    self.unlink(inst[1])
                else:
                    self.unlink(inst[1], link2=inst[2])
            elif inst[0] == "get":
                if len(inst) != 2:
                    raise CMDError(inst_copy, None, f'argument error (needs 1, gave {len(inst) - 1})')
                ret = self[inst[1]]
            elif inst[0] == "get:n":
                if len(inst) != 1:
                    raise CMDError(inst_copy, None, f'argument error (needs 0, gave {len(inst) - 1})')
                ret = self.get_nodes()
            elif inst[0] == "get:s":
                if len(inst) != 1:
                    raise CMDError(inst_copy, None, f'argument error (needs 0, gave {len(inst) - 1})')
                ret = self.get_size()
            elif inst[0] == "get:l":
                if len(inst) != 2:
                    raise CMDError(inst_copy, None, f'argument error (needs 1, gave {len(inst) - 1})')
                ret = self.get_links(inst[1])
            elif inst[0] == "get:d":
                if len(inst) != 2:
                    raise CMDError(inst_copy, None, f'argument error (needs 1, gave {len(inst) - 1})')
                ret = self.get_data(inst[1])
            elif inst[0] == "upt":
                if len(inst) != 1:
                    raise CMDError(inst_copy, None, f'argument error (needs 0, gave {len(inst) - 1})')
                self.update()
            elif inst[0] == "upt:d":
                if len(inst) != 3:
                    raise CMDError(inst_copy, None, f'argument error (needs 2, gave {len(inst) - 1})')
                self.new_data(inst[1], inst[2])
            elif inst[0] == "upt:p":
                if len(inst) != 4:
                    raise CMDError(inst_copy, None, f'argument error (needs 3, gave {len(inst) - 1})')
                self.new_pos(inst[1], inst[2], inst[3])
            elif inst[0] == "shw":
                if len(inst) != 1:
                    raise CMDError(inst_copy, None, f'argument error (needs 0, gave {len(inst) - 1})')
                self.show()
            else:
                raise CMDError(inst_copy, 1, "invalid command")
        except CMDError as err:
            print(err)
            return ""
        else:
            return ret