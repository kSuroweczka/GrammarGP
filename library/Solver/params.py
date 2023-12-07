import random
from datetime import datetime

class Params:
    seed: int
    min_rand: float
    max_rand: float
    max_len: float
    popsize: int
    max_depth: int
    generations: int
    tournament_size: int
    pmut_per_node: float
    crossover_prob: float

    def __init__(self, seed: int | None, min_rand: float = -5, max_rand: float = 5, 
                 max_len: float = 10, popsize: int = 10, max_depth: int = 5, 
                 generations: int = 100, tournament_size: int = 2, pmut_per_node: float = 0.15, 
                 crossover_prob: float = 0.85):
        seed = seed or datetime.now().timestamp()
        random.seed(seed)
        self.seed = seed

        self.min_rand = min_rand
        self.max_rand = max_rand
        self.max_len = max_len
        self.popsize = popsize
        self.max_depth = max_depth
        self.generations = generations
        self.tournament_size = tournament_size
        self.pmut_per_node = pmut_per_node
        self.crossover_prob = crossover_prob

    def __repr__(self) -> str:
        return (
            "SEED="
            + str(self.seed)
            + "\nMAX_LEN="
            + str(self.max_len)
            + "\nPOPSIZE="
            + str(self.popsize)
            + "\nMAX_DEPTH="
            + str(self.max_depth)
            + "\nMIN_RANDOM="
            + str(self.min_rand)
            + "\nMAX_RANDOM="
            + str(self.max_rand)
            + "\nCROSSOVER_PROB="
            + str(self.crossover_prob)
            + "\nPMUT_PER_NODE="
            + str(self.pmut_per_node)
            + "\nGENERATIONS="
            + str(self.generations)
            + "\nTSIZE="
            + str(self.tournament_size)
            + "\n----------------------------------\n"
        )
