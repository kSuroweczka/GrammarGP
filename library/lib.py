import random
import copy

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

class GeneticProgrammingLibrary:
    def __init__(self, max_depth):
        self.max_depth = max_depth

    def generate_random_program(self, depth=None):
        if depth is None:
            depth = random.randint(1, self.max_depth)
        if depth == 1:
            return Node(random.choice(['input', 'constant', 'operation']))
        else:
            node = Node(random.choice(['operation', 'input']))
            for _ in range(random.randint(1, 3)):
                node.add_child(self.generate_random_program(depth - 1))
            return node

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
    






gp_library = GeneticProgrammingLibrary(max_depth=3)

# Generujemy losowe programy
program1 = gp_library.generate_random_program()
program2 = gp_library.generate_random_program()

# Ocena programów na podstawie danych wejściowych
input_data = [3, 5]
output1 = gp_library.evaluate_program(program1, input_data)
output2 = gp_library.evaluate_program(program2, input_data)

print("Program 1 (ocena):", output1)
print("Program 2 (ocena):", output2)

# Krzyżowanie programów
new_program1, new_program2 = gp_library.crossover(program1, program2)

# Mutacja programów
mutated_program1 = gp_library.mutate(program1)
mutated_program2 = gp_library.mutate(program2)

# Selekcja programów
population = [program1, program2, new_program1, new_program2, mutated_program1, mutated_program2]
selected_program = gp_library.tournament_selection(population)

print("Nowy wybrany program (ocena):", gp_library.evaluate_program(selected_program, input_data))

# Serializacja i deserializacja programu
serialized_program = gp_library.serialize_program(selected_program)
print("Serialized Program:", serialized_program)

deserialized_program = gp_library.deserialize_program(serialized_program)
print("Deserialized Program (ocena):", gp_library.evaluate_program(deserialized_program, input_data))