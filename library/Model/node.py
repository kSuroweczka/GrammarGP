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
    is_leaf: bool

    def __init__(self, node_type: NodeType, parent_node: 'Node' = None, children_nodes: list['Node'] = []):
        self.node_type = node_type
        self.name = node_type.name
        self.parent_node = parent_node
        self.depth = self.get_depth()
        self.children_nodes = children_nodes
        self.is_leaf = False
        
    def if_root(self):
        return self.parent_node is None

    def get_depth(self):
        if self.parent_node is None:
            return 0
        else:
            return 1 + self.parent_node.get_depth()
        
    def add_child(self, child_node: 'Node'):
        if not self.is_leaf and child_node is not None:
            if not isinstance(child_node, float) and not isinstance(child_node, bool):
                child_node.parent_node = self
            
            self.children_nodes.append(child_node)

                
    def change_parent(self, new_parent: 'Node'):
        self.parent_node.children_nodes.remove(self)
        self.parent_node = new_parent
        new_parent.children_nodes.append(self)

    

class ScopeNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, children_nodes: list[Node] = []):
        super().__init__(node_type, parent_node)
        self.children_nodes = children_nodes

    def __repr__(self):
        return f"Program:\n"
    

# var, const, expression, number
class FactorNode(Node):
    def __init__(self, node_type: NodeType, parent_node, 
                 body: Node | float = None, 
                 children_nodes: list[Node] = []):
        super().__init__(node_type, parent_node)
        self.body = body
        self.value = self.calculate()
        self.is_leaf = True
        self.children_nodes = children_nodes

    def calculate(self):
        if isinstance(self.body, ExpressionNode):
            return self.body.calculate()
        if isinstance(self.body, VarNode) or isinstance(self.body, ConstNode):
            return self.body.value
        elif isinstance(self.body, float):
            return self.body
        else:
            raise Exception(f"Unknown type: {type(self.body)}")
    
    def __repr__(self):
        if isinstance(self.body, VarNode) or isinstance(self.body, ConstNode):
            return f"{self.body}"
        return f"( {self.value} )"

    

class TermNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, 
                left: Node = None, 
                right: Node | None = None, 
                operation: str | None = None,
                children_nodes: list[Node] = []):
        super().__init__(node_type, parent_node)
        self.children_nodes = children_nodes
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
            right = self.right.value
            left = self.left.value
            if right == 0:
                return left
            return  left / right
        else:
            raise Exception(f"Unknown operation: {self.operation}")
    
        
    def __repr__(self):
        if self.operation is None:
            return f"{self.left}"
        return f"( {self.left} {self.operation} {self.right} )"
    
class ExpressionNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node = None, 
                 left: Node = None, 
                 right: Node | None = None, 
                 operation: str | None = None,
                 children_nodes: list[Node] = []):
        super().__init__(node_type, parent_node)
        self.children_nodes = children_nodes
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
    def __init__(self, node_type: NodeType, parent_node: Node, 
                 name: str, 
                 value: float | bool):
        super().__init__(node_type, parent_node)
        self.name = name
        self.value = value
        self.is_leaf = True
    
    def __repr__(self):
        return f"{self.name}" #(value: {self.value})
    
    # def copy(self):
    #     new_var = VarNode(NodeType.CONST, None, self.name, self.value)
    #     return new_var


class ConstNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, 
                 name: str, 
                 value: float | bool):
        super().__init__(node_type, parent_node)
        self.name = name
        self.value = value
        self.is_leaf = True


    def __repr__(self):
        return f"{self.name}"#(value: {self.value})
    
    # def copy(self):
    #     new_var = ConstNode(NodeType.CONST, None, self.name, self.value)
    #     return new_var
    

class AssignmentNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, 
                 var: VarNode | ConstNode, 
                 body: ExpressionNode,
                 children_nodes: list[Node] = []):
        super().__init__(node_type, parent_node)
        self.children_nodes = children_nodes
        self.var = var
        self.body = body
        self.value = self.calculate()
    
    def calculate(self):
        if isinstance(self.body, float) or isinstance(self.body, bool):
            return self.body
        return self.body.calculate()

    def change_body(self, new_body: ExpressionNode):
        self.body = new_body
        self.value = self.calculate()

    def __repr__(self):
        if self.var.node_type == NodeType.CONST:
            return f"const {self.var.name} = {self.body}"
        return f"{self.var.name} = {self.body}" # (value: {self.value})


class InputNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, children_nodes: list[AssignmentNode] = []):
        super().__init__(node_type, parent_node)
        self.children_nodes = children_nodes
        self.value = []
    
    def __repr__(self):
        input = ""
        for child in self.children_nodes:
            input += str(child) + ", "
        input = input[:-2]
        return f"input({input})"
    
    def calculate(self):
        input = []
        for child in self.children_nodes:
            input.append(child.value)
        return input


class OutputNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, children_nodes: list[VarNode | ConstNode | float | bool] = []):
        super().__init__(node_type, parent_node)
        self.children_nodes = children_nodes
        self.value = []
    
    def __repr__(self):
        output = ""
        for child in self.children_nodes:
            output += str(child) + ","
        output = output[:-1]
        return f"output({output})"
    

    def calculate(self):
        output = []
        for child in self.children_nodes:
            if isinstance(child, VarNode) or isinstance(child, ConstNode):
                output.append(child.value)
            elif isinstance(child, float) or isinstance(child, bool):
                output.append(child)
            else:
                raise Exception(f"Unknown type: {type(child)}")
        return output




#TO DO

# class ConditionNode(Node):
#     def __init__(self, node_type: NodeType, parent_node: Node, left: Node = None, right: Node = None, condition: str = None):
#         super().__init__(node_type, parent_node)
#         self.left = left
#         self.right = right
#         self.condition = condition

#     def __repr__(self):
#         return f"{self.left} {self.condition} {self.right}"


# class IfNode(Node):
#     def __init__(self, name: str, condition: ConditionNode, if_node: Node, else_node: Node):
#         self.name = name
#         self.condition = condition
#         self.if_node = if_node
#         self.else_node = else_node
    
#     def __rep__(self):
#         return f"if {self.condition}:\n {self.if_node}\nelse:\n {self.else_node}\n"


# CHECK IF NESSESARY

# class TerminalNode(Node):
#     def __init__(self, value: float | bool, parent_node: Node = None, children_nodes
#: list[Node] = []):
#         super().__init__(NodeType.TERMINAL, parent_node, children_nodes)
#         self.is_leaf = True
#         self.value = value

#     def __repr__(self):
#         return f"{self.value}"
    
#     def is_numeral(self):
#         return isinstance(self.value, float)
    
#     def is_boolean(self):
#         return isinstance(self.value, bool)