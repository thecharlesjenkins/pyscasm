from typing import List, Dict, Type
from operand import Operand, OperandType
from register import Register
from immediate import Immediate


class UnformedInstruction:
    def __init__(self, opcode: str, operands: List[Operand]):
        self.opcode = opcode
        self.operands = operands

    def __str__(self):
        return f"{self.opcode} {self.operands}"

    def __repr__(self):
        return f"{self.opcode} {self.operands}"


class Instruction:
    operand_types = None

    def serialize(self) -> int:
        pass

    @classmethod
    def build(cls: Type['Instruction'], operands: List[Operand]) -> 'Instruction':
        parsed_operands: List = cls.parse_operands(operands, cls.operand_types)
        return cls(*parsed_operands)

    @staticmethod
    def parse_operands(operands: List[Operand], *args: OperandType):
        num_operands = len(*args)
        parsed_operands = []
        args = args[0]
        if len(operands) != num_operands:
            raise Exception(f"Should have {num_operands} operands but has {len(operands)}.")
        for i in range(num_operands):
            if operands[i].type != args[i]:
                raise Exception(f"Operand should be a {args[i]} but was a {operands[i].type}.")
            if operands[i].type == OperandType.REGISTER:
                parsed_operands.append(Register(operands[i].value))
            else:
                parsed_operands.append(Immediate(operands[i].value))
        return parsed_operands

    def addOpcode(self) -> int:
        return self.opcode << 27

    def addReservedBits(self) -> int:
        return self.reserved_bits << 24

    def addDst(self) -> int:
        return self.dst.num() << 20

    def addSrc1(self) -> int:
        return self.src1.num() << 16

    def addSrc2(self) -> int:
        return self.src2.num() << 12

    def addImm(self) -> int:
        return self.imm.val


class ThreeRegs(Instruction):
    operand_types = [OperandType.REGISTER, OperandType.REGISTER, OperandType.REGISTER]
    reserved_bits = 0b000

    def __init__(self, dst: Register, src1: Register, src2: Register):
        self.dst = dst
        self.src1 = src1
        self.src2 = src2

    def serialize(self) -> int:
        return self.addOpcode() + self.addReservedBits() + self.addDst() + self.addSrc1() + self.addSrc2()


class TwoRegsImm(Instruction):
    operand_types = [OperandType.REGISTER, OperandType.REGISTER, OperandType.INTEGER]
    reserved_bits = 0b100

    def __init__(self, dst: Register, src1: Register, imm: Immediate):
        self.dst = dst
        self.src1 = src1
        self.imm = imm

    def serialize(self) -> int:
        return self.addOpcode() + self.addReservedBits() + self.addDst() + self.addSrc1() + self.addImm()


class ADD(ThreeRegs):
    opcode = 0x1
    reserved_bits = 0b000


class ADDI(TwoRegsImm):
    opcode = 0x1
    reserved_bits = 0b100


instruction_dict: Dict[str, Type[Instruction]] = {
    'add': ADD,
    'addi': ADDI,
    # 'sub': SUB,
    # 'subi': SUBI,
}


def make_instruction(unformed_instruction: UnformedInstruction) -> Instruction:
    opcode = unformed_instruction.opcode.lower()
    if opcode not in instruction_dict:
        raise Exception(f"Can't assemble instruction {opcode} yet...")

    return instruction_dict[opcode].build(unformed_instruction.operands)
