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


class GP:
    name: str
    population: list[Program]
    best: Program
    best_fitness: float
    fitnesses: list[float]
    best_generation: int
    params: Params
    task: Task
    test_cases: list[TestCase] # list of TestCase objects from library/Tasks/task.py
    generation: int
    tournament_size: int

    def __init__(self, task_name: str, set_seed: int | None = None, params: Params | None = None):
        self.population = []
        self.best = None
        self.best_fitness = 0.0
        self.fitnesses = []
        self.best_generation = 0
        self.generation = 0
        self.task = Task(task_name)
        self.params = params or Params(seed=set_seed, max_depth=1)
        self.population = self.create_population(self.task, self.params)
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

            pop.append(p)

        return pop
    
    def print_individual(self, index: int):
        print("---------------------")
        print(f"Individual: {self.population[index].id}\n")
        print("Program: ")
        print(self.population[index])

        print("Variables:")
        var_dict = {}
        vars = "{ "
        for var in self.population[index].variables:
            vars += f"{var}: {float(self.population[index].variables[var].value)}, "
            var_dict[var] = float(self.population[index].variables[var].value)
        vars = vars[:-2]
        vars += " }"
        print(f'{vars}\n')

        self.population[index].output_data = self.interpret(self.population[index].str_program, var_dict, self.population[index].input_data)
        print("\nInput data:")
        print(self.population[index].input_data)

        print("\nOutput data:")
        print(self.population[index].output_data)
        print("---------------------\n")

    def print_population(self):
        print(f"Task: {self.name}")
        print(self.params)
        print(f"Generation: {self.generation}\n")   
        for i in range(len(self.population)):
            self.print_individual(i)
        self.fitness_function()
        # self.tournament()

    def deep_copy_tree(self, tree: Node):
        new_tree = ScopeNode(NodeType.SCOPE, None,[])
        for child in tree.children_nodes:
            new_tree.children_nodes.append(child)
        # print("NEW_TREE:   ", new_tree)
        return new_tree
    
    # TO DO
    def evalate(self):
        if self.generation < self.params.generations:
            print()

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

    def single_fitness(self, individual: Program):
        index = random.randint(0, len(self.task.test_cases) - 1)
        task_cases = self.task.test_cases[index]
        print("task_casecdds: ", len(task_cases.input_data))
        print("individuasdsdl: ", len(individual.input_data))
        if len(task_cases.output_data) == 0 or len(individual.output_data) == 0 or len(task_cases.output_data) != len(individual.output_data):
            return 0.0
        print("task_cases: ", task_cases.output_data[0])
        print("individual: ", individual.output_data[0])
        received = np.array(individual.output_data)
        expected = np.array(task_cases.output_data)
        self.fitnesses.append((-1) * np.abs(expected - received))
        return (-1) * np.abs(expected - received)

    def single_fitness_1_1(self, where: int, only: bool, individual: Program):
        fitness = -100.0
        print("\n")
        print("SINGLE FITNESS 1_1")
        print("individual: ", individual.output_data)
        expected = self.task.test_cases[0].output_data[0]

        if type(individual.output_data) == list:
            if len(individual.output_data) == 0:
                # print("pusta lista, ", individual.output_data)
                fitness = -10.0
            elif individual.output_data == expected or expected in individual.output_data:
                if where == None:
                    if only:
                        if len(individual.output_data) == 1:
                            fitness = (-1)*np.abs(expected - individual.output_data[0])
                            # print("fitness gdy only i len == 1: ", fitness)
                        else:
                            avg = np.average(individual.output_data)
                            fitness = (-1)*np.abs(avg)
                            # print("fitness only i len!=1: ", fitness)
                    else:
                        fitness = 0.0
                else:
                    if individual.output_data[where] == expected:
                        fitness = 0.0
                    else:
                        fitness = (-1)*np.abs(expected - individual.output_data[where])
            elif expected not in individual.output_data and where == None:
                sub = np.abs(np.subtract(expected, individual.output_data))
                fitness = (-1)*np.min(sub)
                # print("nie ma w liscie, ", fitness)
        print("single fitness: ", fitness)
        return fitness


    def single_fitness_1_2(self, individual: Program):
        #### operation, min i max przedziału w pliku task
        print("\n")
        print("SINGLE FITNESS 1_2")
        print("individual: ", individual.output_data)

        output = individual.output_data
        expected = self.task.test_cases[0].output_data
        fitness = -100.0

        if len(output) == 0:
            fitness = -10.0
        elif len(output) == 1:
            if output[0] == expected[0]:
                fitness = 0.0
            else:
                fitness = (-1)*np.abs(expected[0] - output[0])
        elif len(output) > 1:
            avg = np.average(output)
            fitness = (-1)*np.abs(avg - expected[0])
        print("single fitness: ", fitness)
        return fitness

    def single_fitness_1_3(self, list_on_input: list, operator: str, min: float, max: float):
        ### to co w single_fitness_1_2 raczej wystarczy
        pass
    def single_fitness_1_4(self, individual: Program):
        ### w sumie to to samo co w single_fitness_1_2
        print("\n")
        print("SINGLE FITNESS 1_4")
        print("individual: ", individual.output_data)
        output = individual.output_data
        expected = self.task.test_cases[0].output_data
        fitness = -100.0
        if len(output) == 0:
            fitness = -10.0
        elif len(output) == 1:
            if output == expected:
                fitness = 0.0
            else:
                fitness = (-1)*np.abs(output[0] - expected[0])
        elif len(output) > 1:
            avg = int(np.average(output))
            fitness = (-1)*np.abs(avg - expected[0])
        print("single fitness: ", fitness)
        return fitness


    def fitness_function(self):
        fit = 0.0
        for individual in self.population:
            fit += self.single_fitness_1_4(individual)
        print(f"FITNESS: {fit}")
        return fit

    def tournament(self):
        best = random.randint(0, len(self.population) - 1)
        best_fitness = -1.0e34
        print("len: ", len(self.population))
        print("lenf: ", len(self.fitnesses))
        for i in range(self.tournament_size):
            competitor = random.randint(0, len(self.population) - 1)
            if self.fitnesses[competitor] > best_fitness:
                best_fitness = self.fitnesses[competitor]
                best = competitor

        print("Tournament: ", best, " ", best_fitness, "\n")

        return best

    def negative_tournament(self):
        worst = random.randint(0, len(self.population) - 1)
        worst_fitness = 1.0e34

        for i in range(self.tournament_size):
            competitor = random.randint(0, len(self.population) - 1)
            if self.fitnesses[competitor] < worst_fitness:
                worst_fitness = self.fitnesses[competitor]
                worst = competitor

        return worst


    def interpret(self, input_data, variables, input_1):
        var = variables
        input_example = input_data
        # input_example = "x_0 = input() output(-6.0) while(x_0 < 200.0) { x_0 = x_0 + 1.0 output(x_0)}}"

        input = InputStream(input_example)
        # print("TRER ", input_example)
        lexer = TinyGPLexer(input)

        stream = CommonTokenStream(lexer)
        parser = TinyGPParser(stream)
        try:
            tree = parser.program()
        except:
            print("Error")
            return None

        try:
            visitor = TinyGPVisitor(var, input_1)
            visitor.visit(tree)
            return visitor.output
        except:
            return [-100.0]

        