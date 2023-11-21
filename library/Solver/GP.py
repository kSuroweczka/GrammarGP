from library.Model.program import Program
from library.Solver.params import Params
from library.Tasks.task import Task

class GP():
    name: str
    popuation: list[Program]
    best: Program
    best_fitness: float
    best_generation: int
    params: Params
    task: Task
    generation: int

    def __init__(self, name: str, set_seed: int | None = None, params: Params | None = None):
        self.popuation = []
        self.best = None
        self.best_fitness = 0.0
        self.best_generation = 0
        self.generation = 0
        self.task = Task(name)

        self.params = params or Params(seed=set_seed, max_depth=3)
        self.popuation = self.create_population(self.task, self.params)

    def get_task_cases(self):
        return self.task.test_cases

    def create_population(self, task: Task, params: Params):
        # print(params)
        
        self.name = task.name
        pop = []

        for _ in range(params.popsize):
            p = Program(task, params.max_depth, params.min_rand, params.max_rand)
            p.createIndividual()
            pop.append(p)

        return pop
    
    def print_individual(self, index: int):
        print("---------------------")
        print(f"Individual: {index}\n")
        print("Program: ")
        print(self.popuation[index])

        print("Variables:")
        print(self.popuation[index].variables)

        print("\nRoot children:")
        for child in self.popuation[index].ROOT.children_nodes:
            print(child)
        print("---------------------\n")