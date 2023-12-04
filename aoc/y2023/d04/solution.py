from functools import cache
from typing import Dict, List, Optional

from aoc.y2023.d04.inputs import INPUTS

_year = 2023
_label = "Day 04"


def part01(input: str):
    points = list()
    cards = input.splitlines()
    numbers = [card.split(": ")[1].split(" | ") for card in cards]
    for card_numbers in numbers:
        winning_numbers = set([int(num) for num in card_numbers[0].split()])
        selected_numbers = set([int(num) for num in card_numbers[1].split()])
        overlap_count = len(winning_numbers.intersection(selected_numbers))
        if overlap_count == 0:
            continue
        points.append(2 ** (overlap_count - 1))
    return sum(points)


@cache
def count_scratchers(card_values, start=0):
    if start >= len(card_values):
        return 0
    total_count = 1
    winning_numbers, selected_numbers = card_values[start]
    overlap_count = len(set(winning_numbers).intersection(set(selected_numbers)))
    for i in range(1, overlap_count + 1):
        total_count += count_scratchers(card_values, start + i)
    return total_count


def part02(input: str):
    cards = input.splitlines()
    card_values = list()
    numbers = [card.split(": ")[1].split(" | ") for card in cards]
    for card_numbers in numbers:
        winning_numbers = tuple([int(num) for num in card_numbers[0].split()])
        selected_numbers = tuple([int(num) for num in card_numbers[1].split()])
        card_values.append((winning_numbers, selected_numbers))
    counts = [
        count_scratchers(tuple(card_values), card_num)
        for card_num in range(len(card_values))
    ]
    return sum(counts)


def run():
    print(f"{_year} {_label} Example 1: {part01(INPUTS.get_example01())}")
    print(f"{_year} {_label} Part 1: {part01(INPUTS.get_part01())}")
    print(f"{_year} {_label} Example 2: {part02(INPUTS.get_example02())}")
    print(f"{_year} {_label} Part 2: {part02(INPUTS.get_part02())}")


if __name__ == "__main__":
    run()
