from typing import List, Dict

import argparse

from antlr4 import *
from antlr.tl69asmLexer import tl69asmLexer
from antlr.tl69asmParser import tl69asmParser

from tl69asm_listener import TL69ASMListener
from chunk import Chunk


def resolve_labels(chunks: List[Chunk], label_dict: Dict[str, int]):
    for i in range(len(chunks)):
        chunks[i].resolve(label_dict)


def to_intel_hex(memory: List[int], width: int):
    record_type = "00"
    output = ""
    for address, data in enumerate(memory):
        hex_data = f"{data:02X}".zfill(width)

        checksum = width // 2
        lol_address = address
        while lol_address > 0:
            checksum = checksum + lol_address & 0xff
            lol_address = lol_address >> 8

        while data > 0:
            checksum = checksum + data & 0xff
            data = data >> 8

        checksum = (-checksum) & 0xff

        line = f":{(width // 2):02X}{address:04X}{record_type}{hex_data}{checksum:02X}\n"
        output += line
    output += ":00000001FF\n"
    return output

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TL69 assembler')
    parser.add_argument("-o", required=True, type=str, metavar='output_prefix')
    parser.add_argument('file', type=str)

    args = parser.parse_args()

    filename = args.file
    input = FileStream(filename)
    lexer = tl69asmLexer(input)
    stream = CommonTokenStream(lexer)
    parser = tl69asmParser(stream)
    tree = parser.tl69asmProg()  # Parse Root

    listener = TL69ASMListener()
    walker = ParseTreeWalker()

    walker.walk(listener, tree)
    label_dict = listener.label_dict
    chunks = listener.lines
    for chunk in listener.lines:
        print(chunk)
        print()

    for key, val in label_dict.items():
        print(f"{key} -> {val}")
    resolve_labels(chunks, label_dict)

    chunks.sort()

    for v, w in zip(chunks[:-1], chunks[1:]):
        if v.next_line_number() > w.starting_line:
            raise Exception(
                "Chunks starting at {} (length {}) and {} (length {}) are overlapping!".format(v.starting_line,
                                                                                               len(v.instructions),
                                                                                               w.starting_line,
                                                                                               len(w.instructions)))

    memory: List[int] = [0 for i in range(chunks[-1].next_line_number())]

    for chunk in chunks:
        chunk.serialize(memory)

    for line in memory:
        print(f"{line:0X}")

    with open((f'{args.o}.hex'), 'w') as seqFile:
        data_width = 32
        seqFile.write(to_intel_hex(memory, data_width))
        seqFile.flush()

