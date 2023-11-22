import os
import random
from library.Tasks.task import Task
from library.Model.node import *
from library.Solver.params import Params

class Program():
    name: str
    task: Task
    variables: dict[str, VarNode]
    const: dict[str, float | bool]
    input_data: list[float]
    output_data: list[float]
    fitness: float
    mutable_nodes = list[Node]
    max_depth: int
    min_rand: int
    max_rand: int
    ROOT: ScopeNode

    def __init__(self, task: Task, max_depth: int, min_rand: int = -5, max_rand: int = 5):
        self.task = task
        self.name = task.name
        self.variables = {}
        self.const = {}
        self.input_data = []
        self.output_data = []
        self.mutable_nodes = []
        self.fitness = 0.0
        self.max_depth = max_depth
        self.min_rand = min_rand
        self.max_rand = max_rand
        self.ROOT = ScopeNode(NodeType.SCOPE, None)

    def add_variable(self, name: str, value: float):
        new_variables = self.variables.update({name: value})
        return new_variables

    def __repr__(self):
        for child in self.ROOT.children_nodes:
            print(child)
        return ""

    # do recurent createIndividual that will create tree until max_depth
    def createIndividual(self):
        # create input nodes
        self.ROOT.add_child(self.createNode(NodeType.INPUT, self.ROOT))

        self.ROOT.add_child(self.createNode(NodeType.ASSIGNMENT, self.ROOT))

        self.ROOT.add_child(self.createNode(NodeType.OUTPUT, self.ROOT))


    # def get_subtree(self, node: Node):

    def createNode(self, type: NodeType, parent: Node, current_depth: int = 0):

        # if current_depth >= self.max_depth:
        #     return
        
        if type == NodeType.INPUT:
            posible_nodes = [NodeType.VAR, NodeType.CONST]
            node = random.choice(posible_nodes)

            vars: list[TerminalNode] = []
            input = InputNode(node_type=type, parent_node=parent, value=vars)

            input_len = random.randint(self.task.min_input_length, self.task.max_input_length)
            for i in range(input_len):
                var = self.createNode(node, input, current_depth)
                vars.append(var)

            input.value = vars
            self.input_data = list(v.value for v in vars)

            return input
        
        elif type == NodeType.OUTPUT:
            values: list[TerminalNode] = []

            output = OutputNode(node_type=type, parent_node=parent, value=values)
            output_len = random.randint(self.task.min_output_length, self.task.max_output_length)

            for i in range(output_len):
                out_rand = random.choice([True, False])
                out_const = random.choice([True, False])
            
                if self.variables.__len__() == 0 or ( self.const.__len__() == 0 and out_const ) or out_rand:
                    rand_value = random.randint(self.min_rand, self.max_rand)
                    values.append(TerminalNode(float(rand_value), output))
                elif out_const:
                    rand_const = random.choice(list(self.const.keys()))
                    values.append(TerminalNode(self.const[rand_const], output))
                else:
                    rand_var = random.choice(list(self.variables.keys()))
                    values.append(TerminalNode(self.variables[rand_var], output))

            self.output_data = values
            output.value = values
            return output
        
        elif type == NodeType.VAR:
            var_name = f"x_{self.variables.__len__()}"
            value = random.randint(self.min_rand, self.max_rand)
            node = VarNode(node_type=type, parent_node=parent, name=var_name, value=None)
            t_value = TerminalNode(float(value), node)
            node.value = t_value
            
            self.variables.update({var_name: node})
            self.mutable_nodes.append(node)
            return node
            
        elif type == NodeType.CONST:
            var_name = f"c_{self.const.__len__()}"
            value = random.randint(self.min_rand, self.max_rand)
            
            node = ConstNode(node_type=type, parent_node=parent, name=var_name, value=None)
            t_value = TerminalNode(float(value), node)
            node.value = t_value
            
            self.const.update({var_name: node})
            self.mutable_nodes.append(node)
            return node
            
        elif type == NodeType.ASSIGNMENT:
            create_var = random.choice([True, False])

            if self.variables.__len__() == 0 or create_var:
                new_var = self.createNode(NodeType.VAR, None, current_depth+1)
                exp = self.createNode(NodeType.EXPRESSION, None, current_depth+1)

                assign = AssignmentNode(node_type=type, parent_node=parent, var_name=new_var.name, body=exp)
                
                self.variables[new_var.name] = exp.value
            else:
                index = random.randint(0, self.variables.__len__()-1)
                new_var = list(self.variables.keys())[index]
                exp = self.createNode(NodeType.EXPRESSION, None, current_depth+1)
                assign = AssignmentNode(node_type=type, parent_node=parent, var_name=new_var, body=exp)
                self.variables[new_var] = exp.value

            self.mutable_nodes.append(assign)
            return assign
                    
        elif type == NodeType.EXPRESSION:
            left = self.createNode(NodeType.TERM, parent, current_depth+1)
            right = random.choice([
                self.createNode(NodeType.TERM, parent, current_depth+1),
                None])
            
            if right is None:
                operation = None
            else:
                operation = random.choice(['+', '-'])

            out = ExpressionNode(node_type=type, parent_node=parent, left=left, right=right, operation=operation)
            self.mutable_nodes.append(out)
            return out
        
        elif type == NodeType.TERM:
            left = self.createNode(NodeType.FACTOR, parent, current_depth+1)
            right = random.choice([
                self.createNode(NodeType.FACTOR, parent, current_depth+1),
                None])
            
            if right is None:
                operation = None
            else:
                operation = random.choice(['*', '/'])
            
            out = TermNode(node_type=type, parent_node=parent, left=left, right=right, operation=operation)
            self.mutable_nodes.append(out)
            return out
        
        elif type == NodeType.FACTOR:
            if random.choice([True, False]) and current_depth < self.max_depth-2:
                return self.createNode(NodeType.EXPRESSION, parent, current_depth+1)
            else:
                # use variables or constants
                # need to print vars names which can be a problem 

                out = TerminalNode(float(random.choice([i for i in range(self.min_rand, self.max_rand) if i != 0])), parent)
                self.mutable_nodes.append(out)
                return out
            
        else:
            print("ERROR: invalid node type")
            return None

    def use_variables(self, var_name: str, parent: Node):
        value = self.variables[var_name]
        var = VarNode(NodeType.VAR, parent, var_name, TerminalNode(value))
        return var

        
        

        
