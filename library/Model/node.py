from enum import Enum

class NodeType(Enum):
    SCOPE = 0,
    VAR = 1,
    CONST = 2,
    INPUT = 3,
    OUTPUT = 4,

class Node:
    parent_node: 'Node'
    children_nodes: list['Node']
    name: str
    node_type: NodeType
    depth: int
    is_root: bool
    is_leaf: bool = False

    def __init__(self, node_type: NodeType, parent_node: 'Node'):
        self.node_type = node_type
        self.name = node_type.name
        self.parent_node = parent_node
        self.depth = self.get_depth()
        
    def if_root(self):
        return self.parent_node is None

    def get_depth(self):
        if self.parent_node is None:
            return 0
        else:
            return 1 + self.parent_node.get_depth()
        
    def add_child(self, child_node: 'Node'):
        if not self.is_leaf:
            self.children_nodes.append(child_node)
            child_node.parent_node = self


class ScopeNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node):
        super().__init__(node_type, parent_node)
        self.children_nodes = []

    def __repr__(self):
        return f"Program:\n"


class InputNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, value: list[float]):
        super().__init__(node_type, parent_node)
        self.value = value
    
    def __repr__(self):
        return f"input({self.value})"
    
class OutputNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, value: list[float]):
        super().__init__(node_type, parent_node)
        self.value = value
    
    def __repr__(self):
        return f"output({self.value})"
    
class VarNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, name: str, value: float):
        super().__init__(node_type, parent_node)
        self.name = name
        self.value = value
    
    def __repr__(self):
        return f"{self.name} = {self.value}"
    
class ConstNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, name: str, value: float):
        super().__init__(node_type, parent_node)
        self.name = name
        self.value = value

    def __repr__(self):
        return f"const {self.name} = {self.value}"
    
# def IfNode(Node):
#     def __init__(self, name: str, condition: ConditionNode, if_node: Node, else_node: Node):
#         self.name = name
#         self.condition = condition
#         self.if_node = if_node
#         self.else_node = else_node
    
#     def __rep__(self):
#         return f"if {self.condition}:\n {self.if_node}\nelse:\n {self.else_node}\n"

# def ConditionNode(Node):
#     def __init__(self, name: str, condition: str):
#         self.name = name
#         self.condition = condition

    
#     def __rep__(self):
#         return f"{self.condition}\n"

