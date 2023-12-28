from library.Solver.GP import *
from library.Tasks.fitness_functions import *

task_name = '1_1_A'
params = Params(max_depth=4, popsize=10)
gp = GP(task_name=task_name, params=params)

# it should work like this:
gp.run(fitness_function=fitness_1_1_A)






