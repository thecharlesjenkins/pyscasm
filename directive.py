from typing import List
from enum import Enum


class DirectiveType(Enum):
    DW = 0,
    ORG = 1,
    EQU = 2


class Directive:
    def __init__(self, directive_type: DirectiveType, expr, label = None):
        self.directive_type = directive_type
        self.expr = expr
        self.label = label

    def __str__(self):
        return f"{self.directive_type} {self.expr} {self.label if self.label else ''}"
