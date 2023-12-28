import os
import random
from library.Tasks.task import Task, TestCase
from library.Model.node import *


class Program:
    id: int
    name: str
    variables: dict[str, VarNode]
    input_data: list[float]
    output_data: list[float]
    const: list[float]
    task: Task
    fitness: float
    mutable_nodes = list[Node]
    max_depth: int
    min_rand: int
    max_rand: int
    ROOT: ScopeNode
    str_program: str

    def __init__(self, id: int, task: Task, max_depth: int, min_rand: int = -5, max_rand: int = 5, input_data: list[float] = []):
        self.id = id
        self.task = task
        self.name = task.name
        self.variables = {}
        self.const = []
        self.input_data = input_data
        self.output_data = []
        self.mutable_nodes = []
        self.fitness = 0.0
        self.max_depth = max_depth
        self.min_rand = min_rand
        self.max_rand = max_rand
        self.ROOT = ScopeNode(NodeType.SCOPE, None, [])
        self.input_index = 0
        self.str_program = ""

    def __repr__(self):
        self.str_program = self.ROOT.__repr__().replace('\n', '').strip()
        return self.ROOT.__repr__()

    def growTree(self):
        posible_nodes = [NodeType.ASSIGNMENT, NodeType.OUTPUT, NodeType.IF, NodeType.WHILE]
        node_t = random.choice(posible_nodes)

        for i in range(random.randint(2,4)):
            self.ROOT.add_child(self.createNode(node_t, self.ROOT))

    def createIndividual(self):
        self.growTree()


    def createNode(self, type: NodeType, parent: Node, current_depth: int = 0):
        if type == NodeType.INPUT:
            input = InputNode(node_type=type, parent_node=parent)
            value = 0.0

            if self.input_data.__len__() != 0:
                if self.input_index != self.input_data.__len__():
                    value = self.input_data[self.input_index]
                else:
                    self.input_index = 0
                    value = self.input_data[self.input_index]

            input.value = value
            self.input_index += 1
            return input
        
        elif type == NodeType.OUTPUT:
            const_count = self.const.__len__()
            var_count = self.variables.__len__()

            output = OutputNode(node_type=type, parent_node=parent, children_nodes=[])
            output.depth = current_depth

            choice = random.choice(["var", "const", "rand"])
            out_rand = choice == "rand"
            out_const = choice == "const"
            out_var = choice == "var"

            if (var_count == 0 and const_count == 0) or out_rand or (const_count == 0 and out_const) or (var_count == 0 and out_var):
                rand_value = float(random.randint(self.min_rand, self.max_rand))
                output.add_child(rand_value)
                self.output_data.append(rand_value)
                self.const.append(rand_value)
            elif out_const:
                rand_const = random.choice(list(self.const))
                output.add_child(rand_const)
                self.output_data.append(rand_const)
            else:
                rand_var = random.choice(list(self.variables.keys()))
                var = self.variables[rand_var]
                output.add_child(var)
                self.output_data.append(var.value)

            output.value = output.calculate()
            return output
        

        elif type == NodeType.VAR:
            var_name = f"x_{self.variables.__len__()}"
            choice = random.choice(['number', 'bool'])
            if choice == 'number':
                rand_value = float(random.randint(self.min_rand, self.max_rand))
                node = VarNode(node_type=type, parent_node=parent, name=var_name, value=rand_value)
            else:
                rand_value = random.choice([True, False])            
                node = VarNode(node_type=type, parent_node=parent, name=var_name, value=rand_value)
            
            return node
            
            
        elif type == NodeType.ASSIGNMENT:
            create_var = self.variables.__len__() == 0
            action = random.choice(["create", "assign"])
            body_type = random.choice(["exp", "input", "condition"])

            match action, create_var:
                case ("create", True|False) | ("assign", True):
                    new_var = self.createNode(NodeType.VAR, None, current_depth+1)
                    match body_type:
                        case "exp":
                            exp = self.createNode(NodeType.EXPRESSION, None, current_depth+1)
                            new_var.value = exp.value
                            assign = AssignmentNode(node_type=type, parent_node=parent, var=new_var, body=exp)
                            new_var.change_parent(assign)
                            exp.parent_node = assign
                            assign.add_child(new_var)
                            assign.add_child(exp)
                        case "input":
                            input = self.createNode(NodeType.INPUT, None, current_depth+1)
                            new_var.value = input.value
                            assign = AssignmentNode(node_type=type, parent_node=parent, var=new_var, body=input)
                            input.change_parent(assign)
                            assign.add_child(new_var)
                            assign.add_child(input)
                        case "condition":
                            condition = self.createNode(NodeType.CONDITION, None, current_depth+1)
                            new_var.value = condition.value
                            assign = AssignmentNode(node_type=type, parent_node=parent, var=new_var, body=condition)
                            condition.change_parent(assign)
                            assign.add_child(new_var)
                            assign.add_child(condition)

                    self.variables.update({new_var.name: new_var})
                
                case "assign", False:
                    new_var = self.variables[random.choice(list(self.variables.keys()))]
                    match body_type:
                        case "exp":
                            exp = self.createNode(NodeType.EXPRESSION, None, current_depth+1)
                            new_var.value = exp.value
                            assign = AssignmentNode(node_type=type, parent_node=parent, var=new_var, body=exp)
                            exp.change_parent(assign)
                            assign.add_child(new_var)
                            assign.add_child(exp)
                        case "input":
                            input = self.createNode(NodeType.INPUT, None, current_depth+1)
                            new_var.value = input.value
                            assign = AssignmentNode(node_type=type, parent_node=parent, var=new_var, body=input)
                            input.change_parent(assign)
                            assign.add_child(new_var)
                            assign.add_child(input)   
                        case "condition":
                            condition = self.createNode(NodeType.CONDITION, None, current_depth+1)
                            new_var.value = condition.value 
                            assign = AssignmentNode(node_type=type, parent_node=parent, var=new_var, body=condition)
                            condition.change_parent(assign)
                            assign.add_child(new_var)
                            assign.add_child(condition)

            return assign

                    
        elif type == NodeType.EXPRESSION:
            left = self.createNode(NodeType.TERM, None, current_depth+1)
            right = random.choice([self.createNode(NodeType.TERM, None, current_depth+1), None])
            
            if right is None:
                operation = None
            else:
                operation = random.choice(['+', '-'])

            out = ExpressionNode(node_type=type, parent_node=parent, left=left, right=right, operation=operation, children_nodes=[])
            out.depth = current_depth
            left.change_parent(out)
            if right != None:
                right.change_parent(out)
            out.add_child(left)
            out.add_child(right)
            
            self.mutable_nodes.append(out)
            return out
        
        elif type == NodeType.TERM:
            left = self.createNode(NodeType.FACTOR, None, current_depth+1)
            right = random.choice([
                self.createNode(NodeType.FACTOR, None, current_depth+1),
                None])
            
            if right is None:
                operation = None
            else:
                operation = random.choice(['*', '/'])
            
            out = TermNode(node_type=type, parent_node=parent, left=left, right=right, operation=operation, children_nodes=[])
            left.change_parent(out)
            if right is not None:
                right.change_parent(out)
            out.add_child(left)
            out.add_child(right)

            self.mutable_nodes.append(out)
            return out
        
        elif type == NodeType.FACTOR:
            count_var = self.variables.__len__()
            count_const = self.const.__len__()

            choice = random.choice(["var", "const", "rand", "exp"])
            out_exp = choice == "exp"
            out_rand = choice == "rand"
            out_const = choice == "const"
            out_var = choice == "var"

            if out_exp and current_depth < self.max_depth-2:
                out = self.createNode(NodeType.EXPRESSION, parent, current_depth+1)
            elif count_var == 0 or out_rand or (count_const == 0 and out_const) or (count_var == 0 and out_var):
                value = random.choice([True, False ,float(random.randint(self.min_rand, self.max_rand))])
                out = FactorNode(node_type=type, parent_node=parent, body=value, children_nodes=[])
                out.add_child(value)
            elif out_const:
                const = random.choice(self.const)
                out = FactorNode(node_type=type, parent_node=parent, body=const, children_nodes=[])
                out.add_child(const)
            else:
                rand_var = random.choice(list(self.variables.keys()))
                var = self.variables[rand_var]
                out = FactorNode(node_type=type, parent_node=parent, body=var, children_nodes=[])
                out.add_child(var)

            self.mutable_nodes.append(out)
            return out

        elif type == NodeType.EXPRESSIONCONDITION:
            leftexpNode = self.createNode(NodeType.EXPRESSION, None, current_depth+1)
            operator = random.choice(['==', '!=','<','>','<=' ,'>='])
            rightexpNode = self.createNode(NodeType.EXPRESSION, None, current_depth+1)

            expressionConditionNode = ExpressionConditionNode(node_type=type, 
                                                              parent_node=parent,
                                                              children_nodes=[leftexpNode, rightexpNode],
                                                              leftExpression=leftexpNode,
                                                              rigthExpression=rightexpNode,
                                                              operator = operator)
            expressionConditionNode.depth = current_depth
            leftexpNode.change_parent(expressionConditionNode)
            rightexpNode.change_parent(expressionConditionNode)
            return expressionConditionNode

        
        elif type == NodeType.CONDITION:
            howMuch = random.choice([1,2])  ### potem dodac 3 i 4
            children =[]
            logicOperators = []
            expressionConditionNode = self.createNode(NodeType.EXPRESSIONCONDITION,  None, current_depth+1)
            children.append(expressionConditionNode)

            for i in range(howMuch-1):
                logicOperator = random.choice(["&&", "||"])
                logicOperators.append(logicOperator)

                expressionConditionNode = self.createNode(NodeType.EXPRESSIONCONDITION,  None, current_depth+1)
                children.append(expressionConditionNode)

            conditionNode = ConditionNode(node_type=type, 
                                          parent_node= parent, 
                                          children_nodes=children,
                                          logicOperators = logicOperators)
            for child in children:
                child.parent_node = conditionNode

            return conditionNode

        
        elif type == NodeType.SCOPE:
            howMuch = random.choice([1,2])
            scope = ScopeNode(node_type=type, parent_node=parent, children_nodes=[])

            for i in range(howMuch):
                choice = random.choice(['assignment', 'if', 'output']) ## na razie tak bo sie robie nieskonczona petla
                if choice == 'if' and scope.depth < self.max_depth-2:
                    ifNode = self.createNode(NodeType.IF, scope, current_depth+1)
                    scope.add_child(ifNode)
                if choice == 'assignment' or scope.depth >= self.max_depth-2:
                    assignmentNode = self.createNode(NodeType.ASSIGNMENT, scope, current_depth+1)
                    scope.add_child(assignmentNode)
                if choice == 'output':
                    outputNode = self.createNode(NodeType.OUTPUT, scope, current_depth+1)
                    scope.add_child(outputNode)

            return scope

        
        elif type == NodeType.IF:
            children = []
            ifNode = IfNode(node_type=type,
                            parent_node= parent, 
                            children_nodes=children)
            
            condition = self.createNode(NodeType.CONDITION, ifNode, current_depth+1)
            ifNode.add_child(condition)
            ifNode.conditionNode = condition

            ifTrueBody = self.createNode(NodeType.SCOPE, ifNode, current_depth+1)
            ifNode.add_child(ifTrueBody)
            ifNode.ifBodyNode = ifTrueBody

            choice = random.choice([True, False])
            if choice == True:
                ifFalseBody = self.createNode(NodeType.SCOPE, ifNode, current_depth+1)
                ifNode.add_child(ifFalseBody)
                ifNode.elseBodyNode = ifFalseBody

            return ifNode
        
        elif type == NodeType.WHILE:
            
            whileNode = WhileNode(node_type=type, parent_node=parent)
            condition = self.createNode(NodeType.CONDITION, whileNode, current_depth+1)
            body = self.createNode(NodeType.SCOPE, whileNode, current_depth+1)

            whileNode.conditionNode = condition
            whileNode.whileBodyNode = body
            whileNode.add_child(condition)
            whileNode.add_child(body)

            return whileNode
        
