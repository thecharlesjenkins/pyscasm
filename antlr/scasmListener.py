# Generated from /home/araara/Documents/scomp_as/scasm.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .scasmParser import scasmParser
else:
    from scasmParser import scasmParser

# This class defines a complete listener for a parse tree produced by scasmParser.
class scasmListener(ParseTreeListener):

    # Enter a parse tree produced by scasmParser#scasmProg.
    def enterScasmProg(self, ctx:scasmParser.ScasmProgContext):
        pass

    # Exit a parse tree produced by scasmParser#scasmProg.
    def exitScasmProg(self, ctx:scasmParser.ScasmProgContext):
        pass


    # Enter a parse tree produced by scasmParser#scasmLine.
    def enterScasmLine(self, ctx:scasmParser.ScasmLineContext):
        pass

    # Exit a parse tree produced by scasmParser#scasmLine.
    def exitScasmLine(self, ctx:scasmParser.ScasmLineContext):
        pass


    # Enter a parse tree produced by scasmParser#label.
    def enterLabel(self, ctx:scasmParser.LabelContext):
        pass

    # Exit a parse tree produced by scasmParser#label.
    def exitLabel(self, ctx:scasmParser.LabelContext):
        pass


    # Enter a parse tree produced by scasmParser#directive.
    def enterDirective(self, ctx:scasmParser.DirectiveContext):
        pass

    # Exit a parse tree produced by scasmParser#directive.
    def exitDirective(self, ctx:scasmParser.DirectiveContext):
        pass


    # Enter a parse tree produced by scasmParser#directiveDW.
    def enterDirectiveDW(self, ctx:scasmParser.DirectiveDWContext):
        pass

    # Exit a parse tree produced by scasmParser#directiveDW.
    def exitDirectiveDW(self, ctx:scasmParser.DirectiveDWContext):
        pass


    # Enter a parse tree produced by scasmParser#directiveORG.
    def enterDirectiveORG(self, ctx:scasmParser.DirectiveORGContext):
        pass

    # Exit a parse tree produced by scasmParser#directiveORG.
    def exitDirectiveORG(self, ctx:scasmParser.DirectiveORGContext):
        pass


    # Enter a parse tree produced by scasmParser#directiveEQU.
    def enterDirectiveEQU(self, ctx:scasmParser.DirectiveEQUContext):
        pass

    # Exit a parse tree produced by scasmParser#directiveEQU.
    def exitDirectiveEQU(self, ctx:scasmParser.DirectiveEQUContext):
        pass


    # Enter a parse tree produced by scasmParser#operands.
    def enterOperands(self, ctx:scasmParser.OperandsContext):
        pass

    # Exit a parse tree produced by scasmParser#operands.
    def exitOperands(self, ctx:scasmParser.OperandsContext):
        pass


    # Enter a parse tree produced by scasmParser#instruction.
    def enterInstruction(self, ctx:scasmParser.InstructionContext):
        pass

    # Exit a parse tree produced by scasmParser#instruction.
    def exitInstruction(self, ctx:scasmParser.InstructionContext):
        pass


    # Enter a parse tree produced by scasmParser#expr.
    def enterExpr(self, ctx:scasmParser.ExprContext):
        pass

    # Exit a parse tree produced by scasmParser#expr.
    def exitExpr(self, ctx:scasmParser.ExprContext):
        pass


    # Enter a parse tree produced by scasmParser#operand.
    def enterOperand(self, ctx:scasmParser.OperandContext):
        pass

    # Exit a parse tree produced by scasmParser#operand.
    def exitOperand(self, ctx:scasmParser.OperandContext):
        pass


    # Enter a parse tree produced by scasmParser#labelRef.
    def enterLabelRef(self, ctx:scasmParser.LabelRefContext):
        pass

    # Exit a parse tree produced by scasmParser#labelRef.
    def exitLabelRef(self, ctx:scasmParser.LabelRefContext):
        pass


    # Enter a parse tree produced by scasmParser#register.
    def enterRegister(self, ctx:scasmParser.RegisterContext):
        pass

    # Exit a parse tree produced by scasmParser#register.
    def exitRegister(self, ctx:scasmParser.RegisterContext):
        pass


    # Enter a parse tree produced by scasmParser#integer.
    def enterInteger(self, ctx:scasmParser.IntegerContext):
        pass

    # Exit a parse tree produced by scasmParser#integer.
    def exitInteger(self, ctx:scasmParser.IntegerContext):
        pass


    # Enter a parse tree produced by scasmParser#comment.
    def enterComment(self, ctx:scasmParser.CommentContext):
        pass

    # Exit a parse tree produced by scasmParser#comment.
    def exitComment(self, ctx:scasmParser.CommentContext):
        pass


