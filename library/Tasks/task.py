import os
import json

class Task:
    def __init__(self, name):
        self.name = name
        self.data = self.read_data(name)

    def read_data(self, name: str) -> dict:
        test_cases = []

        task_data_path = os.path.join(os.getcwd(),'library/Tasks/tasks_data', name)
        for file in os.listdir(task_data_path):
            if file.endswith('.json'):
                file_path = os.path.join(task_data_path, file)
                with open(file_path, 'r') as f:
                    data = json.load(f)

                for test_case in data['test_cases']:
                    test_cases.append(self.read_test_case(test_case))

                self.min_input_length = data['min_input_length']
                self.max_input_length = data['max_input_length']
                self.min_output_length = data['min_output_length']
                self.max_output_length = data['max_output_length']
                self.test_cases = test_cases

        return data

    def read_test_case(self, case: dict):
        input_data = case['input']
        output_data = case['output']
        return TestCase(input_data, output_data)

class TestCase:
    def __init__(self, input_data, output_data):
        self.input_data = input_data
        self.output_data = output_data

    def __repr__(self):
        return f"TestCase(input={self.input_data}, output={self.output_data})"