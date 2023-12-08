from typing import Dict, List, Optional, Union
from functools import reduce
from math import lcm

from aoc.y2023.d08.inputs import INPUTS

_year = 2023
_label = "Day 08"

def make_tree(elements: List[str]):
    element_map = dict()
    for element in elements:
        value, elements = element.split(" = ")
        element_components = elements.replace("(", "").replace(")", "").split(", ")
        element_map[value] = (value, tuple(element_components))
    return element_map

def part01(input: str, start = "AAA", dest = lambda x: x == "ZZZ"):
    instructions, elements = [chunk.splitlines() for chunk in input.split("\n\n")]
    instructions = instructions[0]
    node_map = make_tree(elements)
    node = node_map[start]
    steps = 0
    while not dest(node[0]):
        if instructions[steps%len(instructions)] == "L":
            node = node_map[node[1][0]]
        else:
            node = node_map[node[1][1]]
        steps += 1
    return steps


def part02(input: str):
    instructions, elements = [chunk.splitlines() for chunk in input.split("\n\n")]
    instructions = instructions[0]
    node_map = make_tree(elements)
    nodes = tuple([node_map[x] for x in node_map if x.endswith("A")])
    cycles = [part01(input, node[0], lambda x: x.endswith("Z")) for node in nodes]
    return lcm(*cycles)


def run():
    print(f"{_year} {_label} Example 1: {part01(INPUTS.get_example01())}")
    print(f"{_year} {_label} Part 1: {part01(INPUTS.get_part01())}")
    print(f"{_year} {_label} Example 2: {part02(INPUTS.get_example02())}")
    print(f"{_year} {_label} Part 2: {part02(INPUTS.get_part02())}")


if __name__ == "__main__":
    run()
