import re
from typing import Dict, List

from aoc.y2023.d01.inputs import INPUTS

_year = 2023
_label = "Day 01"


def part01(input: str):
    totals = list()
    for line in input.splitlines():
        no_letters = re.sub(r"[A-z]", "", line)
        totals.append(int(no_letters[0] + no_letters[-1]))
    return sum(totals)


def part02(input: str):
    newlines: List[str] = list()
    replacements: Dict[str, int] = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    replacements_pattern = "|".join(replacements.keys())
    for line in input.splitlines():
        line = re.sub(
            replacements_pattern,
            lambda match: str(replacements[match.group()]) + match.group()[1:],
            line,
            1,
        )
        line = re.sub(
            replacements_pattern[::-1],
            lambda match: str(replacements[match.group()[::-1]]),
            line[::-1],
            1,
        )[::-1]
        newlines.append(line)
    return "\n".join(newlines)


def run():
    print(f"{_year} {_label} Example 1: {part01(INPUTS.get_example01())}")
    print(f"{_year} {_label} Part 1: {part01(INPUTS.get_part01())}")
    print(f"{_year} {_label} Example 2: {part01(part02(INPUTS.get_example02()))}")
    print(f"{_year} {_label} Part 2: {part01(part02(INPUTS.get_part02()))}")


if __name__ == "__main__":
    run()
