# Generated from C:/Users/karol/PycharmProjects/TIny-pycharm/Grammar\TinyGP.g4 by ANTLR 4.12.0
from antlr4 import *
import pandas as pd
if __name__ is not None and "." in __name__:
    from Grammar.gen.TinyGPParser import TinyGPParser
else:
    from TinyGPParser import TinyGPParser


# This class defines a complete generic visitor for a parse tree produced by TinyGPParser.

class TinyGPVisitor(ParseTreeVisitor):

    def __init__(self, variables:dict, input:list):
        self.variables = variables
        self.input = input
        self.actual_input = None
        self.output = []
        self.limit = 100
        self.instruction_counter = 0

    # Visit a parse tree produced by TinyGPParser#program.
    def visitProgram(self, ctx:TinyGPParser.ProgramContext):
        # print("PROGRAM")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyGPParser#statement.
    def visitStatement(self, ctx:TinyGPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyGPParser#loopStatement.
    def visitLoopStatement(self, ctx:TinyGPParser.LoopStatementContext):
        # print("LOOP")
        condition = self.visitCondition(ctx.getChild(1))
        while condition == True:
            self.visitCompoundStatement(ctx.getChild(2))
            condition = self.visitCondition(ctx.getChild(1))

    # Visit a parse tree produced by TinyGPParser#conditionalStatement.
    def visitConditionalStatement(self, ctx:TinyGPParser.ConditionalStatementContext):
        # print("Conditionalstatement")
        condition = self.visitCondition(ctx.getChild(1))
        if condition == True:
            return self.visitCompoundStatement(ctx.getChild(2))
        if condition == False and ctx.getChildCount() == 5:
            return self.visitCompoundStatement(ctx.getChild(4))


    # Visit a parse tree produced by TinyGPParser#compoundStatement.
    def visitCompoundStatement(self, ctx:TinyGPParser.CompoundStatementContext):
        # print("Coumpandstatement")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyGPParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:TinyGPParser.AssignmentStatementContext):
        # print("ASSIGNMENT ", ctx.getText())
        if self.instruction_counter < self.limit:
            self.instruction_counter+=1
            result = self.visitChildren(ctx)
            if ctx.getChild(0).getText() in self.variables:
                self.variables.update({ctx.getChild(0).getText(): result})
        else:
            print("***********************")
            print("LIMIT INSTRUKCJI WYCZERPANY!!!!")
            print("Liczba instrukcji: ", self.instruction_counter)
            # exit(0)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyGPParser#inputStatement.
    def visitInputStatement(self, ctx:TinyGPParser.InputStatementContext): #### tutaj uzupełnić
        # print('Input')
        input_length = len(self.input)

        if self.actual_input == None:
            self.actual_input = self.input[0]
            return float(self.input[0])
        elif self.actual_input == self.input[input_length-1]:
            self.actual_input = self.input[0]
            return float(self.input[0])
        else:
            index = self.input.index(self.actual_input)
            self.actual_input = self.input[index+1]
            return float(self.input[index+1])



    # Visit a parse tree produced by TinyGPParser#outputStatement.
    def visitOutputStatement(self, ctx:TinyGPParser.OutputStatementContext):#### tutaj uzupełnić
        # print("Output")
        if self.instruction_counter < self.limit:
            self.instruction_counter+=1
            if ctx.getChild(2).getText() in self.variables:
                self.output.append(self.variables.get(ctx.getChild(2).getText()))
                print("OUTPUT:   ",self.variables.get(ctx.getChild(2).getText()))
            else:
                self.output.append(float(ctx.getChild(2).getText()))
                print("OUTPUT:   ",float(ctx.getChild(2).getText()))
        else:
            print("***********************")
            print("LIMIT INSTRUKCJI WYCZERPANY!!!!")
            print("Liczba instrukcji: ", self.instruction_counter)
            # exit(0)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyGPParser#condition.
    def visitCondition(self, ctx:TinyGPParser.ConditionContext):
        # print("CONDITION")
        children_number = ctx.getChildCount()
        result = self.visitExpressionCondition(ctx.getChild(1))
        if children_number > 1:
            logic_operator = None
            for i in range(2, children_number):
                if i % 2 == 0:
                    logic_operator = ctx.getChild(i).getText()
                if i % 2 == 1:
                    if logic_operator == "&&":
                        result = result and self.visitExpressionCondition(ctx.getChild(i))
                    if logic_operator == "||":
                        result = result or self.visitExpressionCondition(ctx.getChild(i))
        # print("WYNIK CONDITION: ", result)
        return result


    # Visit a parse tree produced by TinyGPParser#expressionCondition.
    def visitExpressionCondition(self, ctx:TinyGPParser.ExpressionConditionContext):
        # print("EXPRESSIONCONDITION")
        left = float(self.visitExpression(ctx.getChild(0)))
        right = float(self.visitExpression(ctx.getChild(2)))

        match ctx.getChild(1).getText():
            case "==":
                return left == right
            case "!=":
                return left != right
            case "<":
                return left < right
            case ">":
                return left > right
            case "<=":
                return left <= right
            case ">=":
                return left >= right
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyGPParser#expression.
    def visitExpression(self, ctx:TinyGPParser.ExpressionContext):
        # print("EXPRESSION")
        if ctx.getChild(0).getText() == "-":
            result = float(self.visitTerm(ctx.getChild(1)))
            if ctx.getChildCount() > 1:
                operator = None
                for i in range(2, ctx.getChildCount()):
                    if i % 2 == 0:
                        operator = ctx.getChild(i).getText()
                    if i % 2 == 1:
                        if operator == "+":
                            result = result + float(self.visitTerm(ctx.getChild(i)))
                        if operator == "-":
                            result = result - float(self.visitTerm(ctx.getChild(i)))
            return (-1)*result
        else:
            result = float(self.visitTerm(ctx.getChild(0)))
            if ctx.getChildCount() > 1:
                operator = None
                for i in range(1, ctx.getChildCount()):
                    if i % 2 == 1:
                        operator = ctx.getChild(i).getText()
                    if i % 2 == 0:
                        if operator == "+":
                            result= result + float(self.visitTerm(ctx.getChild(i)))
                        if operator == "-":
                            result = result - float(self.visitTerm(ctx.getChild(i)))
            # print("WYNIK EXPRESSION: ", result)
            return result
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyGPParser#term.
    def visitTerm(self, ctx:TinyGPParser.TermContext):
        # print("TERM: ", ctx.getText())
        result = float(self.visitFactor(ctx.getChild(0)))
        if ctx.getChildCount() > 1:
            operator = None
            for i in range(1, ctx.getChildCount()):
                if i % 2 == 1:
                    operator = ctx.getChild(i).getText()
                if i % 2 == 0:
                    if operator == "*":
                        result = result * float(self.visitFactor(ctx.getChild(i)))
                    if operator == "/":
                        m = float(self.visitFactor(ctx.getChild(i)))
                        if m == 0:
                            # print("DZIELENIE PRZEZ 0")
                            return 0.0
                        else:
                            result = result / float(self.visitFactor(ctx.getChild(i)))
        return result
        # return self.visitChildren(ctx)

    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    # Visit a parse tree produced by TinyGPParser#factor.
    def visitFactor(self, ctx:TinyGPParser.FactorContext):
        # print("FACTOR: ", ctx.getText())
        if ctx.getText() in self.variables:
            return float(self.variables.get(ctx.getText()))
        if self.is_float(ctx.getText()):
            return float(ctx.getText())
        if ctx.getText()=="True" or ctx.getText()=="False":
            return self.visitBoolean(ctx)
        else:
            return self.visitExpression(ctx.getChild(1))

    # Visit a parse tree produced by TinyGPParser#variable.
    def visitVariable(self, ctx:TinyGPParser.VariableContext):
        # print("VAR", ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TinyGPParser#boolean.
    def visitBoolean(self, ctx:TinyGPParser.BooleanContext):
        # print("BOOLEAN", ctx.getText())
        if ctx.getText() == "True":
            return 1.0
        if ctx.getText() == "False":
            return 0.0
        # return self.visitChildren(ctx)

del TinyGPParser