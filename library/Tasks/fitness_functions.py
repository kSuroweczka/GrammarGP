from library.Model.program import Program
import numpy as np
import math


def fitness_1_1_A(individual: Program):
    output = np.array(individual.output_data)
    if output.shape[0] == 0:
        fitness = -100
    elif 1.0 in output:
        fitness = 0.0
    else:
        fitness = -np.sum(np.abs(output - 1.0))
    return fitness


def fitness_1_1_B(individual: Program):
    output = np.array(individual.output_data)
    if output.shape[0] == 0:
        fitness = -100
    elif 789.0 in output:
        fitness = 0.0
    else:
        fitness = -np.sum(np.abs(output - 789.0))
    return fitness


def fitness_1_1_C(individual: Program):
    output = np.array(individual.output_data)
    if output.shape[0] == 0:
        fitness = -100
    elif 31415.0 in output:
        fitness = 0.0
    else:
        fitness = -np.sum(np.abs(output - 31415.0))
    return fitness


def fitness_1_1_D(individual: Program):
    output = np.array(individual.output_data)
    if output.shape[0] == 0:
        fitness = -100
    elif 1.0 in output[0]:
        fitness = 0.0
    else:
        fitness = -abs(output[0] - 1.0)
    return fitness


def fitness_1_1_E(individual: Program):
    output = np.array(individual.output_data)
    if output.shape[0] == 0:
        fitness = -100
    elif 789.0 in output[0]:
        fitness = 0.0
    else:
        fitness = -abs(output[0] - 789.0)
    return fitness


def fitness_1_1_F(individual: Program):
    output = np.array(individual.output_data)
    if output.shape[0] == 0:
        fitness = -100
    elif 1.0 in output[0]:
        fitness = 0.0
    else:
        fitness = -np.sum(np.abs(output - 1.0))

    fitness += (output.shape[0] - 1) * -10
    return fitness


def fitness_1_2_A_C(individual: Program):
    output = np.array(individual.output_data)
    input_data = np.array(individual.input_data)
    expected = np.sum(input_data)

    input = individual.input
    if len(input) < 2:
        fitness = -100
        return fitness

    if len(output) == 0:
        fitness = -1000.0
    elif len(output) == 1:
        if output[0] == expected:
            fitness = 0.0
        else:
            fitness = (-1) * np.abs(expected - output[0])
    else:
        avg = np.average(output)
        fitness = (-1) * np.abs(avg - expected)
    fitness += (output.shape[0] - 1) * -10
    fitness += (len(input) - 2) * -10

    return fitness


def fitness_1_2_D(individual: Program):
    output = individual.output_data
    input_data = individual.input_data
    expected = input_data[0] - input_data[1]

    input = individual.input
    if len(input) < 2:
        fitness = -100
        return fitness

    if len(output) == 0:
        fitness = -1000.0
    elif len(output) == 1:
        if output[0] == expected:
            fitness = 0.0
        else:
            fitness = (-1) * np.abs(expected - output[0])
    else:
        avg = np.average(output)
        fitness = (-1) * np.abs(avg - expected)
    fitness += (len(output) - 1) * -10
    fitness += (len(input) - 2) * -10

    return fitness


def fitness_1_2_E(individual: Program):
    output = individual.output_data
    input_data = individual.input_data
    expected = input_data[0] * input_data[1]

    input = individual.input
    if len(input) < 2:
        fitness = -100
        return fitness

    if len(output) == 0:
        fitness = -1000.0
    elif len(output) == 1:
        if output[0] == expected[0]:
            fitness = 0.0
        else:
            fitness = (-1) * np.abs(expected - output[0])
    else:
        avg = np.average(output)
        fitness = (-1) * np.abs(avg - expected)
    fitness += (len(output) - 1) * -10
    fitness += (len(input) - 2) * -10
    return fitness

def fitness_1_3(individual: Program):
    output = individual.output_data
    input_data = individual.input_data
    expected = max(input_data)

    input = individual.input
    if len(input) < 1:
        fitness = -100
        return fitness

    if len(output) == 0:
        fitness = -1000.0
    elif len(output) == 1:
        if output[0] == expected:
            fitness = 0.0
        else:
            fitness = (-1) * np.abs(expected - output[0])
    else:
        avg = np.average(output)
        fitness = (-1) * np.abs(avg - expected)

    fitness += (len(output) - 1) * -10
    fitness += (len(input) - 2) * -10
    return fitness


def fitness_1_4_A(individual: Program):
    output = individual.output_data
    input_data = np.array(individual.input_data)
    expected = round(np.average(input_data))

    if len(output) == 0:
        fitness = -10.0
    elif len(output) == 1:
        if output == expected:
            fitness = 0.0
        else:
            fitness = (-1) * np.abs(output[0] - expected)
    else:
        avg = int(np.average(output))
        fitness = (-1) * np.abs(avg - expected)
    fitness += (len(output) - 1) * -10
    return fitness

def fitness_1_4_B(individual: Program):
    output = individual.output_data
    input_data = np.array(individual.input_data)
    input_len = len(input_data)

    input = individual.input
    if len(input) < 2:
        fitness = -100
        return fitness

    n = input_data[0]
    if n > input_len - 1:
        a = math.ceil(n / input_len)
        input_data.repeat(input_data, a)
        expected = np.average(input_data)
    else:
        expected = np.average(input_data[1:n+1])

    if len(output) == 0:
        fitness = -1000.0
    elif len(output) == 1:
        if output == expected:
            fitness = 0.0
        else:
            fitness = (-1) * np.abs(output[0] - expected)
    else:
        avg = int(np.average(output))
        fitness = (-1) * np.abs(avg - expected)
    fitness += (len(output) - 1) * -10
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


