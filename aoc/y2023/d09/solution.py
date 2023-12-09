from typing import Dict, List, Optional

from aoc.y2023.d09.inputs import INPUTS

_year = 2023
_label = "Day 09"

def next(history):
    diffs = list()
    for i in range(len(history)-1):
        diffs.append(history[i+1] - history[i])
    if len(set(diffs)) == 1:
        return diffs[0] + history[-1]
    return next(diffs) + history[-1]

def prev(history):
    diffs = list()
    for i in range(len(history)-1):
        diffs.append(history[i+1] - history[i])
    if len(set(diffs)) == 1:
        return history[0] - diffs[0]
    return history[0] - prev(diffs)

def part01(input: str):
    histories = [[int(hist) for hist in history.split()] for history in input.splitlines()]
    nexts = [next(h) for h in histories]
    return sum(nexts)


def part02(input: str):
    histories = [[int(hist) for hist in history.split()] for history in input.splitlines()]
    prevs = [prev(h) for h in histories]
    return sum(prevs)


def run():
    print(f"{_year} {_label} Example 1: {part01(INPUTS.get_example01())}")
    print(f"{_year} {_label} Part 1: {part01(INPUTS.get_part01())}")
    print(f"{_year} {_label} Example 2: {part02(INPUTS.get_example02())}")
    print(f"{_year} {_label} Part 2: {part02(INPUTS.get_part02())}")


if __name__ == "__main__":
    run()
