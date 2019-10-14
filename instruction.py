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
    opcode = None
    reserved_bits = None

    def __init__(self, dst: Register = None, src1: Register = None, src2: Register = None, imm: Immediate = None):
        self.dst: Register = dst
        self.src1: Register = src1
        self.src2: Register = src2
        self.imm: Immediate = imm

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
        super().__init__(dst, src1, src2)

    def serialize(self) -> int:
        return self.addOpcode() + self.addReservedBits() + self.addDst() + self.addSrc1() + self.addSrc2()


class TwoRegsImm(Instruction):
    operand_types = [OperandType.REGISTER, OperandType.REGISTER, OperandType.INTEGER]
    reserved_bits = 0b100

    def __init__(self, dst: Register, src1: Register, imm: Immediate):
        super().__init__(dst, src1, imm=imm)

    def serialize(self) -> int:
        return self.addOpcode() + self.addReservedBits() + self.addDst() + self.addSrc1() + self.addImm()


class TwoRegs(Instruction):
    operand_types = [OperandType.REGISTER, OperandType.REGISTER]
    reserved_bits = 0b000

    def __init__(self, dst: Register, src1: Register):
        super().__init__(dst, src1)

    def serialize(self) -> int:
        return self.addOpcode() + self.addReservedBits() + self.addDst() + self.addSrc1()


class NoRegs(Instruction):
    operand_types = []
    reserved_bits = 0b000

    def serialize(self) -> int:
        return self.addOpcode() + self.addReservedBits()


def ins_class_rrr(name: str, opcode: int, reserved_bits: int = 0b000) -> type(Instruction):
    return type(name, (ThreeRegs,), {'opcode': opcode, 'reserved_bits': reserved_bits})


def ins_class_rri(name: str, opcode: int, reserved_bits: int = 0b000) -> type(Instruction):
    return type(name, (TwoRegsImm,), {'opcode': opcode, 'reserved_bits': reserved_bits})


def ins_class_rr(name: str, opcode: int, reserved_bits: int = 0b000) -> type(Instruction):
    return type(name, (TwoRegs,), {'opcode': opcode, 'reserved_bits': reserved_bits})


def ins_class_none(name: str, opcode: int, reserved_bits: int = 0b000) -> type(Instruction):
    return type(name, (NoRegs,), {'opcode': opcode, 'reserved_bits': reserved_bits})


instructions: List[Type[Instruction]] = [
    ins_class_rrr("ADD", 0x1, 0b000),
    ins_class_rri("ADDI", 0x1, 0b100),
    ins_class_rrr("SUB", 0x2, 0b000),
    ins_class_rri("SUBI", 0x2, 0b100),
    ins_class_rrr("MUL", 0x3, 0b000),
    ins_class_rri("MULI", 0x3, 0b100),
    ins_class_rrr("XCHG", 0x4, 0b000),
    ins_class_rrr("CMP", 0x5, 0b000),
    ins_class_rri("CMPI", 0x5, 0b100),
    ins_class_rrr("OR", 0x6, 0b000),
    ins_class_rri("ORI", 0x6, 0b100),
    ins_class_rrr("XOR", 0x7, 0b000),
    ins_class_rri("XORI", 0x7, 0b100),
    ins_class_rrr("AND", 0x8, 0b000),
    ins_class_rri("ANDI", 0x8, 0b100),
    ins_class_rr("NOT", 0x9, 0b000),
    # SHR
    # SHL
    ins_class_none("HALT", 0x1f)
]

instruction_dict: Dict[str, Type[Instruction]] = {
}

for instruction in instructions:
    instruction_dict[instruction.__name__.lower()] = instruction


def make_instruction(unformed_instruction: UnformedInstruction) -> Instruction:
    opcode = unformed_instruction.opcode.lower()
    if opcode not in instruction_dict:
        raise Exception(f"Can't assemble instruction {opcode} yet...")

    return instruction_dict[opcode].build(unformed_instruction.operands)
