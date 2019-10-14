# Generated from /home/araara/Documents/tl69_assembler/tl69asm.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3(")
        buf.write("_\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\3\2\5\2 \n\2\3\2\6\2#\n\2\r\2\16\2$\3\2")
        buf.write("\3\2\3\3\5\3*\n\3\3\3\3\3\5\3.\n\3\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\5\5\66\n\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\7\tF\n\t\f\t\16\tI\13\t\5\tK\n\t\3")
        buf.write("\n\3\n\3\n\3\13\3\13\5\13R\n\13\3\f\3\f\3\f\5\fW\n\f\3")
        buf.write("\r\3\r\3\16\3\16\3\17\3\17\3\17\2\2\20\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\2\3\3\2\3\6\2[\2\"\3\2\2\2\4)\3")
        buf.write("\2\2\2\6/\3\2\2\2\b\65\3\2\2\2\n\67\3\2\2\2\f:\3\2\2\2")
        buf.write("\16=\3\2\2\2\20J\3\2\2\2\22L\3\2\2\2\24Q\3\2\2\2\26V\3")
        buf.write("\2\2\2\30X\3\2\2\2\32Z\3\2\2\2\34\\\3\2\2\2\36 \5\4\3")
        buf.write("\2\37\36\3\2\2\2\37 \3\2\2\2 !\3\2\2\2!#\7\b\2\2\"\37")
        buf.write("\3\2\2\2#$\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%&\3\2\2\2&\'\7")
        buf.write("\2\2\3\'\3\3\2\2\2(*\5\6\4\2)(\3\2\2\2)*\3\2\2\2*-\3\2")
        buf.write("\2\2+.\5\b\5\2,.\5\22\n\2-+\3\2\2\2-,\3\2\2\2.\5\3\2\2")
        buf.write("\2/\60\7%\2\2\60\61\7\t\2\2\61\7\3\2\2\2\62\66\5\n\6\2")
        buf.write("\63\66\5\f\7\2\64\66\5\16\b\2\65\62\3\2\2\2\65\63\3\2")
        buf.write("\2\2\65\64\3\2\2\2\66\t\3\2\2\2\678\7\20\2\289\5\24\13")
        buf.write("\29\13\3\2\2\2:;\7\21\2\2;<\5\24\13\2<\r\3\2\2\2=>\5\6")
        buf.write("\4\2>?\7\17\2\2?@\5\24\13\2@\17\3\2\2\2AK\3\2\2\2BG\5")
        buf.write("\26\f\2CD\7\f\2\2DF\5\26\f\2EC\3\2\2\2FI\3\2\2\2GE\3\2")
        buf.write("\2\2GH\3\2\2\2HK\3\2\2\2IG\3\2\2\2JA\3\2\2\2JB\3\2\2\2")
        buf.write("K\21\3\2\2\2LM\7\23\2\2MN\5\20\t\2N\23\3\2\2\2OR\5\34")
        buf.write("\17\2PR\5\30\r\2QO\3\2\2\2QP\3\2\2\2R\25\3\2\2\2SW\5\34")
        buf.write("\17\2TW\5\32\16\2UW\5\30\r\2VS\3\2\2\2VT\3\2\2\2VU\3\2")
        buf.write("\2\2W\27\3\2\2\2XY\7%\2\2Y\31\3\2\2\2Z[\7\22\2\2[\33\3")
        buf.write("\2\2\2\\]\t\2\2\2]\35\3\2\2\2\13\37$)-\65GJQV")
        return buf.getvalue()


class tl69asmParser ( Parser ):

    grammarFileName = "tl69asm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "':'", "'('", 
                     "')'", "','", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "INT_HEX", "INT_BIN", "INT_OCT", "INT_DEC", 
                      "White_Space", "EOL", "COLON", "LPARN", "RPARN", "COMMA", 
                      "ADD", "SUB", "DIR_EQU", "DIR_DW", "DIR_ORG", "Register", 
                      "OpCode", "OpADDI", "OpADD", "OpSUBI", "OpSUB", "OpMULI", 
                      "OpMUL", "OpXCHG", "OpCMPI", "OpCMP", "OpORI", "OpOR", 
                      "OpXORI", "OpXOR", "OpANDI", "OpAND", "OpNOT", "OpHALT", 
                      "ID", "COMMENT", "DOUBLE_SLASH_COMMENT", "WHITESPACE" ]

    RULE_tl69asmProg = 0
    RULE_tl69asmLine = 1
    RULE_label = 2
    RULE_directive = 3
    RULE_directiveDW = 4
    RULE_directiveORG = 5
    RULE_directiveEQU = 6
    RULE_operands = 7
    RULE_instruction = 8
    RULE_expr = 9
    RULE_operand = 10
    RULE_labelRef = 11
    RULE_register = 12
    RULE_integer = 13

    ruleNames =  [ "tl69asmProg", "tl69asmLine", "label", "directive", "directiveDW", 
                   "directiveORG", "directiveEQU", "operands", "instruction", 
                   "expr", "operand", "labelRef", "register", "integer" ]

    EOF = Token.EOF
    INT_HEX=1
    INT_BIN=2
    INT_OCT=3
    INT_DEC=4
    White_Space=5
    EOL=6
    COLON=7
    LPARN=8
    RPARN=9
    COMMA=10
    ADD=11
    SUB=12
    DIR_EQU=13
    DIR_DW=14
    DIR_ORG=15
    Register=16
    OpCode=17
    OpADDI=18
    OpADD=19
    OpSUBI=20
    OpSUB=21
    OpMULI=22
    OpMUL=23
    OpXCHG=24
    OpCMPI=25
    OpCMP=26
    OpORI=27
    OpOR=28
    OpXORI=29
    OpXOR=30
    OpANDI=31
    OpAND=32
    OpNOT=33
    OpHALT=34
    ID=35
    COMMENT=36
    DOUBLE_SLASH_COMMENT=37
    WHITESPACE=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Tl69asmProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(tl69asmParser.EOF, 0)

        def EOL(self, i:int=None):
            if i is None:
                return self.getTokens(tl69asmParser.EOL)
            else:
                return self.getToken(tl69asmParser.EOL, i)

        def tl69asmLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tl69asmParser.Tl69asmLineContext)
            else:
                return self.getTypedRuleContext(tl69asmParser.Tl69asmLineContext,i)


        def getRuleIndex(self):
            return tl69asmParser.RULE_tl69asmProg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTl69asmProg" ):
                listener.enterTl69asmProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTl69asmProg" ):
                listener.exitTl69asmProg(self)




    def tl69asmProg(self):

        localctx = tl69asmParser.Tl69asmProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_tl69asmProg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << tl69asmParser.DIR_DW) | (1 << tl69asmParser.DIR_ORG) | (1 << tl69asmParser.OpCode) | (1 << tl69asmParser.ID))) != 0):
                    self.state = 28
                    self.tl69asmLine()


                self.state = 31
                self.match(tl69asmParser.EOL)
                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << tl69asmParser.EOL) | (1 << tl69asmParser.DIR_DW) | (1 << tl69asmParser.DIR_ORG) | (1 << tl69asmParser.OpCode) | (1 << tl69asmParser.ID))) != 0)):
                    break

            self.state = 36
            self.match(tl69asmParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tl69asmLineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def directive(self):
            return self.getTypedRuleContext(tl69asmParser.DirectiveContext,0)


        def instruction(self):
            return self.getTypedRuleContext(tl69asmParser.InstructionContext,0)


        def label(self):
            return self.getTypedRuleContext(tl69asmParser.LabelContext,0)


        def getRuleIndex(self):
            return tl69asmParser.RULE_tl69asmLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTl69asmLine" ):
                listener.enterTl69asmLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTl69asmLine" ):
                listener.exitTl69asmLine(self)




    def tl69asmLine(self):

        localctx = tl69asmParser.Tl69asmLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tl69asmLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 38
                self.label()


            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [tl69asmParser.DIR_DW, tl69asmParser.DIR_ORG, tl69asmParser.ID]:
                self.state = 41
                self.directive()
                pass
            elif token in [tl69asmParser.OpCode]:
                self.state = 42
                self.instruction()
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


    class LabelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(tl69asmParser.ID, 0)

        def COLON(self):
            return self.getToken(tl69asmParser.COLON, 0)

        def getRuleIndex(self):
            return tl69asmParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)




    def label(self):

        localctx = tl69asmParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(tl69asmParser.ID)
            self.state = 46
            self.match(tl69asmParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def directiveDW(self):
            return self.getTypedRuleContext(tl69asmParser.DirectiveDWContext,0)


        def directiveORG(self):
            return self.getTypedRuleContext(tl69asmParser.DirectiveORGContext,0)


        def directiveEQU(self):
            return self.getTypedRuleContext(tl69asmParser.DirectiveEQUContext,0)


        def getRuleIndex(self):
            return tl69asmParser.RULE_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirective" ):
                listener.enterDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirective" ):
                listener.exitDirective(self)




    def directive(self):

        localctx = tl69asmParser.DirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [tl69asmParser.DIR_DW]:
                self.state = 48
                self.directiveDW()
                pass
            elif token in [tl69asmParser.DIR_ORG]:
                self.state = 49
                self.directiveORG()
                pass
            elif token in [tl69asmParser.ID]:
                self.state = 50
                self.directiveEQU()
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


    class DirectiveDWContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIR_DW(self):
            return self.getToken(tl69asmParser.DIR_DW, 0)

        def expr(self):
            return self.getTypedRuleContext(tl69asmParser.ExprContext,0)


        def getRuleIndex(self):
            return tl69asmParser.RULE_directiveDW

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirectiveDW" ):
                listener.enterDirectiveDW(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirectiveDW" ):
                listener.exitDirectiveDW(self)




    def directiveDW(self):

        localctx = tl69asmParser.DirectiveDWContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_directiveDW)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(tl69asmParser.DIR_DW)
            self.state = 54
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectiveORGContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIR_ORG(self):
            return self.getToken(tl69asmParser.DIR_ORG, 0)

        def expr(self):
            return self.getTypedRuleContext(tl69asmParser.ExprContext,0)


        def getRuleIndex(self):
            return tl69asmParser.RULE_directiveORG

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirectiveORG" ):
                listener.enterDirectiveORG(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirectiveORG" ):
                listener.exitDirectiveORG(self)




    def directiveORG(self):

        localctx = tl69asmParser.DirectiveORGContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_directiveORG)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(tl69asmParser.DIR_ORG)
            self.state = 57
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectiveEQUContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label(self):
            return self.getTypedRuleContext(tl69asmParser.LabelContext,0)


        def DIR_EQU(self):
            return self.getToken(tl69asmParser.DIR_EQU, 0)

        def expr(self):
            return self.getTypedRuleContext(tl69asmParser.ExprContext,0)


        def getRuleIndex(self):
            return tl69asmParser.RULE_directiveEQU

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirectiveEQU" ):
                listener.enterDirectiveEQU(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirectiveEQU" ):
                listener.exitDirectiveEQU(self)




    def directiveEQU(self):

        localctx = tl69asmParser.DirectiveEQUContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_directiveEQU)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.label()
            self.state = 60
            self.match(tl69asmParser.DIR_EQU)
            self.state = 61
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tl69asmParser.OperandContext)
            else:
                return self.getTypedRuleContext(tl69asmParser.OperandContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(tl69asmParser.COMMA)
            else:
                return self.getToken(tl69asmParser.COMMA, i)

        def getRuleIndex(self):
            return tl69asmParser.RULE_operands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperands" ):
                listener.enterOperands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperands" ):
                listener.exitOperands(self)




    def operands(self):

        localctx = tl69asmParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operands)
        self._la = 0 # Token type
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [tl69asmParser.EOL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [tl69asmParser.INT_HEX, tl69asmParser.INT_BIN, tl69asmParser.INT_OCT, tl69asmParser.INT_DEC, tl69asmParser.Register, tl69asmParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.operand()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==tl69asmParser.COMMA:
                    self.state = 65
                    self.match(tl69asmParser.COMMA)
                    self.state = 66
                    self.operand()
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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


    class InstructionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpCode(self):
            return self.getToken(tl69asmParser.OpCode, 0)

        def operands(self):
            return self.getTypedRuleContext(tl69asmParser.OperandsContext,0)


        def getRuleIndex(self):
            return tl69asmParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)




    def instruction(self):

        localctx = tl69asmParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_instruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(tl69asmParser.OpCode)
            self.state = 75
            self.operands()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer(self):
            return self.getTypedRuleContext(tl69asmParser.IntegerContext,0)


        def labelRef(self):
            return self.getTypedRuleContext(tl69asmParser.LabelRefContext,0)


        def getRuleIndex(self):
            return tl69asmParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = tl69asmParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [tl69asmParser.INT_HEX, tl69asmParser.INT_BIN, tl69asmParser.INT_OCT, tl69asmParser.INT_DEC]:
                self.state = 77
                self.integer()
                pass
            elif token in [tl69asmParser.ID]:
                self.state = 78
                self.labelRef()
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


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer(self):
            return self.getTypedRuleContext(tl69asmParser.IntegerContext,0)


        def register(self):
            return self.getTypedRuleContext(tl69asmParser.RegisterContext,0)


        def labelRef(self):
            return self.getTypedRuleContext(tl69asmParser.LabelRefContext,0)


        def getRuleIndex(self):
            return tl69asmParser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)




    def operand(self):

        localctx = tl69asmParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [tl69asmParser.INT_HEX, tl69asmParser.INT_BIN, tl69asmParser.INT_OCT, tl69asmParser.INT_DEC]:
                self.state = 81
                self.integer()
                pass
            elif token in [tl69asmParser.Register]:
                self.state = 82
                self.register()
                pass
            elif token in [tl69asmParser.ID]:
                self.state = 83
                self.labelRef()
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


    class LabelRefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(tl69asmParser.ID, 0)

        def getRuleIndex(self):
            return tl69asmParser.RULE_labelRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelRef" ):
                listener.enterLabelRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelRef" ):
                listener.exitLabelRef(self)




    def labelRef(self):

        localctx = tl69asmParser.LabelRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_labelRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(tl69asmParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegisterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Register(self):
            return self.getToken(tl69asmParser.Register, 0)

        def getRuleIndex(self):
            return tl69asmParser.RULE_register

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegister" ):
                listener.enterRegister(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegister" ):
                listener.exitRegister(self)




    def register(self):

        localctx = tl69asmParser.RegisterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_register)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(tl69asmParser.Register)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_HEX(self):
            return self.getToken(tl69asmParser.INT_HEX, 0)

        def INT_DEC(self):
            return self.getToken(tl69asmParser.INT_DEC, 0)

        def INT_BIN(self):
            return self.getToken(tl69asmParser.INT_BIN, 0)

        def INT_OCT(self):
            return self.getToken(tl69asmParser.INT_OCT, 0)

        def getRuleIndex(self):
            return tl69asmParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)




    def integer(self):

        localctx = tl69asmParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << tl69asmParser.INT_HEX) | (1 << tl69asmParser.INT_BIN) | (1 << tl69asmParser.INT_OCT) | (1 << tl69asmParser.INT_DEC))) != 0)):
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





