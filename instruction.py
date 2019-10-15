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
        return (0xFFFF) & self.imm.val


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
        total = self.addOpcode() + self.addReservedBits() + self.addDst() + self.addSrc1() + self.addImm()
        return total


class RegsImm(Instruction):
    operand_types = [OperandType.REGISTER, OperandType.INTEGER]
    reserved_bits = 0b100

    def __init__(self, dst: Register, imm: Immediate):
        super().__init__(dst, imm=imm)

    def serialize(self) -> int:
        return self.addOpcode() + self.addReservedBits() + self.addDst() + self.addImm()


class TwoRegs(Instruction):
    operand_types = [OperandType.REGISTER, OperandType.REGISTER]
    reserved_bits = 0b000

    def __init__(self, dst: Register, src1: Register):
        super().__init__(dst, src1)

    def serialize(self) -> int:
        return self.addOpcode() + self.addReservedBits() + self.addDst() + self.addSrc1()


class TwoRegsCmp(Instruction):
    operand_types = [OperandType.REGISTER, OperandType.REGISTER]
    reserved_bits = 0b000

    def __init__(self, src1: Register, src2: Register):
        super().__init__(src1=src1, src2=src2)

    def serialize(self) -> int:
        return self.addOpcode() + self.addReservedBits() + self.addSrc1() + self.addSrc2()


class RegImmCmp(Instruction):
    operand_types = [OperandType.REGISTER, OperandType.INTEGER]
    reserved_bits = 0b000

    def __init__(self, src1: Register, imm: Immediate):
        super().__init__(src1=src1, imm=imm)

    def serialize(self) -> int:
        return self.addOpcode() + self.addReservedBits() + self.addSrc1() + self.addImm()


class Stack(Instruction):
    operand_types = [OperandType.REGISTER]
    reserved_bits = 0b000

    def __init__(self, dst: Register):
        super().__init__(dst, Register("sp"))

    def serialize(self) -> int:
        return self.addOpcode() + self.addReservedBits() + self.addDst() + self.addSrc1()


class NoRegs(Instruction):
    operand_types = []
    reserved_bits = 0b000

    def serialize(self) -> int:
        return self.addOpcode() + self.addReservedBits()


class Br(Instruction):
    operand_types = [OperandType.INTEGER]
    reserved_bits = 0b001
    condition = 0b0000

    def __init__(self, imm: Immediate, src1: Register = Register("r0")):
        super().__init__(dst=Register(num=self.condition), src1=src1, imm=imm)

    def serialize(self) -> int:
        return self.addOpcode() + self.addReservedBits() + self.addDst() + self.addSrc1() + self.addImm()

    @staticmethod
    def parse_operands(operands: List[Operand], *args: OperandType):
        parsed_operands = []
        if len(operands) == 1:
            if not operands[0].type == OperandType.INTEGER:
                raise Exception(f"Operand should be a {OperandType.INTEGER} but was a {operands[0].type}.")
            parsed_operands.append(Immediate(operands[0].value))

        elif len(operands) == 2:
            if not operands[1].type == OperandType.INTEGER:
                raise Exception(f"Operand should be a {OperandType.INTEGER} but was a {operands[1].type}.")
            parsed_operands.append(Immediate(operands[1].value))
            if not operands[0].type == OperandType.REGISTER:
                raise Exception(f"Operand should be a {OperandType.REGISTER} but was a {operands[0].type}.")
            parsed_operands.append(Register(operands[0].value))

        else:
            raise Exception(f"Should have either 1 or 2 operands but has {len(operands)}.")
        return parsed_operands


class Call(Instruction):
    reserved_bits = 0b001

    def __init__(self, imm: Immediate, src1: Register = Register("r0")):
        super().__init__(dst=Register("sp"), src1=src1, imm=imm)

    def serialize(self) -> int:
        return self.addOpcode() + self.addReservedBits() + self.addDst() + self.addSrc1() + self.addImm()

    @staticmethod
    def parse_operands(operands: List[Operand], *args: OperandType):
        parsed_operands = []
        if len(operands) == 1:
            if not operands[0].type == OperandType.INTEGER:
                raise Exception(f"Operand should be a {OperandType.INTEGER} but was a {operands[0].type}.")
            parsed_operands.append(Immediate(operands[0].value))

        elif len(operands) == 2:
            if not operands[1].type == OperandType.INTEGER:
                raise Exception(f"Operand should be a {OperandType.INTEGER} but was a {operands[1].type}.")
            parsed_operands.append(Immediate(operands[1].value))
            if not operands[0].type == OperandType.REGISTER:
                raise Exception(f"Operand should be a {OperandType.REGISTER} but was a {operands[0].type}.")
            parsed_operands.append(Register(operands[0].value))

        else:
            raise Exception(f"Should have either 1 or 2 operands but has {len(operands)}.")
        return parsed_operands


class Ret(Instruction):
    def __init__(self):
        super().__init__(dst=Register("sp"))

    def serialize(self) -> int:
        return self.addOpcode() + self.addReservedBits() + self.addDst()


def ins_class_rrr(name: str, opcode: int, reserved_bits: int = 0b000) -> type(Instruction):
    return type(name, (ThreeRegs,), {'opcode': opcode, 'reserved_bits': reserved_bits})


def ins_class_rri(name: str, opcode: int, reserved_bits: int = 0b000) -> type(Instruction):
    return type(name, (TwoRegsImm,), {'opcode': opcode, 'reserved_bits': reserved_bits})


def ins_class_rr(name: str, opcode: int, reserved_bits: int = 0b000) -> type(Instruction):
    return type(name, (TwoRegs,), {'opcode': opcode, 'reserved_bits': reserved_bits})


def ins_class_ri(name: str, opcode: int, reserved_bits: int = 0b000) -> type(Instruction):
    return type(name, (RegsImm,), {'opcode': opcode, 'reserved_bits': reserved_bits})


def ins_class_rr_cmp(name: str, opcode: int, reserved_bits: int = 0b000) -> type(Instruction):
    return type(name, (TwoRegsCmp,), {'opcode': opcode, 'reserved_bits': reserved_bits})


def ins_class_ri_cmp(name: str, opcode: int, reserved_bits: int = 0b000) -> type(Instruction):
    return type(name, (RegImmCmp,), {'opcode': opcode, 'reserved_bits': reserved_bits})


def ins_class_none(name: str, opcode: int, reserved_bits: int = 0b000) -> type(Instruction):
    return type(name, (NoRegs,), {'opcode': opcode, 'reserved_bits': reserved_bits})


def ins_class_br(name: str, opcode: int, condition: int) -> type(Instruction):
    return type(name, (Br,), {'opcode': opcode, 'condition': condition})


def ins_class_pushpop(name: str, opcode: int, reserved_bits: int = 0b000) -> type(Instruction):
    return type(name, (Stack,), {'opcode': opcode, 'reserved_bits': reserved_bits})


def ins_class_call(name: str, opcode: int, reserved_bits: int = 0b000) -> type(Instruction):
    return type(name, (Call,), {'opcode': opcode, 'reserved_bits': reserved_bits})


def ins_class_ret(name: str, opcode: int, reserved_bits: int = 0b000) -> type(Instruction):
    return type(name, (Ret,), {'opcode': opcode, 'reserved_bits': reserved_bits})


instructions: List[Type[Instruction]] = [
    ins_class_rrr("ADD", 0x1, 0b001),
    ins_class_rri("ADDI", 0x1, 0b101),
    ins_class_rrr("SUB", 0x2, 0b001),
    ins_class_rri("SUBI", 0x2, 0b101),
    ins_class_rrr("MUL", 0x3, 0b001),
    ins_class_rri("MULI", 0x3, 0b101),
    ins_class_rr("XCHG", 0x4, 0b001),
    ins_class_rr_cmp("CMP", 0x5, 0b001),
    ins_class_ri_cmp("CMPI", 0x5, 0b101),
    ins_class_rrr("OR", 0x6, 0b001),
    ins_class_rri("ORI", 0x6, 0b101),
    ins_class_rrr("XOR", 0x7, 0b001),
    ins_class_rri("XORI", 0x7, 0b101),
    ins_class_rrr("AND", 0x8, 0b001),
    ins_class_rri("ANDI", 0x8, 0b101),
    ins_class_rr("NOT", 0x9, 0b001),
    # SHR
    # SHL
    #                          jump_no
    ins_class_br("JO", 0xC, 0x0),
    ins_class_br("JNO", 0xC, 0x1),
    ins_class_br("JS", 0xC, 0x2),
    ins_class_br("JNS", 0xC, 0x3),
    ins_class_br("JE", 0xC, 0x4),
    ins_class_br("JNE", 0xC, 0x5),
    ins_class_br("JB", 0xC, 0x6),
    ins_class_br("JNB", 0xC, 0x7),
    ins_class_br("JBE", 0xC, 0x8),
    ins_class_br("JA", 0xC, 0x9),
    ins_class_br("JL", 0xC, 0xA),
    ins_class_br("JGE", 0xC, 0xB),
    ins_class_br("JLE", 0xC, 0xC),
    ins_class_br("JG", 0xC, 0xD),
    ins_class_br("JMP", 0xC, 0xF),
    ins_class_call("CALL", 0xD),
    ins_class_ret("RET", 0xE),
    # IO
    ins_class_ri("IN", 0x10, 0b000),
    ins_class_ri("OUT", 0x11, 0b000),
    # Memory
    ins_class_pushpop("PUSH", 0x14, 0b000),
    ins_class_pushpop("POP", 0x15, 0b000),
    ins_class_rri("LW", 0x16, 0b001),
    ins_class_rri("SW", 0x17, 0b001),
    # HALT
    ins_class_none("HALT", 0x0)
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
    return ret
