from library.Solver.Interpreter import Interpreter

interpreter = Interpreter()
#
program = \
         ("{ "
          " x_2 = 0.0               \
            while (x_2 >= 0.0) {    \
            x_2 = x_2 + 1.0         \
            output(x_2)             \
            }"
          "}")

# error, so program stops running after 4 assignment
# program = \
#         ("{ "
#             "x_0 = input() \
#             x_0 = input() \
#             output(9.0)\
#             x_2 = (  x_1 != ( ( x_0 * x_0 ) - ( x_0 * x_0 ) )  ) \
#             output(x_0)\
#             x_0 = (  ( x_2 + x_2 ) != ( x_1 * x_0 )  ) \
#         }")

_input = [3.0, 5.0]


def print_result(program_str, program_input):
    output, actual_input, _vars = interpreter.interpret_string(program_str, program_input)
    print(f"------ Output: ----- \n {output}")
    print(f"\n------ Input: ----- \n {program_input}")
    print(f"\n------ Actual input: ----- \n {actual_input}")
    print(f"\n------ Vars: ----- \n {_vars}")


print_result(program, _input)


