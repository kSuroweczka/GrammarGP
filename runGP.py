from library.Solver.GP import *
from library.Tasks.fitness_functions import *

task_name = '1_1_F'
params = Params(max_depth=2, popsize=50, min_rand=-9000, max_rand=9000, generations=100)
gp = GP(task_name=task_name, params=params)

gp.run(fitness_function=fitness_1_1_F)





