import json
import os
import itertools

def negation(x):
    negation_list =[]
    for input in x:
        list_inside = []
        for i in range(len(input)):
            list_inside.append(int(not input[i]))
        negation_list.append(list_inside)
    return negation_list

def and_function(x):
    and_list = []
    for input in x:
        list_inside = []
        list_inside.append(int(all(input)))
        and_list.append(list_inside)
    return and_list

def or_function(x):
    or_list = []
    for input in x:
        list_inside = []
        list_inside.append(int(any(input)))
        or_list.append(list_inside)
    return or_list

def xor_function(x):
    xor_list = []
    for input in x:
        list_inside = []
        list_inside.append(int(sum(input) % 2))
        xor_list.append(list_inside)
    return xor_list

def generate_dicts(k, input, output, fun):
    data = {}
    data["name"] = f'Bool_{k}_{fun}'
    data["min_input_length"] = k
    data["max_input_length"] = k
    data["min_output_length"] = 1
    data["max_output_length"] = 1
    data["test_cases"] = []

    for i in range(len(input)):
        dict={}
        dict["input"]=input[i]
        dict["output"]=output[i]
        data["test_cases"].append(dict)
    return data

def save_data(data, k, fun):
    dir = os.path.dirname(f'./library/Tasks/tasks_data/Bool_{k}_{fun}/')
    if not os.path.exists(dir):
        os.mkdir(dir)
    with open(f'./library/Tasks/tasks_data/Bool_{k}_{fun}/data.json', 'w') as f:
        json.dump(data, f, indent=4)

def generate_bool_data(k):
    # inputs
    binary_combinations = []
    binary_combinations = list(itertools.product([0, 1], repeat=k))

    # outputs
    negation_list = negation(binary_combinations)
    and_list = and_function(binary_combinations)
    or_list = or_function(binary_combinations)
    xor_list = xor_function(binary_combinations)

    # generating data
    data_negation = generate_dicts(k, binary_combinations, negation_list, 1)
    data_and= generate_dicts(k, binary_combinations, and_list, 2)
    data_or= generate_dicts(k, binary_combinations, or_list, 3)
    data_xor= generate_dicts(k, binary_combinations, xor_list, 4)

    # saving data
    save_data(data_negation, k, 1)
    save_data(data_and, k, 2)
    save_data(data_or, k, 3)
    save_data(data_xor, k, 4)

for k in range(1, 11):
    generate_bool_data(k)