from typing import Dict, List
from collections import OrderedDict

from antlr4 import *

from antlr.tl69asmParser import tl69asmParser
from operand import Operand, OperandType
from instruction import UnformedInstruction
from chunk import Chunk
from directive import Directive, DirectiveType


# This class defines a complete listener for a parse tree produced by tl69asmParser.
class TL69ASMListener(ParseTreeListener):
    def __init__(self):
        self.label_dict: OrderedDict[str, int] = OrderedDict()
        self.lines: List[Chunk] = [Chunk(0)]

    def get_line_number(self) -> int:
        return self.lines[-1].next_line_number()

    # Exit a parse tree produced by tl69asmParser#tl69asmLine.
    def exitTl69asmLine(self, ctx: tl69asmParser.Tl69asmLineContext):
        if ctx.label():
            label_name = ctx.label().label_name
            self.label_dict[label_name] = self.get_line_number()

        if ctx.instruction():
            self.lines[-1].instructions.append(ctx.instruction().instruction)
        elif ctx.directive():
            directive = ctx.directive().directive
            value = None
            if directive.expr[0] == OperandType.LABEL:
                label_name = directive.expr[1]
                if label_name in self.label_dict:
                    value = self.label_dict[label_name]
                else:
                    print("TODO: proper label resolution")
                    return
            elif directive.expr[0] == OperandType.INTEGER:
                value = directive.expr[1]

            if not value:
                return

            if directive.directive_type == DirectiveType.ORG:
                if self.lines[-1].empty():
                    self.lines[-1] = Chunk(value)
                else:
                    self.lines.append(Chunk(value))
            elif directive.directive_type == DirectiveType.DW:
                dw_instruction = UnformedInstruction("DW", [Operand(OperandType.INTEGER, value)])
                self.lines[-1].instructions.append(dw_instruction)
            elif directive.directive_type == DirectiveType.EQU:
                self.label_dict[directive.label] = value
                # print(self.label_dict)

    # Exit a parse tree produced by tl69asmParser#label.
    def exitLabel(self, ctx: tl69asmParser.LabelContext):
        ctx.label_name = ctx.ID().getText()

    # Exit a parse tree produced by tl69asmParser#directive.
    def exitDirective(self, ctx: tl69asmParser.DirectiveContext):
        ctx.directive = ctx.children[0].directive

    # Exit a parse tree produced by tl69asmParser#directiveDW.
    def exitDirectiveDW(self, ctx: tl69asmParser.DirectiveDWContext):
        ctx.directive = Directive(DirectiveType.DW, ctx.expr().expr)

    # Exit a parse tree produced by tl69asmParser#directiveORG.
    def exitDirectiveORG(self, ctx: tl69asmParser.DirectiveORGContext):
        ctx.directive = Directive(DirectiveType.ORG, ctx.expr().expr)

    # Exit a parse tree produced by tl69asmParser#directiveEQU.
    def exitDirectiveEQU(self, ctx: tl69asmParser.DirectiveEQUContext):
        ctx.directive = Directive(DirectiveType.EQU, ctx.expr().expr, ctx.label().label_name)
        ctx.expr = ctx.expr().expr

    def exitOperands(self, ctx: tl69asmParser.OperandsContext):
        def get_operand(operand_ctx: tl69asmParser.OperandContext):
            return operand_ctx.operand

        ctx.operands = list(map(get_operand, ctx.operand()))

    # Exit a parse tree produced by tl69asmParser#instruction.
    def exitInstruction(self, ctx: tl69asmParser.InstructionContext):
        ctx.instruction = UnformedInstruction(ctx.OpCode().getText(), ctx.operands().operands)

    # Exit a parse tree produced by tl69asmParser#expr.
    def exitExpr(self, ctx: tl69asmParser.ExprContext):
        child = ctx.children[0]
        if isinstance(child, tl69asmParser.LabelRefContext):
            ctx.expr = (OperandType.LABEL, child.getText())
        elif isinstance(child, tl69asmParser.IntegerContext):
            ctx.expr = (OperandType.INTEGER, child.value)

    def exitOperand(self, ctx: tl69asmParser.OperandContext):
        child = ctx.children[0]
        if isinstance(child, tl69asmParser.LabelRefContext):
            ctx.operand = Operand(OperandType.LABEL, child.label_text)
        elif isinstance(child, tl69asmParser.IntegerContext):
            ctx.operand = Operand(OperandType.INTEGER, child.value)
        elif isinstance(child, tl69asmParser.RegisterContext):
            ctx.operand = Operand(OperandType.REGISTER, child.register_name)

    # Exit a parse tree produced by tl69asmParser#labelRef.
    def exitLabelRef(self, ctx: tl69asmParser.LabelRefContext):
        ctx.label_text = ctx.getText()

    def exitRegister(self, ctx: tl69asmParser.RegisterContext):
        ctx.register_name = ctx.getText()

    # Exit a parse tree produced by tl69asmParser#integer.
    def exitInteger(self, ctx: tl69asmParser.IntegerContext):
        ctx.value = eval(ctx.getText())
