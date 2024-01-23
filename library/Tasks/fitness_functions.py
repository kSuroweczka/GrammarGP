from library.Model.program import Program
import numpy as np
import math


### solved problems:
### 1_1_A, 1_1_D, 1_1_F, 1_2_A,


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
        fitness = -np.average(np.abs(output - 789.0)) - 300.0
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

###--------------------------------------------
###                    1_1_D
###--------------------------------------------

# def fitness_1_1_D(individual: Program):
#     output = np.array(individual.output_data)
#     if output.shape[0] == 0:
#         fitness = -1000
#     elif 1.0 in output:
#         fitness = 0.0
#     else:
#         fitness = -abs(output[0] - 1.0)
#     return fitness

def fitness_1_1_D(individual: Program):
    output = np.array(individual.output_data)
    if output.shape[0] == 0:
        fitness = -1000
    elif 1.0 in output and output[0] == 1.0:
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

###--------------------------------------------
###                    1_1_F
###--------------------------------------------


###------ problem solved w 7 generacji
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

###--------------------------------------------
###                    1_2_A
###--------------------------------------------

def fitness_1_2_A(individual: Program):
    output = individual.output_data
    input_data = individual.input_data
    expected = input_data[0] + input_data[1]

    fitness = -100
    input = individual.input
#     if len(input) < 2:
#         print("input too short")
#         fitness = -100
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
    fitness += abs(len(input) - 2) * -30

    return fitness

def fitness_1_2_A_C(individual: Program):
    output = individual.output_data
    input_data = individual.input_data
    expected = input_data[0] + input_data[1]

    fitness = -100
    input = individual.input
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
    fitness += abs(len(output) - 1) * -30
    fitness += abs(len(input) - 2) * -20

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
        fitness = -100.0
    elif len(output) == 1:
        if output[0] == expected:
            fitness = 0.0
        else:
            fitness = (-1) * np.abs(expected - output[0])
    else:
        avg = np.average(output)
        fitness = (-1) * np.abs(avg - expected)
    fitness += abs(len(output) - 1) * -10
    fitness += abs(len(input) - 2) * -10

    return fitness


def fitness_1_2_E(individual: Program):
    output = individual.output_data
    input_data = individual.input_data
    expected = input_data[0] * input_data[1]

    input = individual.input
    if len(input) < 2:
        fitness = -100
    elif len(output) == 0:
        fitness = -100.0
    elif len(output) == 1:
        if output[0] == expected:
            fitness = 0.0
        else:
            fitness = (-1) * np.abs(expected - output[0])
    else:
        avg = np.average(output)
        fitness = (-1) * np.abs(avg - expected)
    fitness += abs(len(output) - 1) * -10
    fitness += abs(len(input) - 2) * -10
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
    if n > len(input_data) - 1:
#         a = math.ceil(n / len(input_data))
#         input_data.repeat(input_data, a)
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


def fitness_Bool_NOT(individual: Program):
    output = individual.output_data
    input_data = np.array(individual.input)

    n = len(individual.task.test_cases[0].input_data)

    expected =[]
    for i in range(len(input_data)):
        expected.append(int(not input_data[i]))

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
    fitness += abs(len(output) - k) * -20
    fitness += abs(len(input_data) - n) * -20

    return fitness

def fitness_Bool_AND(individual: Program):
    output = individual.output_data
    input_data = np.array(individual.input)

    n = len(individual.task.test_cases[0].input_data)

    expected =[]
    expected.append(int(all(input_data)))

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
    fitness += abs(len(input_data) - n) * -10

    return fitness

def fitness_Bool_OR(individual: Program):
    output = individual.output_data
    input_data = np.array(individual.input)

    n = len(individual.task.test_cases[0].input_data)

    expected =[]
    expected.append(int(any(input_data)))

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
    fitness += abs(len(input_data) - n) * -10

    return fitness

def fitness_Bool_XOR(individual: Program):
    output = individual.output_data
    input_data = np.array(individual.input)

    n = len(individual.task.test_cases[0].input_data)

    expected =[]
    expected.append(int(sum(input_data) % 2))
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
    fitness += abs(len(input_data) - n) * -10

    return fitness


def fitness_1_Bench(individual: Program):
    output = individual.output_data
    input_data = individual.input_data
    expected = input_data[0] + input_data[1]

    fitness = -100
    input = individual.input

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
    input = individual.input
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
    fitness += abs(len(input) - 1) * -20

    return fitness

def fitness_27_Bench(individual: Program):
    output = individual.output_data
    input_data = individual.input_data
    input = individual.input
    expected = 0
    if len(input_data) % 2 == 0:
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
    fitness += abs(len(input) - 3) * -20

    return fitness


