from library.Model.program import Program
from library.Solver.params import Params
from library.Tasks.task import Task, TestCase
import random

class GP():
    name: str
    popuation: list[Program]
    best: Program
    best_fitness: float
    best_generation: int
    params: Params
    task: Task
    test_cases: list[TestCase] # list of TestCase objects from library/Tasks/task.py
    generation: int

    def __init__(self, task_name: str, set_seed: int | None = None, params: Params | None = None):
        self.popuation = []
        self.best = None
        self.best_fitness = 0.0
        self.best_generation = 0
        self.generation = 0
        self.task = Task(task_name)
        self.params = params or Params(seed=set_seed, max_depth=3)
        self.popuation = self.create_population(self.task, self.params)
        self.test_cases = []


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
        print(f"Individual: {self.popuation[index].id}\n")
        print("Program: ")
        print(self.popuation[index])

        print("Variables:")
        print(self.popuation[index].variables)

        print("\nRoot children:")
        for child in self.popuation[index].ROOT.children_nodes:
            print(child)

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