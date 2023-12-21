import numpy

from library.Model.program import Program
from library.Solver.params import Params
from library.Tasks.task import Task, TestCase
import random
from library.Model.node import *
from Grammar.gen.TinyGPVisitor import TinyGPVisitor
from Grammar.gen.TinyGPParser import TinyGPParser
from Grammar.gen.TinyGPLexer import TinyGPLexer
from antlr4 import *
import numpy as np


class GP():
    name: str
    popuation: list[Program]
    best: Program
    best_fitness: float
    fitnesses :list[float]
    best_generation: int
    params: Params
    task: Task
    test_cases: list[TestCase] # list of TestCase objects from library/Tasks/task.py
    generation: int
    tournament_size: int = 2

    def __init__(self, task_name: str, set_seed: int | None = None, params: Params | None = None):
        self.popuation = []
        self.best = None
        self.best_fitness = 0.0
        self.fitnesses = []
        self.best_generation = 0
        self.generation = 0
        self.task = Task(task_name)
        self.params = params or Params(seed=set_seed, max_depth=1)
        self.popuation = self.create_population(self.task, self.params)
        self.test_cases = []
        self.tournament_size = 2



    def get_task_cases(self):
        self.test_cases = self.task.test_cases

    def create_population(self, task: Task, params: Params):
        # print(params)
        
        self.name = task.name
        pop = []

        for i in range(params.popsize):
            index = random.randint(0, len(task.test_cases) - 1)
            test_case = task.test_cases[index]

            p = Program(i, task, params.max_depth, params.min_rand, params.max_rand, input_data=test_case.input_data)
            p.createIndividual()
            # print(f"\nSERIALIZE: {i}")
            # p.serialize(p.ROOT)
            # print("KONIEC\n")
            # print("\nSERIALIZE")
            # self.serialize(p.ROOT, p)
            # print("KONIEC\n")
            pop.append(p)

        return pop
    
    def print_individual(self, index: int):
        print("---------------------")
        print(f"Individual: {self.popuation[index].id}\n")
        print("Program: ")
        print(self.popuation[index])

        print("Variables:")
        var_dict={}
        vars = "{ "
        for var in self.popuation[index].variables:
            vars += f"{var}: {float(self.popuation[index].variables[var].value)}, "
            var_dict[var] = float(self.popuation[index].variables[var].value)
        vars = vars[:-2]
        vars += " }"
        print(f'{vars}\n')

        output = self.interpret(self.popuation[index].__repr__(), var_dict, self.popuation[index].input_data)
        self.popuation[index].output_data = output

        # print("Const:")
        # if len(self.popuation[index].const) == 0:
        #     print("{" + " " + "}")
        # else:
        #     vars = "{ "
        #     for var in self.popuation[index].const:
        #         vars += f"{var}: {self.popuation[index].const[var].value}, "
        #     vars = vars[:-2]
        #     vars += " }"
        #     print(f'{vars}\n')

        # print("\nRoot children:")
        # for child in self.popuation[index].ROOT.children_nodes:
        #     print(child)

        # print("\nMutable nodes:")
        # for node in self.popuation[index].mutable_nodes:
        #     print(node)

        print("\nInput data:")
        print(self.popuation[index].input_data)

        print("\nOutput data:")
        print(self.popuation[index].output_data)
        print("---------------------\n")


    def print_population(self):
        print(f"Task: {self.name}")
        print(self.params)
        print(f"Generation: {self.generation}\n")   
        for i in range(len(self.popuation)):
            self.print_individual(i)
        self.fitness_function()
        self.tournament()

    def deep_copy_tree(self, tree: Node):
        new_tree =ScopeNode(NodeType.SCOPE, None ,[])
        for child in tree.children_nodes:
            new_tree.children_nodes.append(child)
        # print("NEW_TREE:   ", new_tree)
        return new_tree

    # TO DO
    def evalate(self):
        # check if best_individual solve the case
        # if not -> random: mutation / crossover
        # calculate new fitnesses
        pass

    # TO DO
    def mutation(self, individual: Program):
        pass

    # TO DO
    def crossover(self, individual_1: Program, individual_2: Program):
        pass

    def print_children(self, child: Node):
        pass

    def single_fintess(self, individual: Program):
        index = random.randint(0, len(self.task.test_cases) - 1)
        task_cases = self.task.test_cases[index]
        if len(task_cases.output_data) == 0 or len(individual.output_data) == 0 or len(task_cases.output_data) != len(individual.output_data):
            return 0.0
        # print("task_cases: ", task_cases.output_data[0])
        # print("individual: ", individual.output_data[0])
        received = numpy.array(individual.output_data)
        expected = numpy.array(task_cases.output_data)
        self.fitnesses.append((-1) * np.abs(expected - received))
        return (-1) * np.abs(expected - received)

    def fitness_function(self):
        fit = 0.0
        for individual in self.popuation:
            fit += self.single_fintess(individual)
        print(f"FITNESS: {fit}")
        return fit

    def tournament(self):
        best = random.randint(0, len(self.popuation) - 1)
        best_fitness = -1.0e34
        print("len: ", len(self.popuation))
        print("lenf: ", len(self.fitnesses))
        for i in range(self.tournament_size):
            competitor = random.randint(0, len(self.popuation) - 1)
            if self.fitnesses[competitor] > best_fitness:
                best_fitness = self.fitnesses[competitor]
                best = competitor

        print("Tournament: ", best, " ", best_fitness, "\n")

        return best

    def negative_tournament(self):
        worst = random.randint(0, len(self.popuation) - 1)
        worst_fitness = 1.0e34

        for i in range(self.tournament_size):
            competitor = random.randint(0, len(self.popuation) - 1)
            if self.fitnesses[competitor] < worst_fitness:
                worst_fitness = self.fitnesses[competitor]
                worst = competitor

        return worst


    # def branch(self, node: Node):
    #     branch=""
    #     for i in range(node.depth):
    #         branch += "-"
    #     return branch

    # def serialize(self, node: Node, program: Program):
    #     # print(node.children_nodes)
    #     for child in node.children_nodes:
    #         if type(child) != float and child.node_type != None:
    #             branch=""
    #             for i in range(node.depth):
    #                 branch += "-"
    #             print(branch, child, child.node_type)
    #             self.serialize(child, program)
    #         else:
    #             branch=""
    #             for i in range(program.max_depth):
    #                 branch += "-"

    #             print(branch, child)
    #         # if child.children_nodes != None:
    #         #     self.serialize(child)

    def deserialize(self, node: Node):
        pass
    ### nie moze byc x_1 = (expression) !! --- zmien w gramatyce
    def interpret(self, input_data, variables, input_1):
        input_example ="{x_1 = 1.0 while (x_1 <2.0){ output(x_1) x_1 = x_1 + 1.0 } }"
        var = {"x_0": None, "x_1": None}

        input = InputStream(input_example)
        print("TRER ", type(input_data))
        # print(input_data)
        lexer = TinyGPLexer(input)

        stream = CommonTokenStream(lexer)
        parser = TinyGPParser(stream)
        try:
            tree = parser.program()
        except:
            print("Error")
            return None
        visitor = TinyGPVisitor(var, input_1)

        visitor.visit(tree)
        print("output: ", visitor.output)
        return visitor.output

        # return visitor.visit(tree)

        