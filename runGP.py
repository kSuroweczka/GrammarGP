from library.Tasks.task import *
from library.Model.program import *

task_name = '1_1_A'
task = Task(task_name)

program = Program(task, 3)

program.createIndividual()
print(program)