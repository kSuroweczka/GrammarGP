from library.Tasks.task import *
from library.Model.program import *
from library.Solver.GP import *
from library.Solver.interpreter import *

task_name = '1_1_A'
params = Params(max_depth=5, popsize=1)

gp = GP(task_name=task_name, params=params)


gp.print_population()





