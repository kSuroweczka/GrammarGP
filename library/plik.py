# Przykład użycia biblioteki do generowania, ewolucji, oceny i serializacji/deserializacji programów

# Importujemy naszą bibliotekę
from lib2 import *


# Tworzymy instancję biblioteki z maksymalną głębokością drzewa 3
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