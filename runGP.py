from library.Solver.GP import *
from library.Tasks.fitness_functions import *

task_name = '1_2_A'
params = Params(max_depth=4, popsize=50, min_rand=0, max_rand=9)
gp = GP(task_name=task_name, params=params)

gp.run(fitness_function=fitness_1_2_A_C)





