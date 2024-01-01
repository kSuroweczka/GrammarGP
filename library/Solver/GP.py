from contextlib import redirect_stdout

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

    def create_population(self, task: Task, params: Params):
        self.name = task.name
        pop = []

        for i in range(params.popsize):
            index = random.randint(0, len(task.test_cases) - 1)
            test_case = task.test_cases[index]

            p = Program(i, task, params.max_depth, params.min_rand, params.max_rand, test_case.input_data)
            p.createIndividual()

            pop.append(p)

        return pop

    # TO DO
    def evaluate(self, fitness_function):
        ok = False

        print(f"Task: {self.name}")
        print(self.params)

        while self.generation < self.params.generations:
            for individual in self.population:
                var_dict = {}
                for var in individual.variables:
                    var_dict[var] = float(individual.variables[var].value)
                individual.output_data = self.interpret(individual.str_program, var_dict, individual.input_data)

            self.fitness(fitness_function)
            best_index, best_fitness = self.best_individual_fitness()
            if best_fitness == 0.0:
                print("Problem solved!\n")
                ok = True
                break
            else:
                print("------------------------------")
                print(f"Generation {self.generation}")
                print(f"Best fitness: {best_fitness}")
                self.print_individual(best_index)

                # To do:
                rand_op = random.randrange(0, 1)
                if rand_op < self.params.crossover_prob:
                    self.crossover()
                else:
                    self.mutation()

                worst_index, worst_fitness = self.worst_individual_fitness()
                worst = self.population[worst_index]
                p = Program(worst.id, worst.task, self.params.max_depth, self.params.min_rand, self.params.max_rand, worst.input_data)
                p.createIndividual()

                # print("Worst: \n")
                # self.print_individual(worst_index)
                # self.population[worst_index] = p
                #
                # print("New Individual: \n")
                # self.print_individual(worst_index)


                print("\n\n")
            self.generation += 1

        if not ok:
            print(f"Problem not solved :c\n")
            print(f"Best fitness: {best_fitness}\n")

        self.save_result_to_file(best_index, ok, best_fitness)

    def run(self, fitness_function):
        self.evaluate(fitness_function)

    # TO DO
    def mutation(self):
        program = self.population[self.negative_tournament()]
        # coś tam

    # TO DO
    def crossover(self):
        program_1 = self.population[self.tournament()]
        program_2 = self.population[self.tournament()]
        # tu reszta

    def fitness(self, fitness_function):
        for i, individual in enumerate(self.population):
            self.fitnesses[i] = fitness_function(individual)

    def best_individual_fitness(self):
        max_arg = np.argmax(self.fitnesses)
        value = self.fitnesses[max_arg]
        self.best = self.population[max_arg]
        return int(max_arg), value

    def worst_individual_fitness(self):
        min_arg = np.argmin(self.fitnesses)
        value = self.fitnesses[min_arg]
        return int(min_arg), value

    def tournament(self):
        best = random.randint(0, len(self.population) - 1)
        best_fitness = -1.0e34
        for i in range(self.tournament_size):
            competitor = random.randint(0, len(self.population) - 1)
            if self.fitnesses[competitor] > best_fitness:
                best_fitness = self.fitnesses[competitor]
                best = competitor
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
        if var_dict.__len__() != 0:
            vars = vars[:-2]
        vars += " }"
        print(f'{vars}\n')

        self.population[index].output_data = self.interpret(self.population[index].str_program, var_dict, self.population[index].input_data)
        print("\nInput data:")
        print(self.population[index].input)

        print("\nOutput data:")
        print(self.population[index].output_data)
        print("---------------------\n")

        return self.population[index].__repr__()

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

    def interpret(self, input_data, variables, input_1):
        var = variables
        input_example = input_data

        input = InputStream(input_example)
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

    def get_task_cases(self):
        self.test_cases = self.task.test_cases

    def save_result_to_file(self, best_index, ok, best_fitness):
        path = f"./library/Tasks/outputs/{self.name}/result.txt"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            if not ok:
                f.write("Problem not solved :c\n")
            else:
                f.write(f"Problem solved!\n")
            f.write(self.print_individual(best_index))
            f.write("\n")
            f.write(f"Fitness values: {best_fitness}, Generation: {self.generation}\n")
