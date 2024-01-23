from library.Solver.GP import *
from library.Tasks.fitness_functions import *

task_name = '1_2_A'
params = Params(max_depth=4, popsize=50, min_rand=-100, max_rand=100, generations=100, pmut_per_node=0.4)
gp = GP(task_name=task_name, params=params)

gp.run(fitness_function=fitness_1_2_A)

# for i in range(1,11):
#     for j in range(1,5):
#         task_name = f'Bool_{i}_{j}'
#         params = Params(max_depth=2, popsize=50, min_rand=-5, max_rand=5, generations=100)
#         gp = GP(task_name=task_name, params=params)
#         gp.run(fitness_function=fitness_Bool)



