from typing import Dict, List, Optional

from aoc.y2015.d01.inputs import INPUTS

_year = 2015
_label = "Day 01"


def part01(input: str):
    return input.count("(") - input.count(")")


def part02(input: str):
    floor, instruction_num = 1, 0
    for instruction in input:
        instruction_num += 1
        floor += 1 if instruction is "(" else -1
        if floor == 0:
            return instruction_num


def run():
    print(f"{_year} {_label} Example 1: {part01(INPUTS.get_example01())}")
    print(f"{_year} {_label} Part 1: {part01(INPUTS.get_part01())}")
    print(f"{_year} {_label} Example 2: {part02(INPUTS.get_example02())}")
    print(f"{_year} {_label} Part 2: {part02(INPUTS.get_part02())}")


if __name__ == "__main__":
    run()
