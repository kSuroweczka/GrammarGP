import os
import random
from library.Tasks.task import Task
from library.Model.node import *
from library.Solver.params import Params

class Program():
    name: str
    task: Task
    variables: dict[str, float | bool]
    const: dict[str, float | bool]
    # input_data: list[float]
    # output_data: list[float]
    max_depth: int
    min_rand: int
    max_rand: int
    ROOT: ScopeNode

    def __init__(self, task: Task, max_depth: int, min_rand: int = -5, max_rand: int = 5):
        self.task = task
        self.name = task.name
        self.variables = {}
        self.const = {}
        # self.input_data = task.test_cases[0].input_data
        # self.output_data = task.test_cases[0].output_data
        # self.fitness = 0.0
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

        self.ROOT.add_child(self.createNode(NodeType.VAR, self.ROOT))
        # self.ROOT.add_child(self.createNode(NodeType.CONDITION, self.ROOT))

        self.ROOT.add_child(self.createNode(NodeType.OUTPUT, self.ROOT))



    def createNode(self, type: NodeType, parent: Node):
        if type == NodeType.INPUT:
            vars: list[TerminalNode] = []
            input = InputNode(node_type=type, parent_node=parent, value=vars)

            input_len = random.randint(self.task.min_input_length, self.task.max_input_length)
            for i in range(input_len):
                var = self.createNode(NodeType.VAR, input)
                vars.append(var)
            input.value = vars
            return input
        
        elif type == NodeType.OUTPUT:
            values = []
            output = OutputNode(node_type=type, parent_node=parent, value=values)

            output_len = random.randint(self.task.min_output_length, self.task.max_output_length)
            for i in range(output_len):
                if self.variables.__len__() == 0:
                    rand_value = random.randint(self.min_rand, self.max_rand)
                    values.append(float(rand_value))
                else:
                    rand_var = random.choice(list(self.variables.keys()))
                    values.append(self.variables[rand_var])

            output.value = values
            return output
        
        elif type == NodeType.VAR:
            var_name = f"x_{self.variables.__len__()}"

            is_bool = random.choice([False, True])

            if is_bool:
                value = random.choice([True, False])
                node = BooleanNode(value)
                self.variables.update({var_name: value})
                return VarNode(node_type=type, parent_node=parent, name=var_name, value=node)
            else:
                value = random.randint(self.min_rand, self.max_rand)
                node = NumeralNode(float(value))
                self.variables.update({var_name: float(value)})
                return VarNode(node_type=type, parent_node=parent, name=var_name, value=node)
            
        elif type == NodeType.CONST:
            var_name = f"c_{self.const.__len__()}"
            is_bool = random.choice([False, True])

            if is_bool:
                value = random.choice([True, False])
                self.variables.update({var_name: BooleanNode(value)})
                return ConstNode(node_type=type, parent_node=parent, name=var_name, value=value)
            else:
                value = random.randint(self.min_rand, self.max_rand)
                self.variables.update({var_name: NumeralNode(float(value))})
                return ConstNode(node_type=type, parent_node=parent, name=var_name, value=value)
        
        elif type == NodeType.EXPRESSION:
            left = self.createNode(NodeType.FACTOR, parent)
            right = self.createNode(NodeType.FACTOR, parent)
            operation = random.choice(['+', '-'])
            return ExpressionNode(node_type=type, parent_node=parent, left=left, right=right, operation=operation)
        
        elif type == NodeType.FACTOR:
            left = NumeralNode(float(random.choice([i for i in range(self.min_rand, self.max_rand)])))
            right = NumeralNode(float(random.choice([i for i in range(self.min_rand, self.max_rand) if i not in [0]])))
            operation = random.choice(['*', '/'])
            return FactorNode(node_type=type, parent_node=parent, left=left, right=right, operation=operation)

        # TO DO 
        # elif type == NodeType.CONDITION:
        #     condition = ConditionNode(node_type=type, parent_node=parent)
        #     left = 
        #     condition.add_child(self.createNode(NodeType.CONST, condition))
        #     return condition
        else:
            print("ERROR: invalid node type")
            return None



        

        
