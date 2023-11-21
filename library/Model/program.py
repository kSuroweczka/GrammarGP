import os
import random
from library.Tasks.task import Task
from library.Model.node import *

class Program():
    name: str
    task: Task
    variables: dict[str, float]
    const: dict[str, float]
    input_data: list[float]
    output_data: list[float]
    max_depth: int
    ROOT: ScopeNode

    def __init__(self, task: Task, max_depth: int):
        self.task = task
        self.name = task.name
        self.variables = {}
        self.const = {}
        self.input_data = task.test_cases[0].input_data
        self.output_data = task.test_cases[0].output_data
        self.fitness = 0.0
        self.max_depth = max_depth
        self.ROOT = ScopeNode(NodeType.SCOPE, None)
        

    def __repr__(self):
        for child in self.ROOT.children_nodes:
            print(child)
        return ""


    # do recurent createIndividual that will create tree until max_depth
    def createIndividual(self):

        self.ROOT.add_child(self.createNode(NodeType.VAR, self.ROOT, 1))
        self.ROOT.add_child(self.createNode(NodeType.VAR, self.ROOT, 1))
        self.ROOT.add_child(self.createNode(NodeType.CONST, self.ROOT, 1)) # output


    def createNode(self, type: NodeType, parent: Node, index: int):
        if type == NodeType.INPUT:
            return InputNode(node_type=type, parent_node=parent, value=self.input_data)
        elif type == NodeType.OUTPUT:
            return OutputNode(node_type=type, parent_node=parent, value=self.output_data)
        elif type == NodeType.VAR:
            var_name = f"x_{self.variables.__len__()}"
            value = random.uniform(-1, 1)
            self.variables[var_name] = value
            return VarNode(node_type=type, parent_node=parent, name=var_name, value=value)
        elif type == NodeType.CONST:
            var_name = f"c_{self.const.__len__()}"
            value = random.uniform(-1, 1)
            self.const[var_name] = value
            return ConstNode(node_type=type, parent_node=parent, name=var_name, value=value)
        else:
            print("ERROR: invalid node type")
            return None



        

        
