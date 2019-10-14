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

    print("resolving...")
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

    memory = []

    for chunk in chunks:
        memory.extend(chunk.serialize())

    for instruction in memory:
        print("{:032b}".format(instruction))
