from typing import Dict, List, Optional

from aoc.y2015.d01.inputs import INPUTS

_year = 2015
_label = "Day 01"


def part01(input: str):
    return input.count("(") - input.count(")")


def part02(input: str):
    queue = [0]
    for instruction in input:
        queue.append(queue[-1] + 1)
        if instruction == ")":
            if len(queue) == 2:
                return queue[-1]
            queue = queue[2:]


def run():
    print(f"{_year} {_label} Example 1: {part01(INPUTS.get_example01())}")
    print(f"{_year} {_label} Part 1: {part01(INPUTS.get_part01())}")
    print(f"{_year} {_label} Example 2: {part02(INPUTS.get_example02())}")
    print(f"{_year} {_label} Part 2: {part02(INPUTS.get_part02())}")


if __name__ == "__main__":
    run()
