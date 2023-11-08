ADD = 110
SUB = 111
MUL = 112
DIV = 113
FSET_START = ADD
FSET_END = DIV

MAX_LEN = 10000
POPSIZE = 100000
DEPTH   = 5
GENERATIONS = 100
TSIZE = 2
PMUT_PER_NODE  = 0.05
CROSSOVER_PROB = 0.9

class Parameters:
    fitness: list[float]
    pop=list[str]
    x: list[float]
    minrandom: float
    maxrandom: float
    program:list[str]
    PC:int
    varnumber:int
    fitnesscases:int
    randomnumber:int
    fbestpop = 0.0
    favgpop = 0.0
    seed: float
    avg_len: float
    targets:list[list[float]] 

    def __init__():
        pass