from typing import List, Dict
import struct

import argparse

from antlr4 import *
from antlr.scasmLexer import scasmLexer
from antlr.scasmParser import scasmParser

from scasm_listener import SCASMListener
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
    parser = argparse.ArgumentParser(description='SCOMP assembler')
    parser.add_argument("-o", required=True, type=str, metavar='output_prefix')
    parser.add_argument("-b", action='store_true')
    parser.add_argument("-a", action='store_true', help='Set output as Altera assembly')
    parser.add_argument('file', type=str)

    args = parser.parse_args()

    filename = args.file
    input = FileStream(filename)
    lexer = scasmLexer(input)
    stream = CommonTokenStream(lexer)
    parser = scasmParser(stream)
    tree = parser.scasmProg()  # Parse Root

    listener = SCASMListener()
    walker = ParseTreeWalker()

    walker.walk(listener, tree)
    label_dict = listener.label_dict
    chunks = listener.lines

    resolve_labels(chunks, label_dict)

    for chunk in listener.lines:
        print("----chunk---")
        print(chunk)

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

    asm = []
    for number, line in enumerate(memory):
        # print(f"{line:08X}")
        print(f"{number:0>3d}: {line:016b} {line:04X}")
        asm.append(f"\t\t{number:0>3d}: {line:04X}\n")

    if args.b:
        with open(f'{args.o}.bin', 'wb') as binFile:
            for i in range(0, len(memory)) :
                binFile.write(struct.pack(">H", memory[i]))
            binFile.flush()
    if args.a:
        import os
        with open(os.path.join(os.path.dirname(__file__), "asm_header.txt")) as header:
            header_text = header.read()
        with open(os.path.join(os.path.dirname(__file__), "asm_footer.txt")) as footer:
            footer_text = footer.read()
        with open(f'{args.o}.asm', 'w') as seqFile:
            data_width = 8
            seqFile.write(header_text)
            seqFile.writelines(asm)
            seqFile.write(footer_text)
    else:
        with open(f'{args.o}.hex', 'w') as seqFile:
            data_width = 8
            seqFile.write(to_intel_hex(memory, data_width))
            seqFile.flush()

