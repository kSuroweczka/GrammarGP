from library.Solver.GP import *
from library.Tasks.fitness_functions import *

task_name = '1_Bench'
params = Params(max_depth=2, popsize=50, min_rand=-9000, max_rand=9000, generations=100)
gp = GP(task_name=task_name, params=params)

gp.run(fitness_function=fitness_27_Bench)

for i in range(1,11):
    for j in range(1,5):
        task_name = f'Bool_{i}_{j}'
#         exec(f'x= fitness_Bool')
#         res = x()
        params = Params(max_depth=2, popsize=50, min_rand=-5, max_rand=5, generations=100)
        gp = GP(task_name=task_name, params=params)
        gp.run(fitness_function=fitness_Bool)

for i in [1,17,27]:
    task_name = f'{i}_Bench'
    exec(f'x= fitness_{i}_Bench')
    params = Params(max_depth=2, popsize=50, min_rand=-5, max_rand=5, generations=100)
    gp = GP(task_name=task_name, params=params)
    gp.run(fitness_function=exec(f'fitness_{i}_Bench'))



