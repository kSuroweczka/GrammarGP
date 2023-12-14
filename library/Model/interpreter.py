from library.Model.program import Program
from library.Model.node import *

class Interpreter():
    program: Program
    task_name: str
    variables: dict[str, VarNode]
    const: list[float]
    input_data: list[float]
    output_data: list[float]

    def __init__(self, program: Program, task_name: str):
        self.program = program
        self.task_name = task_name
        self.variables = {}
        self.const = {}
        self.input_data = []