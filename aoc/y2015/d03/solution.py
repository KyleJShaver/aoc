from typing import Dict, List, Optional

from aoc.y2015.d03.inputs import INPUTS

_year = 2015
_label = "Day 03"

movements = {"^": (0, 1), "v": (0, -1), "<": (-1, 0), ">": (1, 0)}


def part01(input: str):
    position = (0, 0)
    delivered_positions = {position}
    for instruction in input:
        movement = movements[instruction]
        position = (position[0] + movement[0], position[1] + movement[1])
        delivered_positions.add(position)
    return delivered_positions


def part02(input: str):
    santa_paths = ["", ""]
    for pos, char in enumerate(input):
        santa_paths[pos % 2] += char
    delivered_positions = set()
    for path in santa_paths:
        delivered_positions.update(part01(path))
    return delivered_positions


def run():
    print(f"{_year} {_label} Example 1: {len(part01(INPUTS.get_example01()))}")
    print(f"{_year} {_label} Part 1: {len(part01(INPUTS.get_part01()))}")
    print(f"{_year} {_label} Example 2: {len(part02(INPUTS.get_example02()))}")
    print(f"{_year} {_label} Part 2: {len(part02(INPUTS.get_part02()))}")


if __name__ == "__main__":
    run()
