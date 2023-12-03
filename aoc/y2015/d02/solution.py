from typing import Dict, List, Optional
import functools

from aoc.y2015.d02.inputs import INPUTS

_year = 2015
_label = "Day 02"


def part01(input: str):
    total_area = 0
    for size in input.splitlines():
        dimensions = [int(dim) for dim in size.split("x")]
        side_areas = [2*dimensions[i]*dimensions[(i +1)%3] for i in range(len(dimensions))]
        total_area += sum(side_areas) + int(min(side_areas) / 2)
    return total_area


def part02(input: str):
    total_length = 0
    for size in input.splitlines():
        dimensions = [int(dim) for dim in size.split("x")]
        dimensions.sort()
        total_length += 2*dimensions[0] + 2*dimensions[1]
        total_length += functools.reduce(lambda a, b: a * b, dimensions)
    return total_length


def run():
    print(f"{_year} {_label} Example 1: {part01(INPUTS.get_example01())}")
    print(f"{_year} {_label} Part 1: {part01(INPUTS.get_part01())}")
    print(f"{_year} {_label} Example 2: {part02(INPUTS.get_example02())}")
    print(f"{_year} {_label} Part 2: {part02(INPUTS.get_part02())}")


if __name__ == "__main__":
    run()
