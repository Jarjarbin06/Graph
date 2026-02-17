#############################
###                       ###
###       Graph v1.2      ###
### ----Interpreter.py----###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################

from typing import Any
from CMDError import CMDError
from Graph import Graph

class Interpreter:
    """
        Interpreter object
    """

    interpreter_list = {}

    def __init__(self: object, name: str | None = None) -> None:

        """
            create an Interpreter and add it to the created Interpreter list

            Parameter :
                - self (object) : Interpreter object
                - name (str | None
        """

        if not name:
            auto_name = 1
            while ("Interpreter" + str(auto_name)) in Interpreter.interpreter_list:
                auto_name += 1
            name = "Interpreter" + str(auto_name)
        if not name in Interpreter.interpreter_list:
            self.name = name
            self.graphs = {}
            Interpreter.interpreter_list[name] = self

    def __str__(self: object) -> str:

        """
            get a string version of Interpreter

            Parameter :
                - self (object) : Interpreter object

            Return :
                str : Interpreter
        """

        s = self.name
        for graph in self.graphs:
            s += "\n - " + graph + self.graphs[graph].__str__()
        return s

    def add(self: object, name: str) -> None:

        """
            create and add a Graph to this Interpreter

            Parameter :
                - self (object) : Interpreter object
                - name (str) : new Graph's name
        """

        self.graphs[name] = Graph()

    def __getitem__(self: object, name: str) -> Graph:

        """
            get graph by name

            Parameter :
                - self (object) : Interpreter object
                - name (str) : Graph's name

            Return :
                object : Graph
        """

        if not name in self.graphs:
            self.graphs[name] = Graph()
        return self.graphs[name]

    def delete(self: object, name: str) -> None:

        """
            delete Graph by name from this Interpreter

            Parameter :
                - self (object) : Interpreter object
                - name (str) : Graph's name
        """

        if name in self.graphs:
            self.graphs.pop(name)

    def __call__(self: object, instructions: list[str]) -> Any:

        """
            respond to given command line when calling an Interpreter object

            Parameter :
                - self (object) : Interpreter object
                - instructions (str) : command line

            Return :
                Any : return of command
        """

        from os import system
        ret = None
        inst = instructions
        cmd_list = {
            "\033[100mhelp\033[0m": "\033[92mget info about commands\033[0m (args : \033[31mNone\033[0m)",
            "\033[100mhelp:sub\033[0m": "\033[92mget info about subcommands\033[0m (args : \033[31mNone\033[0m)",
            "\033[100madd \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m or \033[100madd [\033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m\033[100m...]\033[0m": "\033[92mcreate a new graph\033[0m (args : \033[33mname\033[0m = \033[92mname of the new graph\033[0m)",
            "\033[100mdel \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m or \033[100mdel [\033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m\033[100m...]\033[0m": "\033[92mdelete a graph\033[0m (args : \033[33mname\033[0m = \033[92mname of the graph\033[0m)",
            "\033[100mget \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m": "\033[92mget a graph\033[0m (args : \033[33mname\033[0m = \033[92mname of the graph\033[0m)",
            "\033[100mshw\033[0m": "\033[92mshow the interpreter\033[0m (args : \033[31mNone\033[0m)",
            "\033[100m\033[33m{\033[3mname\033[0m\033[100m\033[33m} {\033[3msubcmd\033[0m\033[100m\033[33m}\033[0m": "\033[92msubcommand of a graph\033[0m (args : \033[33mname\033[0m = \033[92mname of the graph\033[0m ; \033[33msubcmd\033[0m = \033[92msubcommand of the graph\033[0m)",
            "\033[100mclr\033[0m": "\033[92mclear command interpreter window\033[0m (args : \033[31mNone\033[0m)",
            "\033[100mquit\033[0m or \033[100mq\033[0m": "\033[92mquit command interpreter\033[0m (args : \033[31mNone\033[0m)"
        }
        sub_cmd_list = {
            "\033[100mhelp:sub\033[0m": "\033[92mget info about subcommands\033[0m (args : \033[31mNone\033[0m)",
            "\033[100madd \033[33m{\033[3mname\033[0m\033[100m\033[33m} {\033[3mdata\033[0m\033[100m\033[33m}\033[0m": "\033[92mcreate a new node\033[0m (args : \033[33mname\033[0m = \033[92mname of the new node\033[0m ; \033[33mdata\033[0m (optional) = \033[92mdata of the new node\033[0m)",
            "\033[100madd:l \033[33m{\033[3mfrom\033[0m\033[100m\033[33m} {\033[3mto\033[0m\033[100m\033[33m}\033[0m or \033[100madd:l \033[33m{\033[3mfrom\033[0m\033[100m\033[33m}\033[0m\033[100m [\033[33m{\033[3mto\033[0m\033[100m\033[33m}\033[0m\033[100m...]\033[0m": "\033[92mcreate a one-way link from a node to another node\033[0m (args : \033[33mfrom\033[0m = \033[92mname of the starting node\033[0m ; \033[33mto\033[0m = \033[92mname of the end node\033[0m)",
            "\033[100mdel \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m": "\033[92mdelete a node and all links to it\033[0m (args : \033[33mname\033[0m = \033[92mname of the node\033[0m)",
            "\033[100mdel:l \033[33m{\033[3mfrom\033[0m\033[100m\033[33m} {\033[3mto\033[0m\033[100m\033[33m}\033[0m or \033[100mdel:l \033[33m{\033[3mfrom\033[0m\033[100m\033[33m}\033[0m\033[100m [\033[33m{\033[3mto\033[0m\033[100m\033[33m}\033[0m\033[100m...]\033[0m": "\033[92mdelete a link from a node to another node\033[0m (args : \033[33mfrom\033[0m = \033[92mname of the starting node\033[0m ; \033[33mto\033[0m = \033[92mname of the end node\033[0m)",
            "\033[100mget \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m": "\033[92mget a node\033[0m (args : \033[33mname\033[0m = \033[92mname of the node\033[0m)",
            "\033[100mget:n\033[0m": "\033[92mget all nodes' name\033[0m (args : \033[31mNone\033[0m)",
            "\033[100mget:s\033[0m": "\033[92mget graph's size\033[0m (args : \033[31mNone\033[0m)",
            "\033[100mget:l \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m": "\033[92mget all links starting from a node\033[0m (args : \033[33mname\033[0m = \033[92mname of the node\033[0m)",
            "\033[100mget:d \033[33m{\033[3mname\033[0m\033[100m\033[33m}\033[0m": "\033[92mget the data of a node\033[0m (args : \033[33mname\033[0m = \033[92mname of the node\033[0m)",
            "\033[100mupt\033[0m": "\033[92mupdate graph's info\033[0m (args : \033[31mNone\033[0m)",
            "\033[100mupt:d \033[33m{\033[3mname\033[0m\033[100m\033[33m} {\033[3mdata\033[0m\033[100m\033[33m}\033[0m": "\033[92mupdate the data of a node\033[0m (args : \033[33mname\033[0m = \033[92mname of the node\033[0m ; \033[33mdata\033[0m (optional) = \033[92mnew data of the node\033[0m)",
            "\033[100mupt:p \033[33m{\033[3mname\033[0m\033[100m\033[33m} {\033[3mpos_x\033[0m\033[100m\033[33m} {\033[3mpos_y\033[0m\033[100m\033[33m}\033[0m": "\033[92mupdate the position of a node in the GUI of the graph\033[0m (args : \033[33mname\033[0m = \033[92mname of the new node\033[0m ; \033[33mpos_x\033[0m = \033[92mposition x of the node\033[0m ; \033[33mpos_y\033[0m (optional) = \033[92mposition y of the node\033[0m)",
            "\033[100mshw\033[0m": "\033[92mshow the graph\033[0m (args : \033[31mNone\033[0m)"
        }
        if inst == [""]:
            return ""
        try:
            if inst[0] == "help":
                if len(inst) < 1 or len(inst) > 2:
                    raise CMDError(inst, None, f'argument error (needs 0 or 1, gave {len(inst) - 2})')
                if len(inst) == 1:
                    s = "\nHELP commands :"
                    for x in cmd_list:
                        s += f"\n\n - {x} :\n      {cmd_list[x]}"
                    s += "\n"
                    ret = s
                elif len(inst) == 2:
                    found = False
                    s = f"\nHELP commands : {inst[1]} :"
                    for cmd in cmd_list:
                        if inst[1] in cmd or inst[1] in cmd_list[cmd]:
                            found = True
                            s += f"\n\n - {cmd} :\n      {cmd_list[cmd]}"
                    if not found:
                        s += "\n\n   \033[31mcommand not found\033[0m"
                    s += "\n"
                    ret = s
            elif inst[0] == "help:sub":
                if len(inst) < 1 or len(inst) > 2:
                    raise CMDError(inst, None, f'argument error (needs 0 or 1, gave {len(inst) - 2})')
                if len(inst) == 1:
                    s = "\nHELP subcommands :"
                    for x in sub_cmd_list:
                        s += f"\n\n - {x} :\n      {sub_cmd_list[x]}"
                    s += "\n"
                    ret = s
                elif len(inst) == 2:
                    found = False
                    s = f"\nHELP subcommands : {inst[1]} :"
                    for cmd in sub_cmd_list:
                        if inst[1] in cmd or inst[1] in sub_cmd_list[cmd]:
                            found = True
                            s += f"\n\n - {cmd} :\n      {sub_cmd_list[cmd]}"
                    if not found:
                        s += "\n\n   \033[31msubcommand not found\033[0m"
                    s += "\n"
                    ret = s
            elif inst[0] == "add":
                if len(inst) != 2:
                    raise CMDError(inst, None, f'argument error (needs 1, gave {len(inst) - 1})')
                self.add(inst[1])
            elif inst[0] == "get":
                if len(inst) != 2:
                    raise CMDError(inst, None, f'argument error (needs 1, gave {len(inst) - 1})')
                ret = self[inst[1]]
            elif inst[0] == "del":
                if len(inst) != 2:
                    raise CMDError(inst, None, f'argument error (needs 1, gave {len(inst) - 1})')
                self.delete(inst[1])
            elif inst[0] == "shw":
                if len(inst) != 1:
                    raise CMDError(inst, None, f'argument error (needs 0, gave {len(inst) - 1})')
                ret = self.__str__()
            elif inst[0] == "welcome":
                if len(inst) != 1:
                    raise CMDError(inst, None, f'argument error (needs 0, gave {len(inst) - 1})')
                system("clear||cls")
                ret = "welcome to the command interpreter of \033[96mgraph.py\033[0m (\033[96mv1.0\033[0m)\ncreated by Jarjarbin's STUDIO\n"
            elif inst[0] == "clr":
                if len(inst) != 1:
                    raise CMDError(inst, None, f'argument error (needs 0, gave {len(inst) - 1})')
                system("clear||cls")
            elif inst[0] == "":
                ret = "\n"
            elif inst[0] in self.graphs:
                ret = self.graphs[inst[0]](inst)
            else:
                raise CMDError(inst, None, "invalid command")
        except CMDError as err:
            print(err)
            return ""
        else:
            return ret

    def start(self: object) -> None:

        """
            start an interpreter

            Parameter :
                - self (object) : Interpreter object
        """

        actions = [["welcome"]]
        while not (actions[0] in [["q"], ["quit"]]):
            if len(actions) == 1:
                output = self.__call__(actions[0])
                if output: print(output)
            else:
                for act in actions: self.__call__(act)
            actions = [[""]]
            inpt = input("\033[96m>>> ").split(" ")
            if len(inpt[0]) > 0:
                n = 0
                n_max = len(inpt) - 1
                is_multiple = False
                for x in inpt:
                    if '[' in x:
                        is_multiple = True
                if is_multiple:
                    new_actions = []
                    argument = []
                    while n <= n_max:
                        if inpt[n][0] == '[':
                            arguments = []
                            while inpt[n][-1] != ']' and n <= n_max:
                                arguments.append(inpt[n].removeprefix('['))
                                n += 1
                            arguments.append(inpt[n][:-1])
                            for x in arguments:
                                new_actions.append(argument + [x])
                        else:
                            argument.append(inpt[n])
                        n += 1
                    actions = new_actions
                else:
                    new_action = []
                    while n <= n_max:
                        if inpt[n][0] == '"':
                            argument = ""
                            while inpt[n][-1] != '"' and n <= n_max:
                                argument += inpt[n].removeprefix('"') + " "
                                n += 1
                            argument += inpt[n][:-1]
                        else:
                            argument = inpt[n]
                        new_action.append(argument)
                        n += 1
                    actions = [new_action]
            print("\033[0m", end="")