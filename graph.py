## graph ##
## by JARJARBIN'S STUDIO ##
## v1.0 ##
from typing import Any, Generator


class CMDError(Exception):
    
    """
        Error class for CMD errors
    """
    
    def __init__(self : object, cmd : list[str] | None = None, err_pos : int | None = None, msg : str | None = None) -> None :
        
        """
            create an error object (child = Exception class)
            
            Parameter :
                - self (object) : CMDError object
                - cmd (list[str] | None) = None : list of every words in command
                - err_pos (int | None) = None : position/index of the error in cmd
                - msg (str | None) = None : message join to the error
        """
        
        self.cmd = cmd
        self.err_pos = err_pos
        self.msg = msg
    
    def __str__(self : object) -> str :
        
        """
            get a string version of CMDError
            
            Parameter :
                - self (object) : CMDError object
            
            Return :
                str : CMDError
        """
        
        s = '\n============================================================\n'
        s += '= \033[31m-------------------- ERROR DETECTED --------------------\033[0m =\n'
        s += '============================================================\n'
        if self.cmd :
            s += '\033[31mCMD ERROR in :\n    " '
            if self.err_pos :
                for n in range(len(self.cmd)) :
                    if n == self.err_pos :
                        s += '\033[0m\033[41m' + self.cmd[n] + '\033[0m\033[31m '
                    else :
                        s += self.cmd[n] + ' '
            else :
                s += '\033[0m\033[41m'
                for x in self.cmd :
                    s += x + ' '
                s = s[:-1]
                s += '\033[0m\033[31m '
            s += '"'
        s += '\033[0m\n\n\033[7m'
        if self.msg :
            s += self.msg
        else :
            s += 'Error in command'
        s += '\033[0m\n\n(try "help" to get information about commands)\n'
        s += '============================================================\n'
        return s

class GUI :
    
    """
        GUI for Graph
    """
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    def show(self : object, r : int | float = 10) -> None :
        
        """
            show Graph as a circle in a pyplot window
            
            Parameter :
                - self (object) : Graph object
                - r (int | float) = 10 : radius of the circle
        """
        
        dots = {}
        n = 0
        nodes_name = []
        for node in self.nodes :
            nodes_name.append(node)
        for t in self.get_nodes_pos():
            x, y = r * GUI.np.cos(t), r * GUI.np.sin(t)
            if self.nodes[nodes_name[n]].pos == (None, None) :
                dots[nodes_name[n]] = (x, y)
            else :
                dots[nodes_name[n]] = self.nodes[nodes_name[n]].pos
            n += 1
        for dot in dots :
            x, y = dots[dot]
            x_signe = 1
            if x < 0 :
                x_signe = -3.5
            y_signe = 1
            if y < 0 :
                y_signe = -3.5
            links_xy = []
            for link in self.nodes[dot].links :
                links_xy.append(dots[link.name])
            GUI.plt.plot(x, y, 'bo')
            GUI.plt.text(x + (x_signe * 0.2), y + (y_signe * 0.2), self.nodes[dot].name)
            for link in links_xy :
                link_x, link_y = link
                dist_x = 0.90 * (link_x - x)
                dist_y = 0.90 * (link_y - y)
                GUI.plt.arrow(x, y, dist_x, dist_y, width = 0.05, head_width = 0.5)
        GUI.plt.title("Graph viewer")
        GUI.plt.show()
    
    def get_nodes_pos(self : object) -> Generator[int | float | Any, Any, None]:
        
        """
            get x and y position of all nodes
            
            Parameter :
                - self (object) : Graph object
            
            Return :
                dict : positions
        """
        
        for j in range(self.get_ordre()):
            yield j*(2 * GUI.np.pi / self.get_ordre())

class Node :
    
    """
        Node of Graph
    """
    
    def __init__(self : object, name : str, *, data : any = "\033[31mNo data\033[0m", pos : tuple[int | float | None, int | float | None] = (None, None)) -> None :

        """
            create a Node
            
            Parameter :
                - self (object) : Node object
                - name (str) : new Node's name
                
                - data (any)(optional) = "\033[31mNo data\033[0m" : new Node's data
                - pos (tuple[int | float | None, int | float | None])(optional) = (None, None) : new Node's position (GUI)
        """
        
        self.name = name
        self.data = data
        self.links = []
        self.pos = pos
    
    def __str__(self : object) -> str :
        
        """
            get a string version of Node
            
            Parameter :
                - self (object) : Node object
            
            Return :
                str : Node
        """
        
        if self.links == [] :
            return f"{self.name} ({self.data}) -> \033[31mNo link\033[0m"
        s = f"{self.name} ({self.data}) -> "
        for item in self.links :
            s += f"{item.name} - "
        return s.removesuffix(" - ")
    
    def add(self : object, link2 : object) -> None :
        
        """
            add a link from this Node to link2
            
            Parameter :
                - self (object) : Node object
                - link2 (object) : Node object
        """
        
        self.links.append(link2)
    
    def delete(self : object, link2 : object) -> None :
        
        """
            delete link from this Node to node
            
            Parameter :
                - self (object) : Node object
                - link2 (object) : Node object
        """
        
        for link in self.links :
            if link.name == link2 :
                self.links.remove(link)
    
    def delete_all(self : object) -> None :
        
        """
            delete all links from this Node
            
            Parameter :
                - self (object) : Node object
        """
        
        self.links = []
    
    def get_links(self : object) -> list :
        
        """
            get all links that goes from this Node
            
            Parameter :
                - self (object) : Node object
            
            Return :
                list : links
        """
        
        return self.links
    
    def get_data(self : object) -> any :
        
        """
            get data of this Node
            
            Parameter :
                - self (object) : Node object
            
            Return :
                any : data
        """
        
        return self.data

class Graph(GUI) :
    
    """
        Graph object
    """
    
    def __init__(self : object) -> None :
        
        """
            create a Graph
            
            Parameter :
                - self (object) : Node object
        """
        
        self.nodes = {}
        self.ordre = 0
    
    def __str__(self : object) -> str :
        
        """
            get a string version of Graph
            
            Parameter :
                - self (object) : Graph object
            
            Return :
                str : Graph
        """
        
        s = ""
        if len(self.nodes) == 0 :
            s += "\n      No nodes yet"
        else :
            for item in self.nodes :
                s += f"\n    - {self.nodes[item].__str__()}"
        return s
    
    def __getitem__(self : object, node : str) -> Node :
        
        """
            get node
            
            Parameter :
                - self (object) : Graph object
                - node (str) : Node's name
            
            Return :
                object : Node
        """
        
        if not node in self.nodes :
            self.nodes[node] = Node(node)
        return self.nodes[node]
    
    def add(self : object, name : str, data : any = "\033[31mNo data\033[0m") -> None :
        
        """
            create and add a Node to this Graph
            
            Parameter :
                - self (object) : Graph object
                - name (str) : new Node's name
                - data (any) = "\033[31mNo data\033[0m" : new Node's data
        """
        
        if not(name in self.nodes) :
            self.nodes[name] = Node(name, data = data)
    
    def link(self : object, link_from : str, link2 : str | list[str]) -> None :
        
        """
            add a link from link_from to link2
            
            Parameter :
                - self (object) : Graph object
                - link_from (str) : name of Node
                - link2 (str | list[str]) : name(s) of Node(s)
        """
        
        self.add(link_from)
        if type(link2) == str :
            link2 = [link2]
        for item in link2 :
            self.add(item)
            self.nodes[link_from].add(self.nodes[item])
    
    def unlink(self : object, link_from : str, *, link2 : str | list[str] | None = None) -> None :
        
        """
            delete a link from link_from to link2 (all if link2 = None)
            
            Parameter :
                - self (object) : Graph object
                - link_from (str) : name of Node
                - link2 (str | list[str] | None)(optional) = None : name(s) of Node(s)
        """
        
        if type(link2) == None :
            self.nodes[link_from].delete_all()
        if type(link2) == str :
            link2 = [link2]
        for item in link2 :
            self.nodes[link_from].delete(item)
    
    def delete(self : object, node : str) -> None :
        
        """
            delete node and all links to it from this Graph
            
            Parameter :
                - self (object) : Graph object
                - node (str) : Node's name
        """
        
        self.nodes.pop(node)
        for n in self.nodes :
            self.nodes[n].delete(node)
    
    def new_data(self : object, node : str, data : any = "\033[31mNo data\033[0m") -> None :
        
        """
            change node's data to new data
            
            Parameter :
                - self (object) : Graph object
                - node (str) : Node's name
                - data (any) = "\033[31mNo data\033[0m" : new node's data
        """
        
        self.add(node)
        self.nodes[node].data = data
    
    def new_pos(self : object, node : str, pos_x : int | float | None, pos_y : int | float | None) -> None :
        
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
    
    def update(self : object) -> None :
        
        """
            update Graph info
            
            Parameter :
                - self (object) : Graph object
        """
        
        self.ordre = len(self.nodes)
    
    def get_nodes(self : object) -> list[str] :
        
        """
            get all Nodes' name in this Graph
            
            Parameter :
                - self (object) : Graph object
            
            Return :
                list : Nodes' name
        """
        
        nodes_name = []
        for x in self.nodes :
            nodes_name.append(x)
        return nodes_name
    
    def get_ordre(self : object) -> int :
        
        """
            get quantity of Nodes in this Graph
            
            Parameter :
                - self (object) : Graph object
            
            Return :
                int : Nodes' quantity
        """
        
        return self.ordre
    
    def get_links(self : object, node : str) -> list :
        
        """
            get all links that goes from node
            
            Parameter :
                - self (object) : Graph object
                - node (str) : Node's name
            
            Return :
                list : links
        """
        
        links = None
        if node in self.nodes :
            links = []
            for link in self.nodes[node].get_links() :
                links.append(link.name)
        return links
    
    def get_data(self : object, node : str) -> any :
        
        """
            get data from node
            
            Parameter :
                - self (object) : Graph object
                - node (str) : Node's name
            
            Return :
                any : data
        """
        
        data = None
        if node in self.nodes :
            data = self.nodes[node].get_data()
        return data
    
    def __call__(self : object, instructions_list : list[str]) -> any :
        
        """
            respond to given command line when calling a Graph object
            
            Parameter :
                - self (object) : Graph object
                - instructions (str) : command line
            
            Return :
                any : return of command
        """
        
        ret = None
        inst_copy = instructions_list
        inst = instructions_list[1:]
        try :
            if len(inst) == 0 :
                return f"{inst_copy[0]} contain {self.get_ordre()} nodes"
            if inst[0] == "add" :
                if len(inst) < 2 or len(inst) > 3 :
                    raise CMDError(inst_copy, None, f'argument error (needs 1 or 2, gave {len(inst)-1})')
                if len(inst) == 2 :
                    self.add(inst[1])
                else :
                    self.add(inst[1], inst[2])
            elif inst[0] == "add:l" :
                if len(inst) != 3 :
                    raise CMDError(inst_copy, None, f'argument error (needs 2, gave {len(inst)-1})')
                self.link(inst[1], inst[2])
            elif inst[0] == "del" :
                if len(inst) != 2 :
                    raise CMDError(inst_copy, None, f'argument error (needs 1, gave {len(inst)-1})')
                self.delete(inst[1])
            elif inst[0] == "del:l" :
                if len(inst) < 2 or len(inst) > 3 :
                    raise CMDError(inst_copy, None, f'argument error (needs 2, gave {len(inst)-1})')
                if len(inst) == 2 :
                    self.unlink(inst[1])
                else :
                    self.unlink(inst[1], link2 = inst[2])
            elif inst[0] == "get" :
                if len(inst) != 2 :
                    raise CMDError(inst_copy, None, f'argument error (needs 1, gave {len(inst)-1})')
                ret = self[inst[1]]
            elif inst[0] == "get:n" :
                if len(inst) != 1 :
                    raise CMDError(inst_copy, None, f'argument error (needs 0, gave {len(inst)-1})')
                ret = self.get_nodes()
            elif inst[0] == "get:s" :
                if len(inst) != 1 :
                    raise CMDError(inst_copy, None, f'argument error (needs 0, gave {len(inst)-1})')
                ret = self.get_ordre()
            elif inst[0] == "get:l" :
                if len(inst) != 2 :
                    raise CMDError(inst_copy, None, f'argument error (needs 1, gave {len(inst)-1})')
                ret = self.get_links(inst[1])
            elif inst[0] == "get:d" :
                if len(inst) != 2 :
                    raise CMDError(inst_copy, None, f'argument error (needs 1, gave {len(inst)-1})')
                ret = self.get_data(inst[1])
            elif inst[0] == "upt" :
                if len(inst) != 1 :
                    raise CMDError(inst_copy, None, f'argument error (needs 0, gave {len(inst)-1})')
                self.update()
            elif inst[0] == "upt:d" :
                if len(inst) != 3 :
                    raise CMDError(inst_copy, None, f'argument error (needs 2, gave {len(inst)-1})')
                self.new_data(inst[1], inst[2])
            elif inst[0] == "upt:p" :
                if len(inst) != 4 :
                    raise CMDError(inst_copy, None, f'argument error (needs 3, gave {len(inst)-1})')
                self.new_pos(inst[1], inst[2], inst[3])
            elif inst[0] == "shw" :
                if len(inst) != 1 :
                    raise CMDError(inst_copy, None, f'argument error (needs 0, gave {len(inst)-1})')
                self.show()
            else :
                raise CMDError(inst_copy, 1, "invalid command")
        except CMDError as err:
            print(err)
            return ""
        else :
            return ret

###créer les doc-strings###
class Interpretor :
    
    """
        Interpretor object
    """
    
    interpretor_list = {}
    
    def __init__(self : object, name : str | None = None) -> None :
        
        """
            create a Interpretor and add it to the created Interpretor list
            
            Parameter :
                - self (object) : Interpretor object
                - name (str | None
        """
        
        if not name :
            auto_name = 1
            while ("Interpretor"+str(auto_name)) in Interpretor.interpretor_list :
                auto_name += 1
            name = "Interpretor"+str(auto_name)
        if not name in Interpretor.interpretor_list :
            self.name = name
            self.graphs = {}
            Interpretor.interpretor_list[name] = self
    
    def __str__(self : object) -> str :
        
        """
            get a string version of Interpretor
            
            Parameter :
                - self (object) : Interpretor object
            
            Return :
                str : Interpretor
        """
        
        s = self.name
        for graph in self.graphs :
            s += "\n - " + graph + self.graphs[graph].__str__()
        return s
    
    def add(self : object, name : str) -> None :
        
        """
            create and add a Graph to this Interpretor
            
            Parameter :
                - self (object) : Interpretor object
                - name (str) : new Graph's name
        """
        
        self.graphs[name] = Graph()
    
    def __getitem__(self : object, name : str) -> Graph :
        
        """
            get graph by name
            
            Parameter :
                - self (object) : Interpretor object
                - name (str) : Graph's name
            
            Return :
                object : Graph
        """
        
        if not name in self.graphs :
            self.graphs[name] = Graph()
        return self.graphs[name]
    
    def delete(self : object, name : str) -> None :
        
        """
            delete Graph by name from this Interpretor
            
            Parameter :
                - self (object) : Interpretor object
                - name (str) : Graph's name
        """
        
        if name in self.graphs :
            self.graphs.pop(name)
    
    def __call__(self : object, instructions : list[str]) -> any :
        
        """
            respond to given command line when calling an Interpretor object
            
            Parameter :
                - self (object) : Interpretor object
                - instructions (str) : command line
            
            Return :
                any : return of command
        """
        
        from os import system
        ret = None
        inst = instructions
        cmd_list_name = {
            "add" : "\033[100madd \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m or \033[100madd [\033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m\033[100m...]\033[0m",
            "del" : "\033[100mdel \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m or \033[100mdel [\033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m\033[100m...]\033[0m",
            "get" : "\033[100mget \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m",
            "shw" : "\033[100mshw\033[0m",
            "graph" : "\033[100m\033[33m{\033[3mname\033[0m\033[100m\033[33m} {\033[3msubcmd\033[0m\033[100m\033[33m}\033[0m",
            "clr" : "\033[100mclr\033[0m",
            "quit" : "\033[100mquit\033[0m or \033[100mq\033[0m",
            "q" : "\033[100mquit\033[0m or \033[100mq\033[0m"
            }
        sub_cmd_list_name = {
            "add" : "\033[100madd \033[33m{\033[3mname\033[0m\033[100m\033[33m} {\033[3mdata\033[0m\033[100m\033[33m}\033[0m",
            "add:l" : "\033[100madd:l \033[33m{\033[3mfrom\033[0m\033[100m\033[33m} {\033[3mto\033[0m\033[100m\033[33m}\033[0m or \033[100madd:l \033[33m{\033[3mfrom\033[0m\033[100m\033[33m}\033[0m\033[100m [\033[33m{\033[3mto\033[0m\033[100m\033[33m}\033[0m\033[100m...]\033[0m",
            "del" : "\033[100mdel \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m",
            "del:l" : "\033[100mdel:l \033[33m{\033[3mfrom\033[0m\033[100m\033[33m} {\033[3mto\033[0m\033[100m\033[33m}\033[0m or \033[100mdel:l \033[33m{\033[3mfrom\033[0m\033[100m\033[33m}\033[0m\033[100m [\033[33m{\033[3mto\033[0m\033[100m\033[33m}\033[0m\033[100m...]\033[0m",
            "get" : "\033[100mget \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m",
            "get:n" : "\033[100mget:n\033[0m",
            "get:s" : "\033[100mget:s\033[0m",
            "get:l" : "\033[100mget:l \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m",
            "get:d" : "\033[100mget:d \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m",
            "upt" : "\033[100mupt\033[0m",
            "upt:d" : "\033[100mupt:d \033[33m{\033[3mname\033[0m\033[100m\033[33m} {\033[3mdata\033[0m\033[100m\033[33m}\033[0m",
            "upt:p" : "\033[100mupt:p \033[33m{\033[3mname\033[0m\033[100m\033[33m} {\033[3mpos_x\033[0m\033[100m\033[33m} {\033[3mpos_y\033[0m\033[100m\033[33m}\033[0m",
            "shw" : "\033[100mshw\033[0m"
            }
        cmd_list = {
            "\033[100mhelp\033[0m" : "\033[92mget info about commands\033[0m (args : \033[31mNone\033[0m)",
            "\033[100mhelp:sub\033[0m" : "\033[92mget info about subcommands\033[0m (args : \033[31mNone\033[0m)",
            "\033[100madd \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m or \033[100madd [\033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m\033[100m...]\033[0m" : "\033[92mcreate a new graph\033[0m (args : \033[33mname\033[0m = \033[92mname of the new graph\033[0m)",
            "\033[100mdel \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m or \033[100mdel [\033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m\033[100m...]\033[0m" : "\033[92mdelete a graph\033[0m (args : \033[33mname\033[0m = \033[92mname of the graph\033[0m)",
            "\033[100mget \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m" : "\033[92mget a graph\033[0m (args : \033[33mname\033[0m = \033[92mname of the graph\033[0m)",
            "\033[100mshw\033[0m" : "\033[92mshow the interpretor\033[0m (args : \033[31mNone\033[0m)",
            "\033[100m\033[33m{\033[3mname\033[0m\033[100m\033[33m} {\033[3msubcmd\033[0m\033[100m\033[33m}\033[0m" : "\033[92msubcommand of a graph\033[0m (args : \033[33mname\033[0m = \033[92mname of the graph\033[0m ; \033[33msubcmd\033[0m = \033[92msubcommand of the graph\033[0m)",
            "\033[100mclr\033[0m" : "\033[92mclear command interpretor window\033[0m (args : \033[31mNone\033[0m)",
            "\033[100mquit\033[0m or \033[100mq\033[0m" : "\033[92mquit command interpretor\033[0m (args : \033[31mNone\033[0m)"
            }
        sub_cmd_list = {
            "\033[100mhelp:sub\033[0m" : "\033[92mget info about subcommands\033[0m (args : \033[31mNone\033[0m)",
            "\033[100madd \033[33m{\033[3mname\033[0m\033[100m\033[33m} {\033[3mdata\033[0m\033[100m\033[33m}\033[0m" : "\033[92mcreate a new node\033[0m (args : \033[33mname\033[0m = \033[92mname of the new node\033[0m ; \033[33mdata\033[0m (optional) = \033[92mdata of the new node\033[0m)",
            "\033[100madd:l \033[33m{\033[3mfrom\033[0m\033[100m\033[33m} {\033[3mto\033[0m\033[100m\033[33m}\033[0m or \033[100madd:l \033[33m{\033[3mfrom\033[0m\033[100m\033[33m}\033[0m\033[100m [\033[33m{\033[3mto\033[0m\033[100m\033[33m}\033[0m\033[100m...]\033[0m" : "\033[92mcreate a one-way link from a node to another node\033[0m (args : \033[33mfrom\033[0m = \033[92mname of the starting node\033[0m ; \033[33mto\033[0m = \033[92mname of the end node\033[0m)",
            "\033[100mdel \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m" : "\033[92mdelete a node and all links to it\033[0m (args : \033[33mname\033[0m = \033[92mname of the node\033[0m)",
            "\033[100mdel:l \033[33m{\033[3mfrom\033[0m\033[100m\033[33m} {\033[3mto\033[0m\033[100m\033[33m}\033[0m or \033[100mdel:l \033[33m{\033[3mfrom\033[0m\033[100m\033[33m}\033[0m\033[100m [\033[33m{\033[3mto\033[0m\033[100m\033[33m}\033[0m\033[100m...]\033[0m" : "\033[92mdelete a link from a node to another node\033[0m (args : \033[33mfrom\033[0m = \033[92mname of the starting node\033[0m ; \033[33mto\033[0m = \033[92mname of the end node\033[0m)",
            "\033[100mget \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m" : "\033[92mget a node\033[0m (args : \033[33mname\033[0m = \033[92mname of the node\033[0m)",
            "\033[100mget:n\033[0m" : "\033[92mget all nodes' name\033[0m (args : \033[31mNone\033[0m)",
            "\033[100mget:s\033[0m" : "\033[92mget graph's size\033[0m (args : \033[31mNone\033[0m)",
            "\033[100mget:l \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m" : "\033[92mget all links starting from a node\033[0m (args : \033[33mname\033[0m = \033[92mname of the node\033[0m)",
            "\033[100mget:d \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m" : "\033[92mget the data of a node\033[0m (args : \033[33mname\033[0m = \033[92mname of the node\033[0m)",
            "\033[100mupt\033[0m" : "\033[92mupdate graph's info\033[0m (args : \033[31mNone\033[0m)",
            "\033[100mupt:d \033[33m{\033[3mname\033[0m\033[100m\033[33m} {\033[3mdata\033[0m\033[100m\033[33m}\033[0m" : "\033[92mupdate the data of a node\033[0m (args : \033[33mname\033[0m = \033[92mname of the node\033[0m ; \033[33mdata\033[0m (optional) = \033[92mnew data of the node\033[0m)",
            "\033[100mupt:p \033[33m{\033[3mname\033[0m\033[100m\033[33m} {\033[3mpos_x\033[0m\033[100m\033[33m} {\033[3mpos_y\033[0m\033[100m\033[33m}\033[0m" : "\033[92mupdate the position of a node in the GUI of the graph\033[0m (args : \033[33mname\033[0m = \033[92mname of the new node\033[0m ; \033[33mpos_x\033[0m = \033[92mposition x of the node\033[0m ; \033[33mpos_y\033[0m (optional) = \033[92mposition y of the node\033[0m)",
            "\033[100mshw\033[0m" : "\033[92mshow the graph\033[0m (args : \033[31mNone\033[0m)"
            }
        if inst == [""] :
            return ""
        try :
            if inst[0] == "help" :
                if len(inst) < 1 or len(inst) > 2 :
                    raise CMDError(inst, None, f'argument error (needs 0 or 1, gave {len(inst)-2})')
                if len(inst) == 1 :
                    s = "\nHELP commands :"
                    for x in cmd_list :
                        s += f"\n\n - {x} :\n      {cmd_list[x]}"
                    s += "\n"
                    ret = s
                elif len(inst) == 2 :
                    s = f"\nHELP subcommands : {inst[1]} :"
                    if inst[1] in cmd_list_name :
                        s += f"\n\n - {cmd_list_name[inst[1]]} :\n      {cmd_list[cmd_list_name[inst[1]]]}"
                    else :
                        s += "\n\n   \033[31msubcommand not found\033[0m"
                    s += "\n"
                    ret = s
            elif inst[0] == "help:sub" :
                if len(inst) < 1 or len(inst) > 2 :
                    raise CMDError(inst, None, f'argument error (needs 0 or 1, gave {len(inst)-2})')
                if len(inst) == 1 :
                    s = "\nHELP subcommands :"
                    for x in sub_cmd_list :
                        s += f"\n\n - {x} :\n      {sub_cmd_list[x]}"
                    s += "\n"
                    ret = s
                elif len(inst) == 2 :
                    cmds = {}
                    found = False
                    s = f"\nHELP subcommands : {inst[1]} :"
                    for cmd in sub_cmd_list :
                        if inst[1] in cmd :
                            found = True
                            s += f"\n\n - {cmd} :\n      {sub_cmd_list[cmd]}"
                    if not(found) :
                        s += "\n\n   \033[31msubcommand not found\033[0m"
                    s += "\n"
                    ret = s
            elif inst[0] == "add" :
                if len(inst) != 2 :
                    raise CMDError(inst, None, f'argument error (needs 1, gave {len(inst)-1})')
                self.add(inst[1])
            elif inst[0] == "get" :
                if len(inst) != 2 :
                    raise CMDError(inst, None, f'argument error (needs 1, gave {len(inst)-1})')
                ret = self[inst[1]]
            elif inst[0] == "del" :
                if len(inst) != 2 :
                    raise CMDError(inst, None, f'argument error (needs 1, gave {len(inst)-1})')
                self.delete(inst[1])
            elif inst[0] == "shw" :
                if len(inst) != 1 :
                    raise CMDError(inst, None, f'argument error (needs 0, gave {len(inst)-1})')
                ret = self.__str__()
            elif inst[0] == "welcome" :
                if len(inst) != 1 :
                    raise CMDError(inst, None, f'argument error (needs 0, gave {len(inst)-1})')
                system("clear||cls")
                ret = "welcome to the command interpretor of \033[96mgraph.py\033[0m (\033[96mv1.0\033[0m)\ncreated by Jarjarbin's STUDIO\n"
            elif inst[0] == "clr" :
                if len(inst) != 1 :
                    raise CMDError(inst, None, f'argument error (needs 0, gave {len(inst)-1})')
                system("clear||cls")
            elif inst[0] in self.graphs :
                ret = self.graphs[inst[0]](inst)
            else :
                raise CMDError(inst, None, "invalid command")
        except CMDError as err:
            print(err)
            return ""
        else :
            return ret
    
    def start(self : object) -> None :

        """
            start an interpretor

            Parameter :
                - self (object) : Interpretor object
        """

        outpt = None
        actions = [["welcome"]]
        while not(actions[0] in [["q"], ["quit"]]) :
            if len(actions) == 1 :
                outpt = self(actions[0])
                if outpt : print(outpt)
            else :
                for act in actions : self(act)
            outpt = None
            inpt = input("\033[96m>>> ").split(" ")
            n = 0
            n_max = len(inpt) - 1
            actions = []
            is_multiple = False
            for x in inpt :
                if '[' in x :
                    is_multiple = True
            if is_multiple :
                new_actions = []
                argument = []
                while n <= n_max :
                    if inpt[n][0] == '[' :
                        arguments = []
                        while inpt[n][-1] != ']' and n <= n_max :
                            arguments.append(inpt[n].removeprefix('['))
                            n += 1
                        arguments.append(inpt[n][:-1])
                        for x in arguments :
                            new_actions.append(argument + [x])
                    else : argument.append(inpt[n])
                    n += 1
                actions = new_actions
            else :
                new_action = []
                while n <= n_max :
                    if inpt[n][0] == '"' :
                        argument = ""
                        while inpt[n][-1] != '"' and n <= n_max :
                            argument += inpt[n].removeprefix('"') + " "
                            n += 1
                        argument += inpt[n][:-1]
                    else : argument = inpt[n]
                    new_action.append(argument)
                    n += 1
                actions = [new_action]
            print("\033[0m", end = "")