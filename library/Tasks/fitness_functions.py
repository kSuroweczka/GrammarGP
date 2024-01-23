from library.Model.program import Program
import numpy as np
import math


def fitness_1_1_A(individual: Program):
    output = np.array(individual.output_data)
    if output.shape[0] == 0:
        fitness = -1000
    elif 1.0 in output:
        fitness = 0.0
    else:
        fitness = -np.min(np.abs(output - 1.0))
    return fitness


def fitness_1_1_B(individual: Program):
    output = np.array(individual.output_data)

    if output.shape[0] == 0:
        fitness = -10000
    elif 789.0 in output:
        fitness = 0.0
    else:
        fitness = -np.min(np.abs(output - 789.0))
    return fitness


def fitness_1_1_C(individual: Program):
    output = np.array(individual.output_data)

    if output.shape[0] == 0:
        fitness = -100000
    elif 31415.0 in output:
        fitness = 0.0
    else:
        fitness = -np.min(np.abs(output - 31415.0))
    return fitness


def fitness_1_1_D(individual: Program):
    output = np.array(individual.output_data)
    if output.shape[0] == 0:
        fitness = -1000
    elif output[0] == 1.0:
        fitness = 0.0
    else:
        fitness = -abs(output[0] - 1.0)
    return fitness


def fitness_1_1_E(individual: Program):
    output = np.array(individual.output_data)
    if output.shape[0] == 0:
        fitness = -1000
    elif 789.0 in output:
        fitness = 0.0
    else:
        fitness = -abs(output[0] - 789.0)
    return fitness


def fitness_1_1_F(individual: Program):
    output = np.array(individual.output_data)
    if output.shape[0] == 0:
        fitness = -1000
    elif 1.0 in output:
        fitness = 0.0
    else:
        fitness = -np.min(np.abs(output - 1.0))

    fitness += (output.shape[0] - 1) * -10
    return fitness


def fitness_1_2_A_C(individual: Program):
    output = individual.output_data
    input_data = individual.input_data
    expected = input_data[0] + input_data[1]
    input = individual.input

    fitness = 0.0
    if abs(len(input) - 2) != 0:
        fitness -= abs(len(input) - 2) * 500

    if abs(len(output) - 1) != 0:
        fitness -= abs(len(output) - 1) * 500

    if len(output) == 1 and len(input) == 2:
        if output[0] == expected:
            fitness = 0.0
        else:
            fitness -= np.abs(expected - output[0])

    return fitness


def fitness_1_2_D(individual: Program):
    output = individual.output_data
    input_data = individual.input_data
    expected = input_data[0] - input_data[1]
    input = individual.input

    fitness = 0.0
    if abs(len(input) - 2) != 0:
        fitness -= abs(len(input) - 2) * 5000

    if abs(len(output) - 1) != 0:
        fitness -= abs(len(output) - 1) * 5000

    if len(output) == 1 and len(input) == 2:
        if output[0] == expected:
            fitness = 0.0
        else:
            fitness -= np.abs(expected - output[0])

    return fitness


def fitness_1_2_E(individual: Program):
    output = individual.output_data
    input_data = individual.input_data
    expected = input_data[0] * input_data[1]
    input = individual.input

    fitness = 0.0
    if abs(len(input) - 2) != 0:
        fitness -= abs(len(input) - 2) * 10000

    if abs(len(output) - 1) != 0:
        fitness -= abs(len(output) - 1) * 10000

    if len(output) == 1 and len(input) == 2:
        if output[0] == expected:
            fitness = 0.0
        else:
            fitness -= np.abs(expected - output[0])

    return fitness


def fitness_1_3(individual: Program):
    output = np.array(individual.output_data)
    input_data = np.array(individual.input_data)
    expected = np.max(input_data)

    input = individual.input
    if len(input) < 2:
        fitness = -100
    elif len(output) == 0:
        fitness = -100.0
    elif len(output) == 1:
        if output[0] == expected:
            fitness = 0.0
        else:
            fitness = -abs(expected - output[0])
    else:
        avg = np.average(output)
        fitness = (-1) * abs(avg - expected)
    fitness += abs(output.shape[0] - 1) * -10
    fitness += abs(len(input) - 2) * -10
    return fitness


def fitness_1_4_A(individual: Program):
    output = individual.output_data
    input_data = np.array(individual.input_data)
    expected = round(np.average(input_data))

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

def fitness_1_4_B(individual: Program):
    output = individual.output_data
    input_data = np.array(individual.input_data, dtype='int64')
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
        expected = np.average(input_data[1:n])

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


def fitness_4_11_7(individual: Program):
    output = individual.output_data
    input_data = np.array(individual.input_data)

    input = individual.input
    fitness = -abs(len(input) - 3) * 50

    out_size = (input_data[2] - input_data[0] + 1) // input_data[1]
    fitness -= abs(len(output) - out_size) * 50

    return fitness


def fitness_Bool(individual: Program):
    output = individual.output_data
    input_data = np.array(individual.input)
    expected = individual.task.test_cases[0].output_data
    k = len(expected)

    if len(output) == 0:
        fitness = -100.0
    elif len(output) == k:
        if output == expected:
            fitness = 0.0
        else:
            fitness = (-1) * np.abs(np.subtract(output,expected)).sum()
    else:
        fitness = -50.0
    fitness += abs(len(output) - k) * -10

    return fitness

def fitness_1_Bench(individual: Program):
    output = individual.output_data
    input_data = individual.input_data
    expected = input_data[0] + input_data[1]

    fitness = -100
    input = individual.input
    # if len(input) < 2:
    #     fitness = -100
    if len(output) == 0:
        fitness = -100.0
    elif len(output) == 1:
        if output[0] == expected:
            fitness = 0.0
        else:
            fitness = (-1) * np.abs(expected - output[0])
    else:
        avg = np.average(output)
        fitness = (-1) * np.abs(avg - expected)
    fitness += abs(len(output) - 1) * -20
    fitness += abs(len(input) - 2) * -20

    return fitness

def fitness_17_Bench(individual: Program):
    output = individual.output_data
    input_data = individual.input_data
    expected = 0
    for i in range(len(input_data)):
        expected += input_data[i] * input_data[i]

    fitness = -100
    if len(output) == 0:
        fitness = -100.0
    elif len(output) == 1:
        if output[0] == expected:
            fitness = 0.0
        else:
            fitness = (-1) * np.abs(expected - output[0])
    else:
        avg = np.average(output)
        fitness = (-1) * np.abs(avg - expected)
    fitness += abs(len(output) - 1) * -20

    return fitness

def fitness_27_Bench(individual: Program):
    output = individual.output_data
    input_data = individual.input_data
    expected = 0
    if len(input_data) % 2:
        expected = (input_data[len(input_data) // 2 ] + input_data[len(input_data) // 2 + 1])/2
    else:
        expected = input_data[len(input_data) // 2 ]

    fitness = -100
    if len(output) == 0:
        fitness = -100.0
    elif len(output) == 1:
        if output[0] == expected:
            fitness = 0.0
        else:
            fitness = (-1) * np.abs(expected - output[0])
    else:
        avg = np.average(output)
        fitness = (-1) * np.abs(avg - expected)
    fitness += abs(len(output) - 1) * -20

    return fitness



