from library.Tasks.task import *
from library.Model.program import *
from library.Solver.GP import *

task_name = '1_1_A'

gp = GP(set_seed=42, name=task_name)
print(gp.popuation[0])
