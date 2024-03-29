from contextlib import redirect_stdout

from library.Model.program import Program
from library.Solver.params import Params
from library.Tasks.task import Task, TestCase
from library.Solver.Interpreter import Interpreter
import random
from library.Model.node import *
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
    interpreter: Interpreter

    def __init__(self, task_name: str, set_seed: int | None = None, params: Params | None = None):
        self.population = []
        self.params = params or Params(seed=set_seed, max_depth=1)
        self.best_fitness = -1000000.0
        self.fitnesses = self.initialize_fitness()
        self.best_generation = 0
        self.generation = 0
        self.task = Task(task_name)
        self.population = self.create_population(self.task, self.params)
        self.test_cases = []
        self.tournament_size = 2
        self.interpreter = Interpreter()

    def create_population(self, task: Task, params: Params):
        self.name = task.name
        pop = []

        for i in range(params.popsize):
            index = random.randint(0, len(task.test_cases) - 1)
            test_case = task.test_cases[index]

            p = Program(i, task, params.max_depth, params.min_rand, params.max_rand, test_case.input_data)
            p.create_individual()

            pop.append(p)

        return pop

    def evaluate(self, fitness_function):
        self.print_population()

        while self.generation < self.params.generations:
            for i, individual in enumerate(self.population):
                self.population[i].output_data, self.population[i].input, self.population[i].vars = self.interpreter.interpret(individual)

            self.fitness(fitness_function)
            best_index, best_fitness = self.best_individual_fitness()

            if best_fitness == 0.0:
                print("Problem solved!\n")
                break
            else:
                print("------------------------------")
                print(f"Generation: {self.generation+1}")
                print(f"Best fitness: {best_fitness}")
                self.print_individual(best_index)

                rand_op = random.random()
                if rand_op < self.params.crossover_prob:
                    self.crossover()
                else:
                    self.mutation()

                worst_index, worst_fitness = self.worst_individual_fitness()
                worst = self.population[worst_index]
                p = Program(worst.id, worst.task, self.params.max_depth, self.params.min_rand, self.params.max_rand, worst.input_data)
                p.create_individual()
                self.population[worst_index] = p
                self.population[worst_index].output_data, self.population[worst_index].input, self.population[
                    worst_index].vars = self.interpreter.interpret(individual)
                print("\n\n")

            self.generation += 1

        best_index, best_fitness = self.best_individual_fitness()

        if best_fitness != 0.0:
            print(f"Problem not solved :c\n")
            print(f"Best fitness: {self.best_fitness}\n")

    def run(self, fitness_function):
        self.evaluate(fitness_function)

    def mutation(self):

        print("\n------------\n MUTATION \n------------\n")
        id = self.negative_tournament()
        program = self.population[id]

        print("\n------------\n OLD PROGRAM \n------------\n")
        print(self.population[id])

        self.population[id].ROOT = self.walk_tree(program)
        self.population[id].output_data, self.population[id].input, self.population[id].vars = self.interpreter.interpret(self.population[id])

        print("\n------------\n NEW PROGRAM \n------------\n")
        print(self.population[id])

    # node -> root_copy
    def walk_tree(self, program):
        new_program = self.deep_copy_tree(program.ROOT)
        for child in new_program.children_nodes:
            mutate_rand = random.random()
            if mutate_rand < self.params.pmut_per_node:
                new_program = self.mutate(node=child, node_parent=new_program, program=program)

        return new_program

    def mutate(self, node, node_parent, program: Program):
        possible_nodes = []
        if isinstance(node, float) or isinstance(node, bool):
            print(f"\nOLD NODE: {node} ,type: {type(node)}")
            node_parent.value = random.choice([random.randrange(int(self.params.min_rand), int(self.params.max_rand)), True, False])
            print(f"NEW NODE: {node_parent.value} ,type: {type(node)}")
        else:
            print(f"\nOLD NODE: {node} ,type: {node.node_type}")
            match node.node_type:
                case NodeType.INPUT:
                    possible_nodes = [NodeType.EXPRESSION, NodeType.CONDITION]
                case NodeType.OUTPUT | NodeType.ASSIGNMENT | NodeType.IF | NodeType.WHILE:
                    possible_nodes = [NodeType.ASSIGNMENT, NodeType.OUTPUT, NodeType.IF, NodeType.WHILE]
                case NodeType.VAR:
                    possible_nodes = [NodeType.VAR]
                case NodeType.SCOPE:
                    possible_nodes = [NodeType.SCOPE]
                case NodeType.CONDITION:
                    possible_nodes = [NodeType.CONDITION, NodeType.EXPRESSIONCONDITION]
                case NodeType.EXPRESSIONCONDITION:
                    possible_nodes = [NodeType.EXPRESSIONCONDITION, NodeType.CONDITION]
                case NodeType.EXPRESSION:
                    possible_nodes = [NodeType.EXPRESSION, NodeType.VAR, NodeType.TERM]
                case NodeType.FACTOR:
                    possible_nodes = [NodeType.FACTOR]
                case NodeType.TERM:
                    possible_nodes = [NodeType.TERM]
                case NodeType.BOOLEAN:
                    possible_nodes = [NodeType.BOOLEAN, NodeType.EXPRESSION, NodeType.CONDITION]

            if len(possible_nodes) == 0:
                return

            random_node = random.choice(possible_nodes)
            new_node = program.createNode(random_node, None, self.params.max_depth // 2)

            print(f"NEW NODE: {new_node} ,type: {new_node.node_type}")
            return self.replace_node(node_parent, node, new_node)


    def crossover(self):
        print("\n------------\n CROSSOVER \n------------\n")

        id_1 = self.tournament()
        id_2 = self.tournament()

        while id_1 == id_2:
            id_2 = self.tournament()

        program_1 = self.deep_copy_tree(self.population[id_1].ROOT)
        program_2 = self.deep_copy_tree(self.population[id_2].ROOT)

        node_1 = self.draw_subnode_1(program_1)
        node_2 = self.draw_subnode_2(program_2, node_1)

        self.population[id_1].ROOT = self.replace_node(program_1, node_1, node_2)
        self.population[id_2].ROOT = self.replace_node(program_2, node_2, node_1)

        self.population[id_1].output_data, self.population[id_1].input, self.population[id_1].vars = self.interpreter.interpret(self.population[id_1])
        self.population[id_2].output_data, self.population[id_2].input, self.population[id_2].vars = self.interpreter.interpret(self.population[id_2])


    @staticmethod
    def draw_subnode_1(tree):
        random_node = random.choice(tree.children_nodes)
        print("RANDOM NODE: ", random_node)
        return random_node

    @staticmethod
    def draw_subnode_2(tree, first_node):
        node_types = [NodeType.INPUT, NodeType.IF, NodeType.WHILE, NodeType.OUTPUT, NodeType.ASSIGNMENT]

        if first_node.node_type in node_types:
            random_node = random.choice(tree.children_nodes)
            while random_node.node_type in node_types:
                random_node = random.choice(tree.children_nodes)
                if random_node.node_type in node_types:
                    print("RANDOM NODE 2 : ", random_node)
                    return random_node
        else:
            random_node = random.choice(tree.children_nodes)
            while random_node.node_type == first_node.node_type:
                random_node = random.choice(tree.children_nodes)
                if random_node.node_type == first_node.node_type:
                    print("RANDOM NODE 2 : ", random_node)
                    return random_node

    @staticmethod
    def replace_node(tree, node_1, node_2):
        print("TREE BEFORE: ", tree)
        parent_1 = None
        parent_2 = None
        for child in tree.children_nodes:
            if child == node_1:
                parent_1 = node_1.parent_node

        for i in range(len(tree.children_nodes)):
            if tree.children_nodes[i] == node_1:
                tree.children_nodes.remove(tree.children_nodes[i])
                tree.children_nodes.insert(i, node_2)
        print("TREE AFTER: ", tree)
        return tree

    def fitness(self, fitness_function):
        for i, individual in enumerate(self.population):
            if len(individual.output_data) == 1 and individual.output_data[0] == -100000:
                self.fitnesses[i] = -100000
            else:
                self.fitnesses[i] = fitness_function(individual)

    def best_individual_fitness(self):
        max_arg = np.argmax(self.fitnesses)
        value = self.fitnesses[max_arg]
        if value > self.best_fitness:
            self.best_fitness = float(value)
            self.save_result_to_file(int(max_arg), float(value))
        return int(max_arg), value

    def worst_individual_fitness(self):
        min_arg = np.argmin(self.fitnesses)
        value = self.fitnesses[min_arg]
        return int(min_arg), value

    def tournament(self):
        pop_len = len(self.population)
        indexes = list(np.linspace(0, pop_len-1, pop_len-1, dtype='int'))
        best = random.choice(indexes)
        indexes.remove(best)
        best_fitness = -1.0e34
        for i in range(self.tournament_size):
            competitor = random.choice(indexes)
            indexes.remove(competitor)
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

        self.population[index].__repr__()
        print("\nInput data:")
        print(self.population[index].input)

        print("\nOutput data:")
        print(self.population[index].output_data)
        print("---------------------\n")

        print("Variables:")
        print(f'{self.population[index].vars}\n')

        return self.population[index].__repr__()

    def print_population(self):
        print(f"Task: {self.name}")
        print(self.params)
        print(f"Generation: {self.generation}\n")
        for i in range(len(self.population)):
            self.print_individual(i)

    @staticmethod
    def deep_copy_tree(tree: Node):
        new_tree = ScopeNode(NodeType.SCOPE, None,[])
        for child in tree.children_nodes:
            new_tree.children_nodes.append(child)
        # print("\nNEW_TREE (copy):   ", new_tree)
        return new_tree

    def initialize_fitness(self):
        array = np.empty(self.params.popsize, dtype=np.float32)
        array.fill(-100.0)
        return array

    def get_task_cases(self):
        self.test_cases = self.task.test_cases

    def save_result_to_file(self, best_index, best_fitness):
        path = f"./library/Tasks/outputs/{self.name}/result.txt"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            if best_fitness != 0:
                f.write("Problem not solved :c\n")
            else:
                f.write(f"Problem solved!\n")
            f.write(self.print_individual(best_index))
            f.write("\n")
            f.write(f"Fitness values: {best_fitness}, Generation: {self.generation}\n")
            f.write(f"Input: {self.population[best_index].input}\n")
            f.write(f"Output: {self.population[best_index].output_data}\n")
