from typing import List, Dict
from instruction import Instruction
from operand import OperandType
from instruction import make_instruction


class Chunk:
    def __init__(self, starting_line: int):
        self.starting_line = starting_line
        self.instructions: List[Instruction] = []

    def empty(self):
        return len(self.instructions) == 0

    def next_line_number(self) -> int:
        return self.starting_line + len(self.instructions)

    def resolve(self, label_dict: Dict[str, int]):
        for i in range(len(self.instructions)):
            for j in range(len(self.instructions[i].operands)):
                self.instructions[i].operands[j].resolve(label_dict)

    def serialize(self) -> List[int]:
        return [make_instruction(instruction).serialize() for instruction in self.instructions]


    def __str__(self):
        lines = []
        for offset, instruction in enumerate(self.instructions):
            lines.append(f"{self.starting_line + offset}: {instruction}")
        return "\n".join(lines)

    def __lt__(self, other):
        return self.starting_line < other.starting_line
