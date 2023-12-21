# Generated from C:/Users/karol/PycharmProjects/TIny-pycharm/Grammar\TinyGP.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TinyGPParser import TinyGPParser
else:
    from TinyGPParser import TinyGPParser

# This class defines a complete listener for a parse tree produced by TinyGPParser.
class TinyGPListener(ParseTreeListener):

    # Enter a parse tree produced by TinyGPParser#program.
    def enterProgram(self, ctx:TinyGPParser.ProgramContext):
        pass

    # Exit a parse tree produced by TinyGPParser#program.
    def exitProgram(self, ctx:TinyGPParser.ProgramContext):
        pass


    # Enter a parse tree produced by TinyGPParser#statement.
    def enterStatement(self, ctx:TinyGPParser.StatementContext):
        pass

    # Exit a parse tree produced by TinyGPParser#statement.
    def exitStatement(self, ctx:TinyGPParser.StatementContext):
        pass


    # Enter a parse tree produced by TinyGPParser#loopStatement.
    def enterLoopStatement(self, ctx:TinyGPParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by TinyGPParser#loopStatement.
    def exitLoopStatement(self, ctx:TinyGPParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by TinyGPParser#conditionalStatement.
    def enterConditionalStatement(self, ctx:TinyGPParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by TinyGPParser#conditionalStatement.
    def exitConditionalStatement(self, ctx:TinyGPParser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by TinyGPParser#compoundStatement.
    def enterCompoundStatement(self, ctx:TinyGPParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by TinyGPParser#compoundStatement.
    def exitCompoundStatement(self, ctx:TinyGPParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by TinyGPParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:TinyGPParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by TinyGPParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:TinyGPParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by TinyGPParser#inputStatement.
    def enterInputStatement(self, ctx:TinyGPParser.InputStatementContext):
        pass

    # Exit a parse tree produced by TinyGPParser#inputStatement.
    def exitInputStatement(self, ctx:TinyGPParser.InputStatementContext):
        pass


    # Enter a parse tree produced by TinyGPParser#outputStatement.
    def enterOutputStatement(self, ctx:TinyGPParser.OutputStatementContext):
        pass

    # Exit a parse tree produced by TinyGPParser#outputStatement.
    def exitOutputStatement(self, ctx:TinyGPParser.OutputStatementContext):
        pass


    # Enter a parse tree produced by TinyGPParser#condition.
    def enterCondition(self, ctx:TinyGPParser.ConditionContext):
        pass

    # Exit a parse tree produced by TinyGPParser#condition.
    def exitCondition(self, ctx:TinyGPParser.ConditionContext):
        pass


    # Enter a parse tree produced by TinyGPParser#expressionCondition.
    def enterExpressionCondition(self, ctx:TinyGPParser.ExpressionConditionContext):
        pass

    # Exit a parse tree produced by TinyGPParser#expressionCondition.
    def exitExpressionCondition(self, ctx:TinyGPParser.ExpressionConditionContext):
        pass


    # Enter a parse tree produced by TinyGPParser#expression.
    def enterExpression(self, ctx:TinyGPParser.ExpressionContext):
        pass

    # Exit a parse tree produced by TinyGPParser#expression.
    def exitExpression(self, ctx:TinyGPParser.ExpressionContext):
        pass


    # Enter a parse tree produced by TinyGPParser#term.
    def enterTerm(self, ctx:TinyGPParser.TermContext):
        pass

    # Exit a parse tree produced by TinyGPParser#term.
    def exitTerm(self, ctx:TinyGPParser.TermContext):
        pass


    # Enter a parse tree produced by TinyGPParser#factor.
    def enterFactor(self, ctx:TinyGPParser.FactorContext):
        pass

    # Exit a parse tree produced by TinyGPParser#factor.
    def exitFactor(self, ctx:TinyGPParser.FactorContext):
        pass


    # Enter a parse tree produced by TinyGPParser#variable.
    def enterVariable(self, ctx:TinyGPParser.VariableContext):
        pass

    # Exit a parse tree produced by TinyGPParser#variable.
    def exitVariable(self, ctx:TinyGPParser.VariableContext):
        pass


    # Enter a parse tree produced by TinyGPParser#boolean.
    def enterBoolean(self, ctx:TinyGPParser.BooleanContext):
        pass

    # Exit a parse tree produced by TinyGPParser#boolean.
    def exitBoolean(self, ctx:TinyGPParser.BooleanContext):
        pass



del TinyGPParser