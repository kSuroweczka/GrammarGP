import os
import random
from library.Tasks.task import Task, TestCase
from library.Model.node import *
from library.Solver.params import Params

class Program():
    id: int
    name: str
    task: Task
    variables: dict[str, VarNode]
    const: dict[str, ConstNode]
    input_data: list[float]
    output_data: list[float]
    fitness: float
    mutable_nodes = list[Node]
    max_depth: int
    min_rand: int
    max_rand: int
    ROOT: ScopeNode

    def __init__(self, id: int, task: Task, max_depth: int, min_rand: int = -5, max_rand: int = 5, input_data: list[float] = []):
        self.id = id
        self.task = task
        self.name = task.name
        self.variables = {}
        self.const = {}
        self.input_data = input_data
        self.output_data = []
        self.mutable_nodes = []
        self.fitness = 0.0
        self.max_depth = max_depth
        self.min_rand = min_rand
        self.max_rand = max_rand
        self.ROOT = ScopeNode(NodeType.SCOPE, None, [])


    def __repr__(self):
        for child in self.ROOT.children_nodes:
            print(child)
        return ""

    def createIndividual(self):        
        self.ROOT.add_child(self.createNode(NodeType.INPUT, self.ROOT))

        # posible_nodes = [NodeType.ASSIGNMENT, NodeType.VAR, NodeType.CONST]
        # node_t = random.choice(posible_nodes)

        # for i in range(random.randint(2, 5)):
        #     self.ROOT.add_child(self.createNode(node_t, self.ROOT))

        self.ROOT.add_child(self.createNode(NodeType.OUTPUT, self.ROOT))
        


    def createNode(self, type: NodeType, parent: Node, current_depth: int = 0):


        if type == NodeType.INPUT:
            input_len = len(self.input_data)
            input = InputNode(node_type=type, parent_node=parent, children_nodes=[])

            for i in range(input_len):
                new_assignment = self.createNode(NodeType.ASSIGNMENT, input, current_depth)
                input.add_child(new_assignment)

            input.value = input.calculate()
            return input
        
        
        elif type == NodeType.OUTPUT:
            const_count = self.const.__len__()
            var_count = self.variables.__len__()

            output = OutputNode(node_type=type, parent_node=parent, children_nodes=[])
            output_len = random.randint(self.task.min_output_length, self.task.max_output_length)

            for i in range(output_len):
                choice = random.choice(["var", "const", "rand"])
                out_rand = choice == "rand"
                out_const = choice == "const"
                out_var = choice == "var"

                if (var_count == 0 and const_count == 0) or out_rand or (const_count == 0 and out_const) or (var_count == 0 and out_var):
                    rand_value = float(random.randint(self.min_rand, self.max_rand))
                    output.add_child(rand_value)
                    self.output_data.append(rand_value)
                elif out_const:
                    rand_const = random.choice(list(self.const.keys()))
                    const = self.const[rand_const]
                    output.add_child(const)
                    self.output_data.append(const.value)
                else:
                    rand_var = random.choice(list(self.variables.keys()))
                    var = self.variables[rand_var]
                    output.add_child(var)
                    self.output_data.append(var.value)

            output.value = output.calculate()
            return output
        

        elif type == NodeType.VAR:
            var_name = f"x_{self.variables.__len__()}"
            rand_value = float(random.randint(self.min_rand, self.max_rand))
            node = VarNode(node_type=type, parent_node=None, name=var_name, value=rand_value)
            
            self.variables.update({var_name: node})
            return node
            
        elif type == NodeType.CONST:
            const_name = f"c_{self.const.__len__()}"
            rand_value = float(random.randint(self.min_rand, self.max_rand))
            node = ConstNode(node_type=type, parent_node=None, name=const_name, value=rand_value)
            
            self.const.update({const_name: node})
            return node
            
        elif type == NodeType.ASSIGNMENT:
            create_var = random.choice([True, False])
            var_count = self.variables.__len__()
            
            if parent.node_type == NodeType.INPUT:
                index = self.variables.__len__()
                var_value = float(self.input_data[index])
                
                new_var = self.createNode(NodeType.VAR, None, current_depth+1)
                new_var.value = var_value

                assign = AssignmentNode(node_type=type, parent_node=parent, var=new_var, body=var_value, children_nodes=[])
                assign.add_child(new_var)
                assign.add_child(var_value)
                self.variables.update({new_var.name: new_var})

            # else:
            #     if var_count == 0 or create_var:
            #         new_var = self.createNode(NodeType.VAR, None, current_depth+1)
            #         exp = self.createNode(NodeType.EXPRESSION, None, current_depth+1)

            #         assign = AssignmentNode(node_type=type, parent_node=parent, var=new_var, body=exp)
            #         assign.add_child(new_var)
            #         assign.add_child(exp)

            #         self.variables[new_var.name] = exp.value
            #     else:
            #         index = random.randint(0, self.variables.__len__()-1)
            #         new_var = list(self.variables.keys())[index]
            #         exp = self.createNode(NodeType.EXPRESSION, None, current_depth+1)
            #         assign = AssignmentNode(node_type=type, parent_node=parent, var=new_var, body=exp)
            #         assign.add_child(new_var)
            #         assign.add_child(exp)

            #         self.variables[new_var] = exp.value
                
            #     self.mutable_nodes.append(assign)

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
            none_vars = self.variables.__len__() == 0
            none_const = self.const.__len__() == 0

            if random.choice([True, False]) and current_depth < self.max_depth-2:
                out = self.createNode(NodeType.EXPRESSION, parent, current_depth+1)
            else:
                out = TerminalNode(float(random.choice([i for i in range(self.min_rand, self.max_rand) if i != 0])), parent) 

            # else:
            #     posible_nodes = [NodeType.VAR, NodeType.CONST, NodeType.TERMINAL]
            #     node_t = random.choice(posible_nodes) 
            #     match node_t:
            #         case NodeType.VAR:
            #             if not none_vars:
            #                 var = random.choice(list(self.variables.items()))
            #                 node = VarNode(node_t, parent, var[0], var[1])
            #                 out = node
            #             else:
            #                 out = TerminalNode(float(random.choice([i for i in range(self.min_rand, self.max_rand) if i != 0])), parent)
            #         case NodeType.CONST:
            #             if not none_const:
            #                 var = random.choice(list(self.const.items()))
            #                 node = VarNode(node_t, parent, var[0], var[1])
            #                 out = node
            #             else:
            #                 out = TerminalNode(float(random.choice([i for i in range(self.min_rand, self.max_rand) if i != 0])), parent)
            #         case NodeType.TERMINAL:
            #             out = TerminalNode(float(random.choice([i for i in range(self.min_rand, self.max_rand) if i != 0])), parent) 

                self.mutable_nodes.append(out)
                return out
            
        else:
            print("ERROR: invalid node type")
            return None


        
        

        
