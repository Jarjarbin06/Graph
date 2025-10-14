# Graph v1.2
###### by JARJARBIN's studio
**Graph** is a tool to manipulate graphs in python

---
---

### SUMMARY

- [1. IMPORT](#1.%20IMPORT)

- [2. INTERPRETER](#2.%20INTERPRETER)
	- [2.1. **__init__**](#2.1.%20**__init__**)
	- [2.2. **__str__**](#2.2.%20**__str__**)
	- [2.3. **__getitem__**](#2.3.%20**__getitem__**)
	- [2.4. **__call__**](#2.4.%20**__call__**)
	- [2.5. **add**](#2.5.%20**add**)
	- [2.6. **delete**](#2.6.%20**delete**)
	- [2.7. **start**](#2.7.%20**start**)

- [3. GRAPH](#3.%20GRAPH)
	- [3.1. **__init__**](#3.1.%20**__init__**)
	- [3.2. **__str__**](#3.2.%20**__str__**)
	- [3.3. **__getitem__**](#3.3.%20**__getitem__**)
	- [3.4. **__call__**](#3.4.%20**__call__**)
	- [3.5. **add**](#3.5.%20**add**)
	- [3.6. **delete**](#3.6.%20**delete**)
	- [3.7. **link**](#3.7.%20**link**)
	- [3.8. **unlink**](#3.8.%20**unlink**)
	- [3.9. **new_data**](#3.9.%20**new_data**)
	- [3.10. **new_pos**](#3.10.%20**new_pos**)
	- [3.11. **update**](#3.11.%20**update**)
	- [3.12. **get_nodes**](#3.12.%20**get_nodes**)
	- [3.13. **get_ordre**](#3.13.%20**get_ordre**)
	- [3.14. **get_links**](#3.14.%20**get_links**)
	- [3.15. **get_data**](#3.15.%20**get_data**)

- [4. NODE](#4.%20NODE)
	- [4.1. **__init__**](#4.1.%20**__init__**)
	- [4.2. **__str__**](#4.2.%20**__str__**)
	- [4.3. **add**](#4.3.%20**add**)
	- [4.4. **delete**](#4.4.%20**delete**)
	- [4.5. **delete_all**](#4.5.%20**delete_all**)
	- [4.6. **get_links**](#4.6.%20**get_links**)
	- [4.7. **get_data**](#4.7.%20**get_data**)

- [5. GUI](#5.%20GUI)
	- [5.1. **show**](#5.1.%20**show**)
	- [5.2. **get_nodes_pos**](#5.2.%20**get_nodes_pos**)

- [6. CMDError](#6.%20CMDError)
	- [6.1. **__init__**](#6.1.%20**__init__**)
	- [6.2. **__str__**](#6.2.%20**__str__**)

- [7. EXAMPLE](#7.%20EXAMPLE)

---
---

### 1. IMPORT
To import this module in your program, you just need to put these lines in your code :
```py
from CMDError import CMDError
from GUI import GUI
from Node import Node
from Graph import Graph
from Interpreter import Interpreter
```

---
---

### 2. INTERPRETER
The class [*Interpreter*](#2.%20INTERPRETER) is to be used as a command interpreter in a command window.
Use **start()** to lauch the command prompt interpreter.

(child(s) = / ; parent(s) = /)

---
#### SUMMARY

- [2.1. **__init__**](#2.1.%20**__init__**)
- [2.2. **__str__**](#2.2.%20**__str__**)
- [2.3. **__getitem__**](#2.3.%20**__getitem__**)
- [2.4. **__call__**](#2.4.%20**__call__**)
- [2.5. **add**](#2.5.%20**add**)
- [2.6. **delete**](#2.6.%20**delete**)
- [2.7. **start**](#2.7.%20**start**)

---
#### 2.1. **__init__**
Create an instance of [*Interpreter*](#2.%20INTERPRETER) named ==name==
```
__init__(self : object, name : str | None)
	-> None
```
###### Parameter :
- ==self== (**object**) : instance of [*Interpreter*](#2.%20INTERPRETER)
- ==name== (**str** | **None**) = **None** : name of the new [*Interpreter*](#2.%20INTERPRETER)
###### Return :
- **None**

###### Usage :
```py
VarMyInterpreter = Interpreter()
```
or
```py
VarMyInterpreter = Interpreter("MyNewInterpreter")
```
or
```py
Interpreter("MyNewInterpreter")
VarMyInterpreter = Interpreter.interpreter_list["MyNewInterpreter"]
```

---
#### 2.2. **__str__**
Return a chain of characters
```
__str__(self : object)
	-> str
```
###### Parameter :
- ==self== (**object**) : instance of [*Interpreter*](#2.%20INTERPRETER)
###### Return :
- **str**

###### Usage :
```py
MyString = VarMyInterpreter.__str__()
print(MyString)
```
or
```py
print(VarMyInterpreter)
```

---
#### 2.3. **__getitem__**
Get an instance of [*Graph*](#3.%20GRAPH) named ==name==
```
__getitem__(self : object, name : str)
	-> Graph
```
###### Parameter :
- ==self== (**object**) : instance of [*Interpreter*](#2.%20INTERPRETER)
- ==name== (**str**) : name of the [*Graph*](#3.%20GRAPH)
###### Return :
- **[*Graph*](#3.%20GRAPH)**

###### Usage :
```py
MyGraph = VarMyInterpreter.__getitem__("MyGraph")
```
or
```py
MyGraph = VarMyInterpreter["MyGraph"]
```

---
#### 2.4. **__call__**
Execute all commands in ==instructions== and return the results if there are any
```
__call__(self : object, instructions : list[str])
	-> any
```
###### Parameter :
- ==self== (**object**) : instance of [*Interpreter*](#2.%20INTERPRETER)
- ==instructions== (**list**[**str**]) : commands to execute
###### Return :
- **any**

###### Usage :
```py
MyCommandReturn = VarMyInterpreter("MyCommand")
```
or
```py
MyCommandsReturn = VarMyInterpreter(["MyCommand1", "MyCommand2"])
```
or
```py
MyCommandReturn = VarMyInterpreter.__call__("MyCommand")
```

---
#### 2.5. **add**
Create and add a [*Graph*](#3.%20GRAPH) named ==name==
```
add(self : object, name : str)
	-> None
```
###### Parameter :
- ==self== (**object**) : instance of [*Interpreter*](#2.%20INTERPRETER)
- ==name== (**str**) : name of the new [*Graph*](#3.%20GRAPH)
###### Return :
- **None**

###### Usage :
```py
VarMyInterpreter.add("MyNewGraph")
```

---
#### 2.6. **delete**
Delete an instance of [*Graph*](#3.%20GRAPH) named ==name==
```
delete(self : object, name : str)
	-> None
```
###### Parameter :
- ==self== (**object**) : instance of [*Interpreter*](#2.%20INTERPRETER)
- ==name== (**str**) : name of the [*Graph*](#3.%20GRAPH)
###### Return :
- **None**

###### Usage :
```py
VarMyInterpreter.delete("MyOldGraph")
```

---
#### 2.7. **start**
Start a command interpreter (type "help" to see commands)
```
start(self : object)
	-> None
```
###### Parameter :
- ==self== (**object**) : instance of [*Interpreter*](#2.%20INTERPRETER)
###### Return :
- **None**

###### Usage :
```py
VarMyInterpreter.start()
```

---
---

### 3. GRAPH
The class [*Graph*](#3.%20GRAPH) is to create and manipulate graphs.

(child(s) = / ; parent(s) = [*GUI*](#5.%20GUI))

---
#### SUMMARY

- [3.1. **__init__**](#3.1.%20**__init__**)
- [3.2. **__str__**](#3.2.%20**__str__**)
- [3.3. **__getitem__**](#3.3.%20**__getitem__**)
- [3.4. **__call__**](#3.4.%20**__call__**)
- [3.5. **add**](#3.5.%20**add**)
- [3.6. **delete**](#3.6.%20**delete**)
- [3.7. **link**](#3.7.%20**link**)
- [3.8. **unlink**](#3.8.%20**unlink**)
- [3.9. **new_data**](#3.9.%20**new_data**)
- [3.10. **new_pos**](#3.10.%20**new_pos**)
- [3.11. **update**](#3.11.%20**update**)
- [3.12. **get_nodes**](#3.12.%20**get_nodes**)
- [3.13. **get_ordre**](#3.13.%20**get_ordre**)
- [3.14. **get_links**](#3.14.%20**get_links**)
- [3.15. **get_data**](#3.15.%20**get_data**)

---
#### 3.1. **__init__**
Create an instance of [*Graph*](#3.%20GRAPH)
```
__init__(self : object)
	-> None
```
###### Parameter :
- ==self== (**object**) : instance of [*Graph*](#3.%20GRAPH)
###### Return :
- **None**

###### Usage :
```py
VarMyGraph = Graph("MyNewGraph")
```

---
#### 3.2. **__str__**
Return a chain of characters
```
__str__(self : object)
	-> str
```
###### Parameter :
- ==self== (**object**) : instance of [*Graph*](#3.%20GRAPH)
###### Return :
- **str**

###### Usage :
```py
MyString = VarMyGraph.__str__()
print(MyString)
```
or
```py
print(VarMyGraph)
```

---
#### 3.3. **__getitem__**
Get an instance of [*Node*](#4.%20NODE) named ==node==
```
__getitem__(self : object, node : str)
	-> Node
```
###### Parameter :
- ==self== (**object**) : instance of [*Graph*](#3.%20GRAPH)
- ==node== (**str**) : name of the [*Node*](#4.%20NODE)
###### Return :
- **[*Node*](#4.%20NODE)**

###### Usage :
```py
MyNode = VarMyGraph.__getitem__("MyNode")
```
or
```py
MyNode = VarMyGraph["MyNode"]
```

---
#### 3.4. **__call__**
Execute all commands in ==instructions_list== and return the results if there are any
```
__call__(self : object, instructions_list : list[str])
	-> any
```
###### Parameter :
- ==self== (**object**) : instance of [*Graph*](#3.%20GRAPH)
- ==instructions_list== (**list**[**str**]) : commands to execute
###### Return :
- **any**

###### Usage :
```py
MyCommandReturn = VarMyGraph("MyCommand")
```
or
```py
MyCommandsReturn = VarMyGraph(["MyCommand1", "MyCommand2"])
```
or
```py
MyCommandReturn = VarMyGraph.__call__("MyCommand")
```

---
#### 3.5. **add**
Create and add a [*Node*](#4.%20NODE) named ==name== with data ==data==
```
add(self : object, name : str, data : any)
	-> None
```
###### Parameter :
- ==self== (**object**) : instance of [*Graph*](#3.%20GRAPH)
- ==name== (**str**) : name of the new [*Node*](#4.%20NODE)
- ==data== (**any**) = **"\033[31mNo data\033[0m"** : data of the new [*Node*](#4.%20NODE)
###### Return :
- **None**

###### Usage :
```py
VarMyGraph.add("MyNewNode")
```
or
```py
VarMyGraph.add("MyNewNode", "MyNewData")
```

---
#### 3.6. **delete**
Delete an instance of [*Node*](#4.%20NODE) named ==node==
```
delete(self : object, node : str)
	-> None
```
###### Parameter :
- ==self== (**object**) : instance of [*Graph*](#3.%20GRAPH)
- ==node== (**str**) : name of the [*Node*](#4.%20NODE)
###### Return :
- **None**

###### Usage :
```py
VarMyGraph.delete("MyOldNode")
```

---
#### 3.7. **link**
Link an instance of [*Node*](#4.%20NODE) named ==link_from== to one or more instances of [*Node*](#4.%20NODE) named ==link2==
```
link(self : object, link_from : str, link2 : str | list[str])
	-> None
```
###### Parameter :
- ==self== (**object**) : instance of [*Graph*](#3.%20GRAPH)
- ==link_from== (**str**) : name of the [*Node*](#4.%20NODE)
- ==link2== (**str** | **list**[**str**]) : name of the [*Node*](#4.%20NODE)(s)
###### Return :
- **None**

###### Usage :
```py
VarMyGraph.link("MyNode", "MyOtherNode")
```
or
```py
VarMyGraph.link("MyNode", ["MyOtherNode1", "MyOtherNode2"])
```

---
#### 3.8. **unlink**
Unlink an instance of [*Node*](#4.%20NODE) named ==link_from== to one or more instances of [*Node*](#4.%20NODE) named ==link2== (if ==link2== is **None**, unlink to all instances of [*Node*](#4.%20NODE))
```
link(self : object, link_from : str, link2 : str | list[str] | None)
	-> None
```
###### Parameter :
- ==self== (**object**) : instance of [*Graph*](#3.%20GRAPH)
- ==link_from== (**str**) : name of the [*Node*](#4.%20NODE)
- ==link2== (**str** | **list**[**str**] | **None**) = **None** : name of the [*Node*](#4.%20NODE)(s)
###### Return :
- **None**

###### Usage :
```py
VarMyGraph.unlink("MyNode")
```
or
```py
VarMyGraph.unlink("MyNode", "MyOtherNode")
```
or
```py
VarMyGraph.unlink("MyNode", ["MyOtherNode1", "MyOtherNode2"])
```

---
#### 3.9. **new_data**
Change the data of an instance of [*Node*](#4.%20NODE) named ==node== to ==data==
```
new_data(self : object, node : str, data : any)
	-> None
```
###### Parameter :
- ==self== (**object**) : instance of [*Graph*](#3.%20GRAPH)
- ==node== (**str**) : name of the [*Node*](#4.%20NODE)
- ==data== (**any**) = **"\033[31mNo data\033[0m"** : new data of the [*Node*](#4.%20NODE)
###### Return :
- **None**

###### Usage :
```py
VarMyGraph.new_data("MyNode", MyNewData)
```

---
#### 3.10. **new_pos**
Change the x and y position of an instance of [*Node*](#4.%20NODE) named ==node== to ==pos_x== and ==pos_y==
```
new_pos(self : object, node : str, pos_x : int | float | None, pos_y : int | float | None)
	-> None
```
###### Parameter :
- ==self== (**object**) : instance of [*Graph*](#3.%20GRAPH)
- ==node== (**str**) : name of the [*Node*](#4.%20NODE)
- ==pos_x== (**int** | **float** | **None**) : position on the x axis of the [*Node*](#4.%20NODE)
- ==pos_y== (**int** | **float** | **None**) : position on the y axis of the [*Node*](#4.%20NODE)
###### Return :
- **None**

###### Usage :
```py
VarMyGraph.new_pos("MyNode", MyNewPosX, MyNewPosY)
```

---
#### 3.11. **update**
Update all informations about an instance of [*Graph*](#3.%20GRAPH)
```
update(self : object)
	-> None
```
###### Parameter :
- ==self== (**object**) : instance of [*Graph*](#3.%20GRAPH)
###### Return :
- **None**

###### Usage :
```py
VarMyGraph.update()
```

---
#### 3.12. **get_nodes**
Get a list of name of all instances of [*Node*](#4.%20NODE)
```
get_nodes(self : object)
	-> list[str]
```
###### Parameter :
- ==self== (**object**) : instance of [*Graph*](#3.%20GRAPH)
###### Return :
- **list**

###### Usage :
```py
MyGraphNodes = VarMyGraph.get_nodes()
```

---
#### 3.13. **get_ordre**
Get the amount of instances of [*Node*](#4.%20NODE)
```
get_ordre(self : object)
	-> int
```
###### Parameter :
- ==self== (**object**) : instance of [*Graph*](#3.%20GRAPH)
###### Return :
- **int**

###### Usage :
```py
MyGraphOrdre = VarMyGraph.get_size()
```

---
#### 3.14. **get_links**
Get a list of name of all instances of [*Node*](#4.%20NODE) linked to an instance of [*Node*](#4.%20NODE) named ==node==
```
get_links(self : object, node : str)
	-> list
```
###### Parameter :
- ==self== (**object**) : instance of [*Graph*](#3.%20GRAPH)
- ==node== (**str**) : name of the [*Node*](#4.%20NODE)
###### Return :
- **list**

###### Usage :
```py
MyGraphLinks = VarMyGraph.get_links("MyNode")
```

---
#### 3.15. **get_data**
Get the data of an instance of [*Node*](#4.%20NODE) named ==node==
```
get_data(self : object, node : str)
	-> any
```
###### Parameter :
- ==self== (**object**) : instance of [*Graph*](#3.%20GRAPH)
- ==node== (**str**) : name of the [*Node*](#4.%20NODE)
###### Return :
- **any**

###### Usage :
```py
MyGraphData = VarMyGraph.get_data("MyNode")
```

---
---

### 4. NODE
The class [*Node*](#4.%20NODE) is to create and manipulate nodes in a [*Graph*](#3.%20GRAPH).

(child(s) = / ; parent(s) = /)

---
#### SUMMARY

- [4.1. **__init__**](#4.1.%20**__init__**)
- [4.2. **__str__**](#4.2.%20**__str__**)
- [4.3. **add**](#4.3.%20**add**)
- [4.4. **delete**](#4.4.%20**delete**)
- [4.5. **delete_all**](#4.5.%20**delete_all**)
- [4.6. **get_links**](#4.6.%20**get_links**)
- [4.7. **get_data**](#4.7.%20**get_data**)

---
#### 4.1. **__init__**
Create an instance of [*Node*](#4.%20NODE)
```
__init__(self : object, name : str, *, data : any, pos : tuple[int | float | None, int | float | None])
	-> None
```
###### Parameter :
- ==self== (**object**) : instance of [*Node*](#4.%20NODE)
- ==name== (**str**) : name of the new [*Node*](#4.%20NODE)
###### Optional :
- ==data== (**any**) = **"\033[31mNo data\033[0m"** : data of the new [*Node*](#4.%20NODE)
- ==pos== (**tuple**[**int** | **float** | **None**, **int** | **float** | **None**]) = **(None, None)** : position of the new [*Node*](#4.%20NODE)
###### Return :
- **None**

###### Usage :
```py
VarMyNode = Node("MyNewNode")
```
or
```py
VarMyNode = Node("MyNewNode", data = "MyNewData")
```
or
```py
VarMyNode = Node("MyNewNode", data = "MyNewData", pos = (MyNewPosX, MyNewPosY))
```

---
#### 4.2. **__str__**
Return a chain of characters
```
__str__(self : object)
	-> str
```
###### Parameter :
- ==self== (**object**) : instance of [*Node*](#4.%20NODE)
###### Return :
- **str**

###### Usage :
```py
MyString = VarMyNode.__str__()
print(MyString)
```
or
```py
print(VarMyNode)
```

---
#### 4.3. **add**
Create a link to an instance of [*Node*](#4.%20NODE)
```
add(self : object, link2 : object)
	-> None
```
###### Parameter :
- ==self== (**object**) : instance of [*Node*](#4.%20NODE)
- ==link2== (**object**) : instance of [*Node*](#4.%20NODE)
###### Return :
- **None**

###### Usage :
```py
VarMyNode.add(VarMyOtherNode)
```

---
#### 4.4. **delete**
Delete a link to an instance of [*Node*](#4.%20NODE)
```
delete(self : object, link2 : object)
	-> None
```
###### Parameter :
- ==self== (**object**) : instance of [*Node*](#4.%20NODE)
- ==link2== (**object**) : instance of [*Node*](#4.%20NODE)
###### Return :
- **None**

###### Usage :
```py
VarMyNode.delete(VarMyOtherNode)
```

---
#### 4.5. **delete_all**
Delete all links from an instance of [*Node*](#4.%20NODE) to all instances of [*Node*](#4.%20NODE)
```
delete(self : object)
	-> None
```
###### Parameter :
- ==self== (**object**) : instance of [*Node*](#4.%20NODE)
###### Return :
- **None**

###### Usage :
```py
VarMyNode.delete_all()
```

---
#### 4.6. **get_links**
Get a list of all links form an instance of [*Node*](#4.%20NODE) to other instances of [*Node*](#4.%20NODE)
```
get_links(self : object)
	-> list
```
###### Parameter :
- ==self== (**object**) : instance of [*Node*](#4.%20NODE)
###### Return :
- **list**

###### Usage :
```py
MyNodeLinks = VarMyNode.get_links()
```

---
#### 4.7. **get_data**
Get the data of an instance of [*Node*](#4.%20NODE)
```
get_data(self : object)
	-> any
```
###### Parameter :
- ==self== (**object**) : instance of [*Node*](#4.%20NODE)
###### Return :
- **any**

###### Usage :
```py
MyNodeData = VarMyNode.get_data()
```

---
---

### 5. GUI
The class [*GUI*](#5.%20GUI) is to show graphs in a GUI window.

(child(s) = [*Graph*](#3.%20GRAPH) ; parent(s) = /)

---
#### SUMMARY

- [5.1. **show**](#5.1.%20**show**)
- [5.2. **get_nodes_pos**](#5.2.%20**get_nodes_pos**)

---
#### 5.1. **show**
Show an instance of [*Graph*](#3.%20GRAPH) as a circle in a pyplot window
```
__init__(self : object, r : int | float)
	-> None
```
###### Parameter :
- ==self== (**object**) : instance of [*Graph*](#3.%20GRAPH)
- ==r== (**int** | **float**) = **10** : radius of the circle
###### Return :
- **None**

###### Usage :
```py
GUI.show(VarMyGraph)
```
or
```py
GUI.show(VarMyGraph, 5)
```
or
```py
VarMyGraph.show()
```
or
```py
VarMyGraph.show(5)
```

---
#### 5.2. **get_nodes_pos**
Get the x and y position of all instances of [*Node*](#4.%20NODE) in an instance of [*Graph*](#3.%20GRAPH)
```
__str__(self : object)
	-> dict
```
###### Parameter :
- ==self== (**object**) : instance of [*Graph*](#3.%20GRAPH)
###### Return :
- **dict**

###### Usage :
```py
MyNodesPos = GUI.get_nodes_pos(VarMyGraph)
```
or
```py
MyNodesPos = VarMyGraph.get_nodes_pos()
```

---
---

### 6. CMDError
The class [*CMDError*](#6.%20CMDError) is to create error exceptions in command prompts.

(child(s) = / ; parent(s) = *Exception*)

---
#### SUMMARY

- [6.1. **__init__**](#6.1.%20**__init__**)
- [6.2. **__str__**](#6.2.%20**__str__**)

---
#### 6.1. **__init__**
Create an instance of [*CMDError*](#6.%20CMDError)
```
__init__(self : object, cmd : list[str] | None, err_pos : int | None, msg : str | None)
	-> None
```
###### Parameter :
- ==self== (**object**) : instance of [*CMDError*](#6.%20CMDError)
- ==cmd== (**list**[**str**] | **None**) = **None** : list of every words a command line
- ==err_pos== (**int** | **None**) = **None** : index position of the word error in cmd
- ==msg== (**str** | **None**) = **None** : message to explain the error
###### Return :
- **None**

###### Usage :
```py
VarMyError = CMDError()
```
or
```py
VarMyError = CMDError(["My", "Command", "List"])
```
or
```py
VarMyError = CMDError(["My", "Command", "List"], MyErrorPosition)
```
or
```py
VarMyError = CMDError(["My", "Command", "List"], MyErrorPosition, "MyErrorMSG")
```

---
#### 6.2. **__str__**
Return a chain of characters
```
__str__(self : object)
	-> str
```
###### Parameter :
- ==self== (**object**) : instance of [*CMDError*](#6.%20CMDError)
###### Return :
- **str**

###### Usage :
```py
MyString = VarMyError.__str__()
print(MyString)
```
or
```py
print(VarMyError)
```

---
---

### 7. EXAMPLE
Here is a little program example showing and testing some aspects of the module
```py
#######################################
### Little program to test Graph.py ###
#######################################

# Import :
from importlib.machinery import SourceFileLoader
Graph = SourceFileLoader("graph", "D:\Programmation\Python\exo\graph_module\graph.py").load_module()

# Create an Interpreter :
MyInterpreter = Graph.Interpreter("Interp1") # Interpreter.__init__

# Show MyInterpreter :
print(MyInterpreter) # Interpreter.__str__

# Show a list of commands :
print(MyInterpreter(["help"])) # Interpreter.__call__
print(MyInterpreter(["help:sub"])) # Interpreter.__call__

# Create a Graph :
MyInterpreter.add("Graph1") # Interpreter.add
MyGraph = MyInterpreter["Graph1"] # Interpreter.__getitem__

# Show MyGraph :
print(MyGraph) # Graph.__str__

# Create some Nodes :
MyInterpreter(["Graph1", "add", "MyNode1"]) # Interpreter.__call__
MyInterpreter(["Graph1", "add", "MyNode2", "Data_of_MyNode2"]) # Interpreter.__call__
MyGraph(["Graph1", "add", "MyNode3", "Data_of_MyNode3"]) # Graph.__call__
MyGraph.add("MyNode4", "Data_of_MyNode4") # Graph.add

# Show MyGraph :
print(MyGraph) # Graph.__str__

# Create some links :
MyInterpreter(["Graph1", "add:l", "MyNode1", "MyNode2"]) # Interpreter.__call__
MyGraph(["Graph1", "add:l", "MyNode2", "MyNode4"]) # Graph.__call__
MyGraph.link("MyNode3", ["MyNode1", "MyNode4"]) # Graph.link

# Update MyGraph :
MyGraph.update() # Graph.update

# Show MyGraph :
print(MyGraph) # Graph.__str__

# Show MyInterpreter :
print(MyInterpreter) # Interpreter.__str__

# Show MyGraph in GUI window :
MyGraph.show() # GUI.show

```