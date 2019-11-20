from typing import Dict, List
from collections import OrderedDict

from antlr4 import *

from antlr.scasmParser import scasmParser
from operand import Operand, OperandType
from instruction import UnformedInstruction
from chunk import Chunk
from directive import Directive, DirectiveType


# This class defines a complete listener for a parse tree produced by scasmParser.
class SCASMListener(ParseTreeListener):
    def __init__(self):
        self.label_dict: OrderedDict[str, int] = OrderedDict()
        self.lines: List[Chunk] = [Chunk(0)]

    def get_line_number(self) -> int:
        return self.lines[-1].next_line_number()

    # Exit a parse tree produced by scasmParser#scasmLine.
    def exitScasmLine(self, ctx: scasmParser.ScasmLineContext):
        if ctx.label():
            label_name = ctx.label().label_name
            if label_name in self.label_dict:
                print(f'DUPLICATE LABEL: "{label_name}"')
                exit(-1)
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

    # Exit a parse tree produced by scasmParser#label.
    def exitLabel(self, ctx: scasmParser.LabelContext):
        ctx.label_name = ctx.ID().getText().lower()

    # Exit a parse tree produced by scasmParser#directive.
    def exitDirective(self, ctx: scasmParser.DirectiveContext):
        ctx.directive = ctx.children[0].directive

    # Exit a parse tree produced by scasmParser#directiveDW.
    def exitDirectiveDW(self, ctx: scasmParser.DirectiveDWContext):
        ctx.directive = Directive(DirectiveType.DW, ctx.expr().expr)

    # Exit a parse tree produced by scasmParser#directiveORG.
    def exitDirectiveORG(self, ctx: scasmParser.DirectiveORGContext):
        ctx.directive = Directive(DirectiveType.ORG, ctx.expr().expr)

    # Exit a parse tree produced by scasmParser#directiveEQU.
    def exitDirectiveEQU(self, ctx: scasmParser.DirectiveEQUContext):
        ctx.directive = Directive(DirectiveType.EQU, ctx.expr().expr, ctx.label().label_name)
        ctx.expr = ctx.expr().expr

    def exitOperands(self, ctx: scasmParser.OperandsContext):
        def get_operand(operand_ctx: scasmParser.OperandContext):
            return operand_ctx.operand

        ctx.operands = list(map(get_operand, ctx.operand()))

    # Exit a parse tree produced by scasmParser#instruction.
    def exitInstruction(self, ctx: scasmParser.InstructionContext):
        ctx.instruction = UnformedInstruction(ctx.OpCode().getText(), ctx.operands().operands)

    # Exit a parse tree produced by scasmParser#expr.
    def exitExpr(self, ctx: scasmParser.ExprContext):
        child = ctx.children[0]
        if isinstance(child, scasmParser.LabelRefContext):
            ctx.expr = (OperandType.LABEL, child.getText())
        elif isinstance(child, scasmParser.IntegerContext):
            ctx.expr = (OperandType.INTEGER, child.value)

    def exitOperand(self, ctx: scasmParser.OperandContext):
        child = ctx.children[0]
        if isinstance(child, scasmParser.LabelRefContext):
            ctx.operand = Operand(OperandType.LABEL, child.label_text)
        elif isinstance(child, scasmParser.IntegerContext):
            ctx.operand = Operand(OperandType.INTEGER, child.value)
        elif isinstance(child, scasmParser.RegisterContext):
            ctx.operand = Operand(OperandType.REGISTER, child.register_name)

    # Exit a parse tree produced by scasmParser#labelRef.
    def exitLabelRef(self, ctx: scasmParser.LabelRefContext):
        ctx.label_text = ctx.getText().lower()

    def exitRegister(self, ctx: scasmParser.RegisterContext):
        ctx.register_name = ctx.getText().lower()

    # Exit a parse tree produced by scasmParser#integer.
    def exitInteger(self, ctx: scasmParser.IntegerContext):
        if ctx.getText()[0:2].lower() == "&h":
            print(f"{ctx.getText()} -> {ctx.getText()[2:]}")
            hex_string = "0x" + ctx.getText()[2:]
            ctx.value = eval(hex_string)
        elif ctx.getText()[0:2].lower() == "&b":
            print(f"{ctx.getText()} -> {ctx.getText()[2:]}")
            b_string = "0b" + ctx.getText()[2:]
            ctx.value = eval(b_string)
        else:
            ctx.value = eval(ctx.getText())
