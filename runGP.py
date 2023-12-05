from library.Tasks.task import *
from library.Model.program import *
from library.Solver.GP import *
from library.Solver.interpreter import *

task_name = '1_1_A'

gp = GP(set_seed=None, task_name=task_name)


gp.print_population()

# TO DO 
# parsed_program = parsProgram(gp.popuation[0])
# print(parsed_program)

# new_program = runProgram(gp.popuation[0])




