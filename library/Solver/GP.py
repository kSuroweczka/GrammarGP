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

    def create_population(self, task: Task, params: Params):
        self.name = task.name
        pop = []

        for _ in range(params.popsize):
            p = Program(task, params.max_depth)
            p.createIndividual()
            pop.append(p)

        return pop