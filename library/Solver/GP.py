from contextlib import redirect_stdout

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
import os


class GP:
    name: str
    population: list[Program]
    best: Program
    best_fitness: float
    best_generation: int
    params: Params
    task: Task
    test_cases: list[TestCase] # list of TestCase objects from library/Tasks/task.py
    generation: int
    tournament_size: int
    fitnesses: np.array

    def __init__(self, task_name: str, set_seed: int | None = None, params: Params | None = None):
        self.population = []
        self.params = params or Params(seed=set_seed, max_depth=1)
        self.best = None
        self.best_fitness = 0.0
        self.fitnesses = self.initialize_fitness()
        self.best_generation = 0
        self.generation = 0
        self.task = Task(task_name)
        self.population = self.create_population(self.task, self.params)
        self.test_cases = []
        self.tournament_size = 2


    def get_task_cases(self):
        self.test_cases = self.task.test_cases

    def create_population(self, task: Task, params: Params):
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
        individual = ""
        print("---------------------")
        print(f"Individual: {self.population[index].id}\n")
        print("Program: ")
        print(self.population[index])
        individual = self.population[index].__repr__()

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

        return individual

    def print_population(self):
        print(f"Task: {self.name}")
        print(self.params)
        print(f"Generation: {self.generation}\n")   
        for i in range(len(self.population)):
            self.print_individual(i)

    def deep_copy_tree(self, tree: Node):
        new_tree = ScopeNode(NodeType.SCOPE, None,[])
        for child in tree.children_nodes:
            new_tree.children_nodes.append(child)
        # print("NEW_TREE:   ", new_tree)
        return new_tree
    
    # TO DO
    def evaluate(self, fitness_function):
        self.print_population()
        while self.generation < self.params.generations:
            for individual in self.population:
                var_dict = {}
                for var in individual.variables:
                    var_dict[var] = float(individual.variables[var].value)
                individual.output_data = self.interpret(individual.str_program, var_dict, individual.input_data)

            self.fitness(fitness_function)
            best_index, best_fitness = self.best_individual_fitness()
            self.print_individual(best_index)
            if best_fitness == 0.0:
                print("Problem solved!\n")
                self.print_individual(best_index)
                # zrobić zapisywanie do pliku wyniku
                # path = f"../Tasks/outputs/{self.name}/"
                # with open(os.path.join(path, f"{self.name}.txt"), 'a+') as f:
                #         st = self.print_individual(best_index)
                #         f.write(st)
                exit(1)
            # else:

            self.generation += 1

        print(f"Problem not solved :c\n")
        print(f"Best fitness: {best_fitness}\n")

        pass

    def run(self, fitness_function):
        self.evaluate(fitness_function)

    # TO DO
    def mutation(self, individual: Program):
        pass

    # TO DO
    def crossover(self, individual_1: Program, individual_2: Program):
        pass

    def print_children(self, child: Node):
        pass

    def fitness(self, fitness_function):
        for i, individual in enumerate(self.population):
            self.fitnesses[i] = fitness_function(individual)

    def best_individual_fitness(self):
        max_arg = np.argmax(self.fitnesses)
        value = self.fitnesses[max_arg]
        return int(max_arg), value

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

    def initialize_fitness(self):
        array = np.empty(self.params.popsize, dtype=np.float32)
        array.fill(-100.0)
        return array

    def save_result_to_file(self, result):
        path = os.path.join("../Tasks/outputs/", self.name)
        if not os.path.exists(path):
            os.makedirs(path)

        with open(os.path.join(path, self.name), 'w+') as f:
            f.write(result)
