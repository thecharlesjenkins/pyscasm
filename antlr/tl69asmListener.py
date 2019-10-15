# Generated from /home/araara/Documents/tl69_assembler/tl69asm.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tl69asmParser import tl69asmParser
else:
    from tl69asmParser import tl69asmParser

# This class defines a complete listener for a parse tree produced by tl69asmParser.
class tl69asmListener(ParseTreeListener):

    # Enter a parse tree produced by tl69asmParser#tl69asmProg.
    def enterTl69asmProg(self, ctx:tl69asmParser.Tl69asmProgContext):
        pass

    # Exit a parse tree produced by tl69asmParser#tl69asmProg.
    def exitTl69asmProg(self, ctx:tl69asmParser.Tl69asmProgContext):
        pass


    # Enter a parse tree produced by tl69asmParser#tl69asmLine.
    def enterTl69asmLine(self, ctx:tl69asmParser.Tl69asmLineContext):
        pass

    # Exit a parse tree produced by tl69asmParser#tl69asmLine.
    def exitTl69asmLine(self, ctx:tl69asmParser.Tl69asmLineContext):
        pass


    # Enter a parse tree produced by tl69asmParser#label.
    def enterLabel(self, ctx:tl69asmParser.LabelContext):
        pass

    # Exit a parse tree produced by tl69asmParser#label.
    def exitLabel(self, ctx:tl69asmParser.LabelContext):
        pass


    # Enter a parse tree produced by tl69asmParser#directive.
    def enterDirective(self, ctx:tl69asmParser.DirectiveContext):
        pass

    # Exit a parse tree produced by tl69asmParser#directive.
    def exitDirective(self, ctx:tl69asmParser.DirectiveContext):
        pass


    # Enter a parse tree produced by tl69asmParser#directiveDW.
    def enterDirectiveDW(self, ctx:tl69asmParser.DirectiveDWContext):
        pass

    # Exit a parse tree produced by tl69asmParser#directiveDW.
    def exitDirectiveDW(self, ctx:tl69asmParser.DirectiveDWContext):
        pass


    # Enter a parse tree produced by tl69asmParser#directiveORG.
    def enterDirectiveORG(self, ctx:tl69asmParser.DirectiveORGContext):
        pass

    # Exit a parse tree produced by tl69asmParser#directiveORG.
    def exitDirectiveORG(self, ctx:tl69asmParser.DirectiveORGContext):
        pass


    # Enter a parse tree produced by tl69asmParser#directiveEQU.
    def enterDirectiveEQU(self, ctx:tl69asmParser.DirectiveEQUContext):
        pass

    # Exit a parse tree produced by tl69asmParser#directiveEQU.
    def exitDirectiveEQU(self, ctx:tl69asmParser.DirectiveEQUContext):
        pass


    # Enter a parse tree produced by tl69asmParser#operands.
    def enterOperands(self, ctx:tl69asmParser.OperandsContext):
        pass

    # Exit a parse tree produced by tl69asmParser#operands.
    def exitOperands(self, ctx:tl69asmParser.OperandsContext):
        pass


    # Enter a parse tree produced by tl69asmParser#instruction.
    def enterInstruction(self, ctx:tl69asmParser.InstructionContext):
        pass

    # Exit a parse tree produced by tl69asmParser#instruction.
    def exitInstruction(self, ctx:tl69asmParser.InstructionContext):
        pass


    # Enter a parse tree produced by tl69asmParser#expr.
    def enterExpr(self, ctx:tl69asmParser.ExprContext):
        pass

    # Exit a parse tree produced by tl69asmParser#expr.
    def exitExpr(self, ctx:tl69asmParser.ExprContext):
        pass


    # Enter a parse tree produced by tl69asmParser#operand.
    def enterOperand(self, ctx:tl69asmParser.OperandContext):
        pass

    # Exit a parse tree produced by tl69asmParser#operand.
    def exitOperand(self, ctx:tl69asmParser.OperandContext):
        pass


    # Enter a parse tree produced by tl69asmParser#labelRef.
    def enterLabelRef(self, ctx:tl69asmParser.LabelRefContext):
        pass

    # Exit a parse tree produced by tl69asmParser#labelRef.
    def exitLabelRef(self, ctx:tl69asmParser.LabelRefContext):
        pass


    # Enter a parse tree produced by tl69asmParser#register.
    def enterRegister(self, ctx:tl69asmParser.RegisterContext):
        pass

    # Exit a parse tree produced by tl69asmParser#register.
    def exitRegister(self, ctx:tl69asmParser.RegisterContext):
        pass


    # Enter a parse tree produced by tl69asmParser#integer.
    def enterInteger(self, ctx:tl69asmParser.IntegerContext):
        pass

    # Exit a parse tree produced by tl69asmParser#integer.
    def exitInteger(self, ctx:tl69asmParser.IntegerContext):
        pass


    # Enter a parse tree produced by tl69asmParser#comment.
    def enterComment(self, ctx:tl69asmParser.CommentContext):
        pass

    # Exit a parse tree produced by tl69asmParser#comment.
    def exitComment(self, ctx:tl69asmParser.CommentContext):
        pass


