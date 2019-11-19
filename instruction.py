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
    operand_types = []
    opcode = None
    reserved_bits = None

    def __init__(self, imm: Immediate = None):
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

    def addSmIMM(self) -> int:
        return (0x7FF) & self.imm.smval

    def addImm(self) -> int:
        return (0x7FF) & self.imm.val

    def addDW(self) -> int:
        return (0xFFFF) & self.imm.val

    def addOpcode(self) -> int:
        return self.opcode << 11


class SMImm(Instruction):
    operand_types = [OperandType.INTEGER]

    def __init__(self, imm: Immediate):
        super().__init__(imm)

    def serialize(self) -> int:
        return self.addOpcode() + self.addSmIMM()


class Imm(Instruction):
    operand_types = [OperandType.INTEGER]

    def __init__(self, imm: Immediate):
        super().__init__(imm)

    def serialize(self) -> int:
        return self.addOpcode() + self.addImm()


class DW(Instruction):
    operand_types = [OperandType.INTEGER]

    def __init__(self, imm: Immediate):
        super().__init__(imm)

    def serialize(self) -> int:
        return self.addDW()


class Nothing(Instruction):
    operand_types = []

    def __init__(self):
        super().__init__()

    def serialize(self) -> int:
        return self.addOpcode()

def inst_class_smi(name: str, opcode: int) -> type(Instruction):
    return type(name, (SMImm, ), {'opcode': opcode})

def ins_class_i(name: str, opcode: int) -> type(Instruction):
    return type(name, (Imm,), {'opcode': opcode})


def ins_class_dw(name: str) -> type(Instruction):
    return type(name, (DW,), {})


def ins_class_none(name: str, opcode: int) -> type(Instruction):
    return type(name, (Nothing,), {'opcode': opcode})


instructions: List[Type[Instruction]] = [
    ins_class_none("NOP", 0x00),
    ins_class_i("LOAD", 0x01),
    ins_class_i("STORE", 0x02),
    ins_class_i("ADD", 0x03),
    ins_class_i("SUB", 0x04),
    ins_class_i("JUMP", 0x05),
    ins_class_i("JNEG", 0x06),
    ins_class_i("JPOS", 0x07),
    ins_class_i("JZERO", 0x08),
    ins_class_i("AND", 0x09),
    ins_class_i("OR", 0x0A),
    ins_class_i("XOR", 0x0B),
    inst_class_smi("SHIFT", 0x0C),
    ins_class_i("ADDI", 0x0D),
    ins_class_i("ILOAD", 0x0E),
    ins_class_i("ISTORE", 0x0F),
    ins_class_i("CALL", 0x10),
    ins_class_none("RETURN", 0x11),
    ins_class_i("IN", 0x12),
    ins_class_i("OUT", 0x13),
    ins_class_i("CLI", 0x14),
    ins_class_i("SEI", 0x15),
    ins_class_none("RETI", 0x16),
    ins_class_i("LOADI", 0x17),
    # LMAO dw is an instruction
    ins_class_dw("DW"),
]

instruction_dict: Dict[str, Type[Instruction]] = {
}

for instruction in instructions:
    instruction_dict[instruction.__name__.lower()] = instruction


def make_instruction(unformed_instruction: UnformedInstruction) -> Instruction:
    opcode = unformed_instruction.opcode.lower()
    if opcode not in instruction_dict:
        raise Exception(f"Can't assemble instruction {opcode} yet...")

    ret = None
    try:
        ret = instruction_dict[opcode].build(unformed_instruction.operands)
    except Exception as e:
        print(e)
        print(unformed_instruction)
        raise e
    return ret
