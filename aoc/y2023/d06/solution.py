from typing import Dict, List, Optional
import re
from functools import reduce

from aoc.y2023.d06.inputs import INPUTS

_year = 2023
_label = "Day 06"


def part01(input: str, condense=False):
    lines = input.splitlines()
    times = re.split(r"\s{1,}", re.split(r":\s{0,}", lines[0])[1])
    distances = re.split(r"\s{1,}", re.split(r":\s{0,}", lines[1])[1])
    if condense:
        times = [int("".join(times))]
        distances = [int("".join(distances))]
    else:
        times = [int(i) for i in times]
        distances = [int(d) for d in distances]
    margins = list()
    for i in range(len(times)):
        hold_length = list()
        time = times[i]
        for j in range(1, times[i]):
            distance = (time - j) * j
            if distance > distances[i]:
                hold_length.append(j)
        margins.append(len(hold_length))
    return reduce(lambda a, b: a * b, margins)


def part02(input: str):
    return part01(input, True)


def run():
    print(f"{_year} {_label} Example 1: {part01(INPUTS.get_example01())}")
    print(f"{_year} {_label} Part 1: {part01(INPUTS.get_part01())}")
    print(f"{_year} {_label} Example 2: {part02(INPUTS.get_example02())}")
    print(f"{_year} {_label} Part 2: {part02(INPUTS.get_part02())}")


if __name__ == "__main__":
    run()
