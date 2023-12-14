from enum import Enum

class NodeType(Enum):
    SCOPE = 0,
    VAR = 1,
    INPUT = 3,
    OUTPUT = 4,
    CONDITION = 5,
    IF = 6,
    TERMINAL = 7,
    FACTOR = 8,
    TERM = 9,
    EXPRESSION = 10,
    ASSIGNMENT = 11,
    OPERATOR = 12,
    LOGICOPERATOR=13,
    BOOLEAN = 14,
    EXPRESSIONCONDITION=15
    LOGICCONDITION=16,
    WHILE =17


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
        self.is_root = self.if_root()
        
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
        if self.parent_node is None:
            return
        if self.parent_node.children_nodes is not None:
            self.parent_node.children_nodes.remove(self)
        self.parent_node = new_parent
        new_parent.children_nodes.append(self)
        self.depth = self.get_depth()
        self.is_root = self.if_root()

    

class ScopeNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, children_nodes: list[Node] = []):
        super().__init__(node_type, parent_node)
        self.children_nodes = children_nodes
        self.parent_node = parent_node

    def __repr__(self) -> str:
        output = "{\n"
        for child in self.children_nodes:
            spaces = child.depth * "  "
            output += f"{spaces}{child}\n" # {: 

        closeSpaces = (self.depth - 2) * "  "
        return output+closeSpaces+"}"

    

# var, const, expression, number
class FactorNode(Node):
    def __init__(self, node_type: NodeType, parent_node, 
                 body: Node | float | bool = None, 
                 children_nodes: list[Node] = []):
        super().__init__(node_type, parent_node)
        self.body = body
        self.value = self.calculate()
        self.is_leaf = True
        self.children_nodes = children_nodes
        self.parent_node = parent_node

    def calculate(self):
        if isinstance(self.body, ExpressionNode):
            return self.body.calculate()
        if isinstance(self.body, VarNode):
            return self.body.value
        elif isinstance(self.body, float):
            return self.body
        elif isinstance(self.body, bool):
            return float(self.body)
        else:
            raise Exception(f"Unknown type: {type(self.body)}")
    
    def __repr__(self):
        if isinstance(self.body, VarNode) | isinstance(self.body, bool):
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
        self.parent_node = parent_node
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
        self.parent_node = parent_node
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
        self.parent_node = parent_node
        self.name = name
        self.value = value
        self.is_leaf = True
    
    def __repr__(self):
        return f"{self.name}" #(value: {self.value})

    
class InputNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, index: int = 0):
        super().__init__(node_type, parent_node)
        self.parent_node = parent_node
        self.value: float | bool = None, 
        self.is_leaf = True

    def __repr__(self):
        return f"input()"
    
    def calculate(self):
        return self.value


class AssignmentNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, 
                 var: VarNode = None, 
                 body: ExpressionNode | float | bool | InputNode = None,
                 children_nodes: list[Node] = []):
        super().__init__(node_type, parent_node)
        self.parent_node = parent_node
        self.children_nodes = children_nodes
        self.var = var
        self.body = body
        self.value = self.calculate()
    
    def calculate(self):
        if isinstance(self.body, float) or isinstance(self.body, bool):
            return self.body
        if self.body == None:
            return None
        return self.body.calculate()

    def change_body(self, new_body: ExpressionNode):
        self.body = new_body
        self.value = self.calculate()

    def __repr__(self):
        if self.var == None:
            return "dupa jasia"
        
        return f"{self.var.name} = {self.body} (value: {self.value})" # 



class OutputNode(Node):
    def __init__(self, node_type: NodeType, parent_node: Node, children_nodes: list[VarNode | float | bool] = []):
        super().__init__(node_type, parent_node)
        self.parent_node = parent_node
        self.children_nodes = children_nodes
        self.value = []
    
    def __repr__(self):
        output = ""
        for child in self.children_nodes:
            output += str(child) + ","
        output = output[:-1]
        # some problem with output - needed to add 2 spaces before output
        return f"  output({output})"
    

    def calculate(self):
        output = []
        for child in self.children_nodes:
            if isinstance(child, VarNode):
                output.append(child.value)
            elif isinstance(child, float) or isinstance(child, bool):
                output.append(child)
            else:
                raise Exception(f"Unknown type: {type(child)}")
        return output



class ExpressionConditionNode(Node):
    def __init__(self, node_type: NodeType, 
                 parent_node: Node = None, 
                 children_nodes: list[Node] = [], 
                 leftExpression:ExpressionNode=None, 
                 rigthExpression: ExpressionNode=None,
                 operator: str=None):
        super().__init__(node_type, parent_node, children_nodes)
        self.parent_node = parent_node
        self.leftExpression = leftExpression
        self.rightExpression = rigthExpression
        self.operator = operator
        self.value = self.calculate()
        
    def __repr__(self) -> str:
        output = ""
        output += f'{self.children_nodes[0]} '
        output += self.operator
        output += f' {self.children_nodes[1]}'
        return output
    
    def calculate(self):
        if self.operator == '<':
            return self.leftExpression.value < self.rightExpression.value
        elif self.operator == '>':
            return self.leftExpression.value > self.rightExpression.value
        elif self.operator == '==':
            return self.leftExpression.value == self.rightExpression.value
        elif self.operator == '!=':
            return self.leftExpression.value != self.rightExpression.value
        elif self.operator == '<=':
            return self.leftExpression.value <= self.rightExpression.value
        elif self.operator == '>=':
            return self.leftExpression.value >= self.rightExpression.value
        else:
            raise Exception(f"Unknown operation: {self.operator}")


class ConditionNode(Node):
    def __init__(self, node_type: NodeType, 
                 parent_node: Node,
                logicOperators: list[str],
                children_nodes:list[Node]=None):  
        
        super().__init__(node_type, parent_node)
        self.parent_node = parent_node
        self.children_nodes = children_nodes
        self.logicOperators = logicOperators
        self.value = self.calculate()

    def __repr__(self) -> str:
        output = "( "
        # for child in self.children_nodes:
        #     output += f"{child}"
        for i in range(len(self.children_nodes)):
            output+=f' {self.children_nodes[i]} '
            if i!=len(self.children_nodes)-1:
                output+=self.logicOperators[i]
        return output+" ) (value: "+ str(self.value) + ")"
    
    def calculate(self):
        value = self.children_nodes[0].value
        if len(self.logicOperators) > 0:
            for i in range(len(self.logicOperators)):
                if self.logicOperators[i]=='&&':
                    value = value and self.children_nodes[i+1].value
                elif self.logicOperators[i]=='||':
                    value=value or self.children_nodes[i+1].value
                else:
                    raise Exception(f"Unknown operation: {self.logicOperators[i]}")
        return value

        


class IfNode(Node):
    def __init__(self, node_type: NodeType, 
                 parent_node: Node = None, 
                 children_nodes: list[Node] = [], 
                 conditionNode: ConditionNode = None, 
                 ifBodyNode: ScopeNode | None = None, 
                 elseBodyNode: ScopeNode | None = None):
        
        super().__init__(node_type, parent_node, children_nodes)
        self.parent_node = parent_node
        self.children_nodes = children_nodes
        self.conditionNode = conditionNode
        self.ifBodyNode = ifBodyNode
        self.elseBodyNode = elseBodyNode

    def __repr__(self) -> str:
        spaces = self.depth * "  "
        output = "if "
        output += f'{self.conditionNode}'
        output += f'{self.ifBodyNode}'
        if self.elseBodyNode is not None:
            output+=f" else"
            output+=f'{spaces}{self.elseBodyNode}'
        return output
    
class WhileNode(Node):
    def __init__(self, node_type: NodeType, 
                 parent_node: Node = None, 
                 children_nodes: list[Node] = [],
                 conditionNode: ConditionNode=None,
                 whileBodyNode: ScopeNode=None):
        
        super().__init__(node_type, parent_node, children_nodes)
        self.parent_node = parent_node
        self.children_nodes = children_nodes
        self.conditionNode = conditionNode
        self.whileBodyNode = whileBodyNode
        
    def __repr__(self) -> str:
        output = "while "
        output += f'{self.conditionNode}'
        output += f'{self.whileBodyNode}'
        return output


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