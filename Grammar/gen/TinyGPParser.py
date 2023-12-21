# Generated from C:/Users/karol/PycharmProjects/TIny-pycharm/Grammar\TinyGP.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,28,136,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,5,0,32,8,0,10,0,12,0,35,9,0,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,43,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        3,3,58,8,3,1,4,1,4,5,4,62,8,4,10,4,12,4,65,9,4,1,4,1,4,1,5,1,5,1,
        5,1,5,1,5,3,5,74,8,5,1,5,3,5,77,8,5,1,6,1,6,1,6,1,6,3,6,83,8,6,1,
        7,1,7,1,7,1,7,1,7,3,7,90,8,7,1,8,1,8,1,8,5,8,95,8,8,10,8,12,8,98,
        9,8,1,9,1,9,1,9,1,9,1,10,3,10,105,8,10,1,10,1,10,1,10,5,10,110,8,
        10,10,10,12,10,113,9,10,1,11,1,11,1,11,5,11,118,8,11,10,11,12,11,
        121,9,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,130,8,12,1,13,1,
        13,1,14,1,14,1,14,0,0,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        0,5,1,0,12,13,1,0,14,19,1,0,20,21,1,0,22,23,1,0,24,25,140,0,33,1,
        0,0,0,2,42,1,0,0,0,4,44,1,0,0,0,6,50,1,0,0,0,8,59,1,0,0,0,10,68,
        1,0,0,0,12,78,1,0,0,0,14,84,1,0,0,0,16,91,1,0,0,0,18,99,1,0,0,0,
        20,104,1,0,0,0,22,114,1,0,0,0,24,129,1,0,0,0,26,131,1,0,0,0,28,133,
        1,0,0,0,30,32,3,2,1,0,31,30,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,
        33,34,1,0,0,0,34,1,1,0,0,0,35,33,1,0,0,0,36,43,3,4,2,0,37,43,3,6,
        3,0,38,43,3,8,4,0,39,43,3,10,5,0,40,43,3,12,6,0,41,43,3,14,7,0,42,
        36,1,0,0,0,42,37,1,0,0,0,42,38,1,0,0,0,42,39,1,0,0,0,42,40,1,0,0,
        0,42,41,1,0,0,0,43,3,1,0,0,0,44,45,5,1,0,0,45,46,5,2,0,0,46,47,3,
        16,8,0,47,48,5,3,0,0,48,49,3,8,4,0,49,5,1,0,0,0,50,51,5,4,0,0,51,
        52,5,2,0,0,52,53,3,16,8,0,53,54,5,3,0,0,54,57,3,8,4,0,55,56,5,5,
        0,0,56,58,3,8,4,0,57,55,1,0,0,0,57,58,1,0,0,0,58,7,1,0,0,0,59,63,
        5,6,0,0,60,62,3,2,1,0,61,60,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,
        63,64,1,0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,66,67,5,7,0,0,67,9,1,0,
        0,0,68,69,3,26,13,0,69,73,5,8,0,0,70,74,3,16,8,0,71,74,3,20,10,0,
        72,74,3,12,6,0,73,70,1,0,0,0,73,71,1,0,0,0,73,72,1,0,0,0,74,76,1,
        0,0,0,75,77,5,9,0,0,76,75,1,0,0,0,76,77,1,0,0,0,77,11,1,0,0,0,78,
        79,5,10,0,0,79,80,5,2,0,0,80,82,5,3,0,0,81,83,5,9,0,0,82,81,1,0,
        0,0,82,83,1,0,0,0,83,13,1,0,0,0,84,85,5,11,0,0,85,86,5,2,0,0,86,
        87,3,26,13,0,87,89,5,3,0,0,88,90,5,9,0,0,89,88,1,0,0,0,89,90,1,0,
        0,0,90,15,1,0,0,0,91,96,3,18,9,0,92,93,7,0,0,0,93,95,3,18,9,0,94,
        92,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,17,1,0,0,
        0,98,96,1,0,0,0,99,100,3,20,10,0,100,101,7,1,0,0,101,102,3,20,10,
        0,102,19,1,0,0,0,103,105,5,20,0,0,104,103,1,0,0,0,104,105,1,0,0,
        0,105,106,1,0,0,0,106,111,3,22,11,0,107,108,7,2,0,0,108,110,3,22,
        11,0,109,107,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,111,112,1,0,
        0,0,112,21,1,0,0,0,113,111,1,0,0,0,114,119,3,24,12,0,115,116,7,3,
        0,0,116,118,3,24,12,0,117,115,1,0,0,0,118,121,1,0,0,0,119,117,1,
        0,0,0,119,120,1,0,0,0,120,23,1,0,0,0,121,119,1,0,0,0,122,123,5,2,
        0,0,123,124,3,20,10,0,124,125,5,3,0,0,125,130,1,0,0,0,126,130,3,
        26,13,0,127,130,3,28,14,0,128,130,5,27,0,0,129,122,1,0,0,0,129,126,
        1,0,0,0,129,127,1,0,0,0,129,128,1,0,0,0,130,25,1,0,0,0,131,132,5,
        26,0,0,132,27,1,0,0,0,133,134,7,4,0,0,134,29,1,0,0,0,13,33,42,57,
        63,73,76,82,89,96,104,111,119,129
    ]

class TinyGPParser ( Parser ):

    grammarFileName = "TinyGP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'while'", "'('", "')'", "'if'", "'else'", 
                     "'{'", "'}'", "'='", "';'", "'input'", "'output'", 
                     "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'-'", "'+'", "'*'", "'/'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_loopStatement = 2
    RULE_conditionalStatement = 3
    RULE_compoundStatement = 4
    RULE_assignmentStatement = 5
    RULE_inputStatement = 6
    RULE_outputStatement = 7
    RULE_condition = 8
    RULE_expressionCondition = 9
    RULE_expression = 10
    RULE_term = 11
    RULE_factor = 12
    RULE_variable = 13
    RULE_boolean = 14

    ruleNames =  [ "program", "statement", "loopStatement", "conditionalStatement", 
                   "compoundStatement", "assignmentStatement", "inputStatement", 
                   "outputStatement", "condition", "expressionCondition", 
                   "expression", "term", "factor", "variable", "boolean" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    ID=26
    NUMBER=27
    WS=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TinyGPParser.StatementContext)
            else:
                return self.getTypedRuleContext(TinyGPParser.StatementContext,i)


        def getRuleIndex(self):
            return TinyGPParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = TinyGPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67112018) != 0):
                self.state = 30
                self.statement()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loopStatement(self):
            return self.getTypedRuleContext(TinyGPParser.LoopStatementContext,0)


        def conditionalStatement(self):
            return self.getTypedRuleContext(TinyGPParser.ConditionalStatementContext,0)


        def compoundStatement(self):
            return self.getTypedRuleContext(TinyGPParser.CompoundStatementContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(TinyGPParser.AssignmentStatementContext,0)


        def inputStatement(self):
            return self.getTypedRuleContext(TinyGPParser.InputStatementContext,0)


        def outputStatement(self):
            return self.getTypedRuleContext(TinyGPParser.OutputStatementContext,0)


        def getRuleIndex(self):
            return TinyGPParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = TinyGPParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.loopStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.conditionalStatement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.compoundStatement()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 39
                self.assignmentStatement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 40
                self.inputStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 6)
                self.state = 41
                self.outputStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(TinyGPParser.ConditionContext,0)


        def compoundStatement(self):
            return self.getTypedRuleContext(TinyGPParser.CompoundStatementContext,0)


        def getRuleIndex(self):
            return TinyGPParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = TinyGPParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(TinyGPParser.T__0)
            self.state = 45
            self.match(TinyGPParser.T__1)
            self.state = 46
            self.condition()
            self.state = 47
            self.match(TinyGPParser.T__2)
            self.state = 48
            self.compoundStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(TinyGPParser.ConditionContext,0)


        def compoundStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TinyGPParser.CompoundStatementContext)
            else:
                return self.getTypedRuleContext(TinyGPParser.CompoundStatementContext,i)


        def getRuleIndex(self):
            return TinyGPParser.RULE_conditionalStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalStatement" ):
                listener.enterConditionalStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalStatement" ):
                listener.exitConditionalStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalStatement" ):
                return visitor.visitConditionalStatement(self)
            else:
                return visitor.visitChildren(self)




    def conditionalStatement(self):

        localctx = TinyGPParser.ConditionalStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_conditionalStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(TinyGPParser.T__3)
            self.state = 51
            self.match(TinyGPParser.T__1)
            self.state = 52
            self.condition()
            self.state = 53
            self.match(TinyGPParser.T__2)
            self.state = 54
            self.compoundStatement()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 55
                self.match(TinyGPParser.T__4)
                self.state = 56
                self.compoundStatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TinyGPParser.StatementContext)
            else:
                return self.getTypedRuleContext(TinyGPParser.StatementContext,i)


        def getRuleIndex(self):
            return TinyGPParser.RULE_compoundStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundStatement" ):
                listener.enterCompoundStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundStatement" ):
                listener.exitCompoundStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundStatement" ):
                return visitor.visitCompoundStatement(self)
            else:
                return visitor.visitChildren(self)




    def compoundStatement(self):

        localctx = TinyGPParser.CompoundStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(TinyGPParser.T__5)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67112018) != 0):
                self.state = 60
                self.statement()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(TinyGPParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(TinyGPParser.VariableContext,0)


        def condition(self):
            return self.getTypedRuleContext(TinyGPParser.ConditionContext,0)


        def expression(self):
            return self.getTypedRuleContext(TinyGPParser.ExpressionContext,0)


        def inputStatement(self):
            return self.getTypedRuleContext(TinyGPParser.InputStatementContext,0)


        def getRuleIndex(self):
            return TinyGPParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = TinyGPParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignmentStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.variable()
            self.state = 69
            self.match(TinyGPParser.T__7)
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 70
                self.condition()
                pass

            elif la_ == 2:
                self.state = 71
                self.expression()
                pass

            elif la_ == 3:
                self.state = 72
                self.inputStatement()
                pass


            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 75
                self.match(TinyGPParser.T__8)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TinyGPParser.RULE_inputStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputStatement" ):
                listener.enterInputStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputStatement" ):
                listener.exitInputStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputStatement" ):
                return visitor.visitInputStatement(self)
            else:
                return visitor.visitChildren(self)




    def inputStatement(self):

        localctx = TinyGPParser.InputStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_inputStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(TinyGPParser.T__9)
            self.state = 79
            self.match(TinyGPParser.T__1)
            self.state = 80
            self.match(TinyGPParser.T__2)
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 81
                self.match(TinyGPParser.T__8)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(TinyGPParser.VariableContext,0)


        def getRuleIndex(self):
            return TinyGPParser.RULE_outputStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutputStatement" ):
                listener.enterOutputStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutputStatement" ):
                listener.exitOutputStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputStatement" ):
                return visitor.visitOutputStatement(self)
            else:
                return visitor.visitChildren(self)




    def outputStatement(self):

        localctx = TinyGPParser.OutputStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_outputStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(TinyGPParser.T__10)
            self.state = 85
            self.match(TinyGPParser.T__1)
            self.state = 86
            self.variable()
            self.state = 87
            self.match(TinyGPParser.T__2)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 88
                self.match(TinyGPParser.T__8)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionCondition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TinyGPParser.ExpressionConditionContext)
            else:
                return self.getTypedRuleContext(TinyGPParser.ExpressionConditionContext,i)


        def getRuleIndex(self):
            return TinyGPParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = TinyGPParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.expressionCondition()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12 or _la==13:
                self.state = 92
                _la = self._input.LA(1)
                if not(_la==12 or _la==13):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()

                self.state = 93
                self.expressionCondition()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TinyGPParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(TinyGPParser.ExpressionContext,i)


        def getRuleIndex(self):
            return TinyGPParser.RULE_expressionCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionCondition" ):
                listener.enterExpressionCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionCondition" ):
                listener.exitExpressionCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionCondition" ):
                return visitor.visitExpressionCondition(self)
            else:
                return visitor.visitChildren(self)




    def expressionCondition(self):

        localctx = TinyGPParser.ExpressionConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expressionCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.expression()
            self.state = 100
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1032192) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 101
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TinyGPParser.TermContext)
            else:
                return self.getTypedRuleContext(TinyGPParser.TermContext,i)


        def getRuleIndex(self):
            return TinyGPParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = TinyGPParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 103
                self.match(TinyGPParser.T__19)


            self.state = 106
            self.term()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20 or _la==21:
                self.state = 107
                _la = self._input.LA(1)
                if not(_la==20 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 108
                self.term()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TinyGPParser.FactorContext)
            else:
                return self.getTypedRuleContext(TinyGPParser.FactorContext,i)


        def getRuleIndex(self):
            return TinyGPParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = TinyGPParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.factor()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==23:
                self.state = 115
                _la = self._input.LA(1)
                if not(_la==22 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 116
                self.factor()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(TinyGPParser.ExpressionContext,0)


        def variable(self):
            return self.getTypedRuleContext(TinyGPParser.VariableContext,0)


        def boolean(self):
            return self.getTypedRuleContext(TinyGPParser.BooleanContext,0)


        def NUMBER(self):
            return self.getToken(TinyGPParser.NUMBER, 0)

        def getRuleIndex(self):
            return TinyGPParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = TinyGPParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_factor)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.match(TinyGPParser.T__1)
                self.state = 123
                self.expression()
                self.state = 124
                self.match(TinyGPParser.T__2)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.variable()
                pass
            elif token in [24, 25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.boolean()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 4)
                self.state = 128
                self.match(TinyGPParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TinyGPParser.ID, 0)

        def getRuleIndex(self):
            return TinyGPParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = TinyGPParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(TinyGPParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TinyGPParser.RULE_boolean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)




    def boolean(self):

        localctx = TinyGPParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





