from enum import Enum
from typing import Dict


class OperandType(Enum):
    REGISTER = 0,
    INTEGER = 1
    LABEL = 2,


class Operand:
    def __init__(self, operand_type: OperandType, value):
        self.type = operand_type
        self.value = value

    def resolve(self, label_dict: Dict[str, int]):
        if self.type == OperandType.LABEL:
            if self.value not in label_dict:
                raise Exception(f"Could not resolve label {self.value} after one pass!")

            self.type = OperandType.INTEGER
            self.value = label_dict[self.value]

    def __repr__(self):
        return f"{self.type}({self.value})"

    def __str__(self):
        return f"{self.type}({self.value})"

