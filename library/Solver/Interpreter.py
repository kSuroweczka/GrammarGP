from library.Model.program import Program
from Grammar.gen.TinyGPVisitor import TinyGPVisitor
from Grammar.gen.TinyGPParser import TinyGPParser
from Grammar.gen.TinyGPLexer import TinyGPLexer
from antlr4 import *


class Interpreter:

    @staticmethod
    def interpret(program: Program):
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

    @staticmethod
    def interpret_string(program_string: str, program_intput: [float]):
        input = InputStream(program_string)
        lexer = TinyGPLexer(input)
        stream = CommonTokenStream(lexer)
        parser = TinyGPParser(stream)
        try:
            tree = parser.program()
        except:
            print("Error")
            return None
        visitor = TinyGPVisitor({}, program_intput)
        try:
            visitor.visit(tree)
            return visitor.output, visitor.actual_input, visitor.variables
        except:
            return visitor.output, visitor.actual_input, visitor.variables
