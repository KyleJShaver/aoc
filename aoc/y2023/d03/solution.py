import re
from typing import Dict, List, Optional, Set

from aoc.y2023.d03.inputs import INPUTS

_year = 2023
_label = "Day 03"


def part01(input: str):
    numbers = list()
    lines = input.splitlines()
    symbols = [
        set([m.span()[0] for m in list(re.finditer(r"[^\d\.]", line))])
        for line in lines
    ]
    for line_num, line in enumerate(lines):
        matches = list(re.finditer(r"\d+", line))
        for match in matches:
            span = match.span()
            search_set = set(
                range(max(span[0] - 1, 0), min(span[1] + 1, len(line) - 1))
            )
            is_part_num = False
            if line_num > 0:
                is_part_num = (
                    bool(len(search_set.intersection(symbols[line_num - 1])))
                    or is_part_num
                )
            if line_num < len(lines) - 1:
                is_part_num = (
                    bool(len(search_set.intersection(symbols[line_num + 1])))
                    or is_part_num
                )
            is_part_num = (
                bool(len(search_set.intersection(symbols[line_num]))) or is_part_num
            )
            if is_part_num:
                numbers.append(int(match.group()))
    return sum(numbers)


def part02(input: str):
    lines = input.splitlines()
    gear_ratios = list()
    numbers = [list(re.finditer(r"[\d]+", line)) for line in lines]
    number_spans = list()
    for number_line in numbers:
        line_lokup = dict()
        for number in number_line:
            for pos in range(number.span()[0], number.span()[1]):
                line_lokup[pos] = number
        number_spans.append(line_lokup)
    possible_gears = [list(re.finditer(r"\*", line)) for line in lines]
    for line_num, possible_gear_line in enumerate(possible_gears):
        for possible_gear in possible_gear_line:
            search_set: Set = set(
                range(
                    max(possible_gear.span()[0] - 1, 0),
                    min(possible_gear.span()[1] + 1, len(possible_gear.string) - 1),
                )
            )
            adjacent_numbers = set()
            for search_line_num in range(
                max(line_num - 1, 0), min(line_num + 1, len(possible_gears) - 1) + 1
            ):
                for match_index in search_set.intersection(
                    set(number_spans[search_line_num].keys())
                ):
                    adjacent_numbers.add(number_spans[search_line_num][match_index])
            if len(adjacent_numbers) == 2:
                ratio_components = [int(an.group()) for an in adjacent_numbers]
                gear_ratios.append(ratio_components[0] * ratio_components[1])
    return sum(gear_ratios)


def run():
    print(f"{_year} {_label} Example 1: {part01(INPUTS.get_example01())}")
    print(f"{_year} {_label} Part 1: {part01(INPUTS.get_part01())}")
    print(f"{_year} {_label} Example 2: {part02(INPUTS.get_example02())}")
    print(f"{_year} {_label} Part 2: {part02(INPUTS.get_part02())}")


if __name__ == "__main__":
    run()
