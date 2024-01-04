from library.Solver.GP import *
from library.Tasks.fitness_functions import *

task_name = '1_Bench'
params = Params(max_depth=2, popsize=50, min_rand=-5, max_rand=5, generations=100)
gp = GP(task_name=task_name, params=params)

gp.run(fitness_function=fitness_27_Bench)





