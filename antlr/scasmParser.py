# Generated from /home/araara/Documents/scomp_as/scasm.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3M")
        buf.write("j\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\7\2$\n\2\f\2\16\2")
        buf.write("\'\13\2\3\2\3\2\5\2+\n\2\3\2\3\2\3\3\5\3\60\n\3\3\3\3")
        buf.write("\3\5\3\64\n\3\3\3\5\3\67\n\3\3\4\3\4\3\4\3\5\3\5\3\5\5")
        buf.write("\5?\n\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\7\tO\n\t\f\t\16\tR\13\t\5\tT\n\t\3\n\3\n\3")
        buf.write("\n\3\13\3\13\5\13[\n\13\3\f\3\f\3\f\5\f`\n\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\20\3\20\3\20\2\2\21\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36\2\3\3\2\3\6\2g\2%\3\2\2\2\4/")
        buf.write("\3\2\2\2\68\3\2\2\2\b>\3\2\2\2\n@\3\2\2\2\fC\3\2\2\2\16")
        buf.write("F\3\2\2\2\20S\3\2\2\2\22U\3\2\2\2\24Z\3\2\2\2\26_\3\2")
        buf.write("\2\2\30a\3\2\2\2\32c\3\2\2\2\34e\3\2\2\2\36g\3\2\2\2 ")
        buf.write("!\5\4\3\2!\"\7\b\2\2\"$\3\2\2\2# \3\2\2\2$\'\3\2\2\2%")
        buf.write("#\3\2\2\2%&\3\2\2\2&(\3\2\2\2\'%\3\2\2\2(*\5\4\3\2)+\7")
        buf.write("\b\2\2*)\3\2\2\2*+\3\2\2\2+,\3\2\2\2,-\7\2\2\3-\3\3\2")
        buf.write("\2\2.\60\5\6\4\2/.\3\2\2\2/\60\3\2\2\2\60\63\3\2\2\2\61")
        buf.write("\64\5\b\5\2\62\64\5\22\n\2\63\61\3\2\2\2\63\62\3\2\2\2")
        buf.write("\63\64\3\2\2\2\64\66\3\2\2\2\65\67\5\36\20\2\66\65\3\2")
        buf.write("\2\2\66\67\3\2\2\2\67\5\3\2\2\289\7J\2\29:\7\t\2\2:\7")
        buf.write("\3\2\2\2;?\5\n\6\2<?\5\f\7\2=?\5\16\b\2>;\3\2\2\2><\3")
        buf.write("\2\2\2>=\3\2\2\2?\t\3\2\2\2@A\7\20\2\2AB\5\24\13\2B\13")
        buf.write("\3\2\2\2CD\7\21\2\2DE\5\24\13\2E\r\3\2\2\2FG\5\6\4\2G")
        buf.write("H\7\17\2\2HI\5\24\13\2I\17\3\2\2\2JT\3\2\2\2KP\5\26\f")
        buf.write("\2LM\7\f\2\2MO\5\26\f\2NL\3\2\2\2OR\3\2\2\2PN\3\2\2\2")
        buf.write("PQ\3\2\2\2QT\3\2\2\2RP\3\2\2\2SJ\3\2\2\2SK\3\2\2\2T\21")
        buf.write("\3\2\2\2UV\7\23\2\2VW\5\20\t\2W\23\3\2\2\2X[\5\34\17\2")
        buf.write("Y[\5\30\r\2ZX\3\2\2\2ZY\3\2\2\2[\25\3\2\2\2\\`\5\34\17")
        buf.write("\2]`\5\32\16\2^`\5\30\r\2_\\\3\2\2\2_]\3\2\2\2_^\3\2\2")
        buf.write("\2`\27\3\2\2\2ab\7J\2\2b\31\3\2\2\2cd\7\22\2\2d\33\3\2")
        buf.write("\2\2ef\t\2\2\2f\35\3\2\2\2gh\7K\2\2h\37\3\2\2\2\f%*/\63")
        buf.write("\66>PSZ_")
        return buf.getvalue()


class scasmParser ( Parser ):

    grammarFileName = "scasm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "':'", "'('", 
                     "')'", "','", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "INT_HEX", "INT_BIN", "INT_OCT", "INT_DEC", 
                      "White_Space", "EOL", "COLON", "LPARN", "RPARN", "COMMA", 
                      "ADD", "SUB", "DIR_EQU", "DIR_DW", "DIR_ORG", "Register", 
                      "OpCode", "OpJUMP", "OpJNEG", "OpJPOS", "OpJZERO", 
                      "OpSHIFT", "OpILOAD", "OpISTORE", "OpCLI", "OpSEI", 
                      "OpRETI", "OpLOADI", "OpNOP", "OpADDI", "OpADD", "OpSUBI", 
                      "OpSUB", "OpMULI", "OpMUL", "OpXCHG", "OpCMPI", "OpCMP", 
                      "OpORI", "OpOR", "OpXORI", "OpXOR", "OpANDI", "OpAND", 
                      "OpNOT", "OpOUT", "OpIN", "OpJO", "OpJNO", "OpJS", 
                      "OpJNS", "OpJE", "OpJNE", "OpJB", "OpJNB", "OpJBE", 
                      "OpJA", "OpJL", "OpJGE", "OpJLE", "OpJG", "OpJMP", 
                      "OpLOAD", "OpSTORE", "OpCALL", "OpRETURN", "OpPUSH", 
                      "OpPOP", "OpLW", "OpSW", "OpHALT", "ID", "COMMENT", 
                      "DOUBLE_SLASH_COMMENT", "WHITESPACE" ]

    RULE_scasmProg = 0
    RULE_scasmLine = 1
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
    RULE_comment = 14

    ruleNames =  [ "scasmProg", "scasmLine", "label", "directive", "directiveDW", 
                   "directiveORG", "directiveEQU", "operands", "instruction", 
                   "expr", "operand", "labelRef", "register", "integer", 
                   "comment" ]

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
    OpJUMP=18
    OpJNEG=19
    OpJPOS=20
    OpJZERO=21
    OpSHIFT=22
    OpILOAD=23
    OpISTORE=24
    OpCLI=25
    OpSEI=26
    OpRETI=27
    OpLOADI=28
    OpNOP=29
    OpADDI=30
    OpADD=31
    OpSUBI=32
    OpSUB=33
    OpMULI=34
    OpMUL=35
    OpXCHG=36
    OpCMPI=37
    OpCMP=38
    OpORI=39
    OpOR=40
    OpXORI=41
    OpXOR=42
    OpANDI=43
    OpAND=44
    OpNOT=45
    OpOUT=46
    OpIN=47
    OpJO=48
    OpJNO=49
    OpJS=50
    OpJNS=51
    OpJE=52
    OpJNE=53
    OpJB=54
    OpJNB=55
    OpJBE=56
    OpJA=57
    OpJL=58
    OpJGE=59
    OpJLE=60
    OpJG=61
    OpJMP=62
    OpLOAD=63
    OpSTORE=64
    OpCALL=65
    OpRETURN=66
    OpPUSH=67
    OpPOP=68
    OpLW=69
    OpSW=70
    OpHALT=71
    ID=72
    COMMENT=73
    DOUBLE_SLASH_COMMENT=74
    WHITESPACE=75

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScasmProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scasmLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(scasmParser.ScasmLineContext)
            else:
                return self.getTypedRuleContext(scasmParser.ScasmLineContext,i)


        def EOF(self):
            return self.getToken(scasmParser.EOF, 0)

        def EOL(self, i:int=None):
            if i is None:
                return self.getTokens(scasmParser.EOL)
            else:
                return self.getToken(scasmParser.EOL, i)

        def getRuleIndex(self):
            return scasmParser.RULE_scasmProg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScasmProg" ):
                listener.enterScasmProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScasmProg" ):
                listener.exitScasmProg(self)




    def scasmProg(self):

        localctx = scasmParser.ScasmProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_scasmProg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 30
                    self.scasmLine()
                    self.state = 31
                    self.match(scasmParser.EOL) 
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 38
            self.scasmLine()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==scasmParser.EOL:
                self.state = 39
                self.match(scasmParser.EOL)


            self.state = 42
            self.match(scasmParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScasmLineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label(self):
            return self.getTypedRuleContext(scasmParser.LabelContext,0)


        def directive(self):
            return self.getTypedRuleContext(scasmParser.DirectiveContext,0)


        def instruction(self):
            return self.getTypedRuleContext(scasmParser.InstructionContext,0)


        def comment(self):
            return self.getTypedRuleContext(scasmParser.CommentContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_scasmLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScasmLine" ):
                listener.enterScasmLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScasmLine" ):
                listener.exitScasmLine(self)




    def scasmLine(self):

        localctx = scasmParser.ScasmLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_scasmLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 44
                self.label()


            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scasmParser.DIR_DW, scasmParser.DIR_ORG, scasmParser.ID]:
                self.state = 47
                self.directive()
                pass
            elif token in [scasmParser.OpCode]:
                self.state = 48
                self.instruction()
                pass
            elif token in [scasmParser.EOF, scasmParser.EOL, scasmParser.COMMENT]:
                pass
            else:
                pass
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==scasmParser.COMMENT:
                self.state = 51
                self.comment()


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
            return self.getToken(scasmParser.ID, 0)

        def COLON(self):
            return self.getToken(scasmParser.COLON, 0)

        def getRuleIndex(self):
            return scasmParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)




    def label(self):

        localctx = scasmParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(scasmParser.ID)
            self.state = 55
            self.match(scasmParser.COLON)
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
            return self.getTypedRuleContext(scasmParser.DirectiveDWContext,0)


        def directiveORG(self):
            return self.getTypedRuleContext(scasmParser.DirectiveORGContext,0)


        def directiveEQU(self):
            return self.getTypedRuleContext(scasmParser.DirectiveEQUContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirective" ):
                listener.enterDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirective" ):
                listener.exitDirective(self)




    def directive(self):

        localctx = scasmParser.DirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scasmParser.DIR_DW]:
                self.state = 57
                self.directiveDW()
                pass
            elif token in [scasmParser.DIR_ORG]:
                self.state = 58
                self.directiveORG()
                pass
            elif token in [scasmParser.ID]:
                self.state = 59
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
            return self.getToken(scasmParser.DIR_DW, 0)

        def expr(self):
            return self.getTypedRuleContext(scasmParser.ExprContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_directiveDW

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirectiveDW" ):
                listener.enterDirectiveDW(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirectiveDW" ):
                listener.exitDirectiveDW(self)




    def directiveDW(self):

        localctx = scasmParser.DirectiveDWContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_directiveDW)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(scasmParser.DIR_DW)
            self.state = 63
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
            return self.getToken(scasmParser.DIR_ORG, 0)

        def expr(self):
            return self.getTypedRuleContext(scasmParser.ExprContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_directiveORG

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirectiveORG" ):
                listener.enterDirectiveORG(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirectiveORG" ):
                listener.exitDirectiveORG(self)




    def directiveORG(self):

        localctx = scasmParser.DirectiveORGContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_directiveORG)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(scasmParser.DIR_ORG)
            self.state = 66
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
            return self.getTypedRuleContext(scasmParser.LabelContext,0)


        def DIR_EQU(self):
            return self.getToken(scasmParser.DIR_EQU, 0)

        def expr(self):
            return self.getTypedRuleContext(scasmParser.ExprContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_directiveEQU

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirectiveEQU" ):
                listener.enterDirectiveEQU(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirectiveEQU" ):
                listener.exitDirectiveEQU(self)




    def directiveEQU(self):

        localctx = scasmParser.DirectiveEQUContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_directiveEQU)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.label()
            self.state = 69
            self.match(scasmParser.DIR_EQU)
            self.state = 70
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
                return self.getTypedRuleContexts(scasmParser.OperandContext)
            else:
                return self.getTypedRuleContext(scasmParser.OperandContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(scasmParser.COMMA)
            else:
                return self.getToken(scasmParser.COMMA, i)

        def getRuleIndex(self):
            return scasmParser.RULE_operands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperands" ):
                listener.enterOperands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperands" ):
                listener.exitOperands(self)




    def operands(self):

        localctx = scasmParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operands)
        self._la = 0 # Token type
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scasmParser.EOF, scasmParser.EOL, scasmParser.COMMENT]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [scasmParser.INT_HEX, scasmParser.INT_BIN, scasmParser.INT_OCT, scasmParser.INT_DEC, scasmParser.Register, scasmParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.operand()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==scasmParser.COMMA:
                    self.state = 74
                    self.match(scasmParser.COMMA)
                    self.state = 75
                    self.operand()
                    self.state = 80
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
            return self.getToken(scasmParser.OpCode, 0)

        def operands(self):
            return self.getTypedRuleContext(scasmParser.OperandsContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)




    def instruction(self):

        localctx = scasmParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_instruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(scasmParser.OpCode)
            self.state = 84
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
            return self.getTypedRuleContext(scasmParser.IntegerContext,0)


        def labelRef(self):
            return self.getTypedRuleContext(scasmParser.LabelRefContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = scasmParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scasmParser.INT_HEX, scasmParser.INT_BIN, scasmParser.INT_OCT, scasmParser.INT_DEC]:
                self.state = 86
                self.integer()
                pass
            elif token in [scasmParser.ID]:
                self.state = 87
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
            return self.getTypedRuleContext(scasmParser.IntegerContext,0)


        def register(self):
            return self.getTypedRuleContext(scasmParser.RegisterContext,0)


        def labelRef(self):
            return self.getTypedRuleContext(scasmParser.LabelRefContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)




    def operand(self):

        localctx = scasmParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scasmParser.INT_HEX, scasmParser.INT_BIN, scasmParser.INT_OCT, scasmParser.INT_DEC]:
                self.state = 90
                self.integer()
                pass
            elif token in [scasmParser.Register]:
                self.state = 91
                self.register()
                pass
            elif token in [scasmParser.ID]:
                self.state = 92
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
            return self.getToken(scasmParser.ID, 0)

        def getRuleIndex(self):
            return scasmParser.RULE_labelRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelRef" ):
                listener.enterLabelRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelRef" ):
                listener.exitLabelRef(self)




    def labelRef(self):

        localctx = scasmParser.LabelRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_labelRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(scasmParser.ID)
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
            return self.getToken(scasmParser.Register, 0)

        def getRuleIndex(self):
            return scasmParser.RULE_register

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegister" ):
                listener.enterRegister(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegister" ):
                listener.exitRegister(self)




    def register(self):

        localctx = scasmParser.RegisterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_register)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(scasmParser.Register)
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
            return self.getToken(scasmParser.INT_HEX, 0)

        def INT_DEC(self):
            return self.getToken(scasmParser.INT_DEC, 0)

        def INT_BIN(self):
            return self.getToken(scasmParser.INT_BIN, 0)

        def INT_OCT(self):
            return self.getToken(scasmParser.INT_OCT, 0)

        def getRuleIndex(self):
            return scasmParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)




    def integer(self):

        localctx = scasmParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << scasmParser.INT_HEX) | (1 << scasmParser.INT_BIN) | (1 << scasmParser.INT_OCT) | (1 << scasmParser.INT_DEC))) != 0)):
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


    class CommentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(scasmParser.COMMENT, 0)

        def getRuleIndex(self):
            return scasmParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = scasmParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(scasmParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





