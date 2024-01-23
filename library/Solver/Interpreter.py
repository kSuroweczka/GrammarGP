from library.Model.program import Program
from Grammar.gen.TinyGPVisitor import TinyGPVisitor
from Grammar.gen.TinyGPParser import TinyGPParser
from Grammar.gen.TinyGPLexer import TinyGPLexer
from antlr4 import *


class Interpreter:

    @staticmethod
    def interpret(program: Program = None):
        input = InputStream(program.get_program_string())
        lexer = TinyGPLexer(input)

        stream = CommonTokenStream(lexer)
        parser = TinyGPParser(stream)
        try:
            tree = parser.program()
        except:
            print("Error")
            return None

        visitor = TinyGPVisitor({}, program.input_data)
        try:
            visitor.visit(tree)
            return visitor.output, visitor.actual_input , visitor.variables
        except:
            return visitor.output, visitor.actual_input, visitor.variables

#         example = " x1 = input() output(x1) x1 = input() output(x1) x1 = input() output(x1)"
# #         example = " {x1=input() output(x1) while(x1 >0.0 ){ output(x1) x1=x1+1.0 }}"
#         input_data = [2.0, 11.0]
#         input = InputStream(example)
#         lexer = TinyGPLexer(input)
#
#         stream = CommonTokenStream(lexer)
#         parser = TinyGPParser(stream)
#         try:
#             tree = parser.program()
#         except:
#             print("Error")
#             return None
#
#         visitor = TinyGPVisitor({}, input_data)
#         try:
#             visitor.visit(tree)
#             print("OUTPUT: ", visitor.output)
#             print("INPUT: ", input_data)
#             print("VARIABLES: ", visitor.variables)
#             return visitor.output, visitor.actual_input , visitor.variables
#         except:
#             return visitor.output, visitor.actual_input, visitor.variables
