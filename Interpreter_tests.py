from library.Solver.Interpreter import Interpreter

interpreter = Interpreter()

program = \
        "x_0 = input()      \
         x_1 = input()      \
         x_2 = x_0 + x_1    \
         while (x_2 > 0.0) {  \
            x_2 = x_2 + 1.0   \
            output(x_2)     \
         }"


_input = [3.0, 7.0]


def print_result(program_str, program_input):
    output, actual_input, _vars = interpreter.interpret_string(program_str, program_input)
    print(f"------ Output: ----- \n {output}")
    print(f"\n------ Actual input: ----- \n {actual_input}")
    print(f"\n------ Vars: ----- \n {_vars}")


print_result(program, _input)


