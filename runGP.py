from library.Solver.GP import *
from library.Tasks.fitness_functions import *
from library.Solver.Interpreter import *

# do pokazania przykładu działania interpretera
# interpreter = Interpreter()
# interpreter.interpret()

task_name = '1_4_B'
params = Params(max_depth=2, popsize=50, min_rand=-5, max_rand=5, generations=100)
gp = GP(task_name=task_name, params=params)

gp.run(fitness_function=fitness_1_4_B)

# for i in range(7,11):
#     for j in range(1,5):
#         task_name = f'Bool_{i}_{j}'
#         params = Params(max_depth=2, popsize=50, min_rand=-5, max_rand=5, generations=100)
#         gp = GP(task_name=task_name, params=params)
#         if j == 1:
#             gp.run(fitness_function=fitness_Bool_NOT)
#         if j == 2:
#             gp.run(fitness_function=fitness_Bool_AND)
#         if j == 3:
#             gp.run(fitness_function=fitness_Bool_OR)
#         if j == 4:
#             gp.run(fitness_function=fitness_Bool_XOR)



