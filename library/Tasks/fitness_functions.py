from library.Model.program import Program
import numpy as np


def fitness_1_1_A(individual: Program):
    output = np.array(individual.output_data)
    if output.shape[0] == 0:
        fitness = -100
    elif 1.0 in output:
        fitness = 0.0
    else:
        fitness = -np.sum(np.abs(output - 1.0))
    return fitness

# def fitness_1_1(output_data, where: int, only: bool, individual: Program):
#     fitness = -100.0
#     print("\n")
#     print("SINGLE FITNESS 1_1")
#     print("individual: ", individual.output_data)
#     expected = output_data[0]
#
#     if type(individual.output_data) == list:
#         if len(individual.output_data) == 0:
#             # print("pusta lista, ", individual.output_data)
#             fitness = -10.0
#         elif individual.output_data == expected or expected in individual.output_data:
#             if where is None:
#                 if only:
#                     if len(individual.output_data) == 1:
#                         fitness = (-1) * np.abs(expected - individual.output_data[0])
#                         # print("fitness gdy only i len == 1: ", fitness)
#                     else:
#                         avg = np.average(individual.output_data)
#                         fitness = (-1) * np.abs(avg)
#                         # print("fitness only i len!=1: ", fitness)
#                 else:
#                     fitness = 0.0
#             else:
#                 if individual.output_data[where] == expected:
#                     fitness = 0.0
#                 else:
#                     fitness = (-1) * np.abs(expected - individual.output_data[where])
#         elif expected not in individual.output_data and where is None:
#             sub = np.abs(np.subtract(expected, individual.output_data))
#             fitness = (-1) * np.min(sub)
#             # print("nie ma w liscie, ", fitness)
#     print("single fitness: ", fitness)
#     return fitness


def single_fitness_1_2(self, individual: Program):
    #### operation, min i max przedziału w pliku task
    print("\n")
    print("SINGLE FITNESS 1_2")
    print("individual: ", individual.output_data)

    output = individual.output_data
    expected = self.task.test_cases[0].output_data
    fitness = -100.0

    if len(output) == 0:
        fitness = -10.0
    elif len(output) == 1:
        if output[0] == expected[0]:
            fitness = 0.0
        else:
            fitness = (-1) * np.abs(expected[0] - output[0])
    elif len(output) > 1:
        avg = np.average(output)
        fitness = (-1) * np.abs(avg - expected[0])
    print("single fitness: ", fitness)
    return fitness


def single_fitness_1_3(self, list_on_input: list, operator: str, min: float, max: float):
    ### to co w single_fitness_1_2 raczej wystarczy
    pass


def single_fitness_1_4(self, individual: Program):
    ### w sumie to to samo co w single_fitness_1_2
    print("\n")
    print("SINGLE FITNESS 1_4")
    print("individual: ", individual.output_data)
    output = individual.output_data
    expected = self.task.test_cases[0].output_data
    fitness = -100.0
    if len(output) == 0:
        fitness = -10.0
    elif len(output) == 1:
        if output == expected:
            fitness = 0.0
        else:
            fitness = (-1) * np.abs(output[0] - expected[0])
    elif len(output) > 1:
        avg = int(np.average(output))
        fitness = (-1) * np.abs(avg - expected[0])
    print("single fitness: ", fitness)
    return fitness