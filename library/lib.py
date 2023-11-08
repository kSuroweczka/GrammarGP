import random
import copy
from enum import Enum

from library import Parameters

class NodeType(Enum):
    INPUT = 'INPUT'
    CONSTANT = 'CONSTANT'
    OPERATION = 'OPERATION'

class TreeType(Enum):
    GROW = 1
    FULL = 2
    HALF_AND_HALF = 3

class Node:
    type: NodeType
    value: str
    children: list['Node']
    isRoot: bool

    def __init__(self, value, isRoot=False):
        self.type = NodeType(value)
        self.value = value
        self.children = []
        self.isRoot = isRoot
    
    def __repr__(self):
        return f"Node({self.value}, children:{self.children})"

    def add_child(self, child_node):
        self.children.append(child_node)

Program = list[Node]

class GeneticProgrammingLibrary:
    fitness: list[float]
    program: Program
    population: list[Program]
    params: Parameters.Params
    input_data: list[float]

    def __init__(self, Params: Parameters.Params):
        self.params = Params
        self.generation = 0
        self.population = self.initialize_population(self.params.max_depth)
        self.fitness: list[float] = [0.0 for _ in range(self.params.popsize)]


        # x: list[float]
        # PC:int
        # fbestpop = 0.0
        # favgpop = 0.0
        # targets:list[list[float]] 
        
    def grow(self, depth=None):
        if depth is None:
            depth = random.randint(1, self.params.max_depth)
        if depth == 1:
            return Node(random.choice(['INPUT', 'CONSTANT', 'OPERATION']), isRoot=True)
        else:
            node = Node(random.choice(['CONSTANT', 'OPERATION']))
            for _ in range(random.randint(1, 3)):
                node.add_child(self.grow(depth - 1))
            return node


    def generate_random_program(self, depth: int, tree_type=TreeType.GROW):
        if tree_type == TreeType.GROW:
            return self.grow(depth)
        else:
            print("Not implemented")
        # elif tree_type == TreeType.FULL:
        #     return self.full(depth)
        # elif tree_type == TreeType.HALF_AND_HALF:
        #     return self.half_and_half(depth)
        
    def initialize_population(self, depth: int):
        return [self.generate_random_program(depth=depth) for _ in range(self.params.popsize)]
        
    def crossover(self, program1, program2):
        new_program1 = copy.deepcopy(program1)
        new_program2 = copy.deepcopy(program2)
        # Perform crossover operation (swap subtrees) between new_program1 and new_program2
        return new_program1, new_program2

    def mutate(self, program):
        new_program = copy.deepcopy(program)
        # Perform mutation operation (modify subtree or replace subtree with a new random subtree)
        return new_program

    def evaluate_program(self, program, input_data):
        # Evaluate the fitness of the program based on input_data and output_data
        def evaluate_node(node,input_data):
            if node.value == 'input':
                # Pobierz wartość zmiennej wejściowej z input_data (indeksowanie od 0)
                return input_data[int(random.uniform(0, len(input_data)))]
            elif node.value == 'constant':
                # Ustaw stałą wartość (dla przykładu 1)
                return 1
            elif node.value == 'operation':
                # Pobierz wartości z dzieci (rekurencyjnie) i wykonaj odpowiednią operację arytmetyczną
                if len(node.children) == 2:
                    left_value = evaluate_node(node.children[0])
                    right_value = evaluate_node(node.children[1])
                    if random.choice([True, False]):
                        return left_value + right_value
                    else:
                        return left_value - right_value
                else:
                    # Obsługa innych operacji arytmetycznych
                    pass
        return evaluate_node(program, input_data)

    def tournament_selection(self, population, k=2):
        tournament_players = random.sample(population, k)
        # Return the best program from the tournament
        return max(tournament_players, key=lambda program: self.evaluate_program(program, input_data))

    def serialize_program(self, program):
        # Serialize the program to a string or a data structure
        # Prosta serializacja drzewa do listy (pre-order traversal)
        def serialize_node(node):
            serialized = [node.value]
            for child in node.children:
                serialized.extend(serialize_node(child))
            return serialized

        return serialize_node(program)

    def deserialize_program(self, serialized_program):
        # Deserialize the program from a string or a data structure
        # Prosta deserializacja listy na drzewo
        def deserialize_node(serialized_iter):
                value = next(serialized_iter)
                node = Node(value)
                while value not in ['input', 'constant', 'operation']:
                    node.add_child(deserialize_node(serialized_iter))
                    value = next(serialized_iter)
                return node
        return deserialize_node(iter(serialized_program))
    