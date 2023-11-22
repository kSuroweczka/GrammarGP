from enum import Enum

class NodeType(Enum):
    SCOPE = 0,
    VAR = 1,
    CONST = 2,
    INPUT = 3,
    OUTPUT = 4,
    CONDITION = 5,
    IF = 6,
    TERMINAL = 7,
    FACTOR = 8,
    TERM = 9,
    EXPRESSION = 10,
    ASSIGNMENT = 11,


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

    def change_parent(self, new_parent: 'Node'):
        self.parent_node.children_nodes.remove(self)
        self.parent_node = new_parent
        new_parent.children_nodes.append(self)


class TerminalNode(Node):
    def __init__(self, value: float | bool):
        super().__init__(NodeType.TERMINAL, None)
        self.is_leaf = True
        self.value = value

    def __repr__(self):
        return f"{self.value}"
    
    def is_numeral(self):
        return isinstance(self.value, float)
    
    def is_boolean(self):
        return isinstance(self.value, bool)
    

class ScopeNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node):
        super().__init__(node_type, parent_node)
        self.children_nodes = []

    def __repr__(self):
        return f"Program:\n"

# var, const, expression, number
class FactorNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, body: Node):
        super().__init__(node_type, parent_node)
        self.body = body
        self.value = self.calculate()

    def calculate(self):
        return self.body.value
    
    def __repr__(self):
        return f"( {self.value} )"
    

class TermNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, 
                left: Node, 
                right: Node | None, 
                operation: str | None):
        super().__init__(node_type, parent_node)
        self.left = left
        self.right = right
        self.operation = operation
        self.value = self.calculate()
    
    def calculate(self):
        if self.operation is None:
            return self.left.value
        elif self.operation == '*':
            return self.left.value * self.right.value
        elif self.operation == '/':
            return self.left.value / self.right.value
        else:
            raise Exception(f"Unknown operation: {self.operation}")
        
    def __repr__(self):
        if self.operation is None:
            return f"{self.left}"
        return f"{self.left} {self.operation} {self.right}"
    
class ExpressionNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, 
                 left: Node, 
                 right: Node | None, 
                 operation: str | None):
        super().__init__(node_type, parent_node)
        self.left = left
        self.right = right
        self.operation = operation
        self.value = self.calculate()
    
    def calculate(self):
        if self.operation is None:
            return self.left.value
        elif self.operation == '+':
            return self.left.value + self.right.value
        elif self.operation == '-':
            return self.left.value - self.right.value
        else:
            raise Exception(f"Unknown operation: {self.operation}")
        
    def __repr__(self):
        if self.operation is None:
            return f"{self.left}"
        return f"( {self.left} {self.operation} {self.right} )"


class VarNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, name: str, value: ExpressionNode):
        super().__init__(node_type, parent_node)
        self.name = name
        self.value = value
    
    def __repr__(self):
        return f"{self.name} = {self.value}"


class ConstNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, name: str, value: ExpressionNode):
        super().__init__(node_type, parent_node)
        self.name = name
        self.value = value

    def __repr__(self):
        return f"const {self.name} = {self.value}"
    

class AssignmentNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, var_name: str, body: ExpressionNode):
        super().__init__(node_type, parent_node)
        self.var_name = var_name
        self.body = body
        self.value = self.calculate()
    
    def calculate(self):
        return self.body.calculate()
    
    def __repr__(self):
        return f"{self.var_name} = {self.body} (value: {self.value})"


class InputNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, value: list[VarNode]):
        super().__init__(node_type, parent_node)
        self.value = value
    
    def __repr__(self):
        return f"input({self.value})"


class OutputNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, value: list[TerminalNode]):
        super().__init__(node_type, parent_node)
        self.value = value
    
    def __repr__(self):
        return f"output({self.value})"


class ConditionNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, left: Node = None, right: Node = None, condition: str = None):
        super().__init__(node_type, parent_node)
        self.left = left
        self.right = right
        self.condition = condition

    def __repr__(self):
        return f"{self.left} {self.condition} {self.right}"


class IfNode(Node):
    def __init__(self, name: str, condition: ConditionNode, if_node: Node, else_node: Node):
        self.name = name
        self.condition = condition
        self.if_node = if_node
        self.else_node = else_node
    
    def __rep__(self):
        return f"if {self.condition}:\n {self.if_node}\nelse:\n {self.else_node}\n"


