from typing import Dict, List, Optional

from aoc.y2023.d02.inputs import INPUTS

_year = 2023
_label = "Day 02"


def part01(input: str, maxes: Dict[str, int] = {"red": 12, "green": 13, "blue": 14}):
    game_sets = {
        int(l.split(": ")[0].split()[1]): l.split(": ")[1] for l in input.splitlines()
    }
    possible_games: List[int] = list()
    for set_id, game_set in game_sets.items():
        possible = True
        for game in game_set.split("; "):
            for cube_count in game.split(", "):
                count, color = cube_count.split()
                if int(count) > maxes[color]:
                    possible = False
                    break
            if not possible:
                break
        if not possible:
            continue
        possible_games.append(set_id)
    return sum(possible_games)


def part02(input: str):
    game_sets = {
        int(l.split(": ")[0].split()[1]): l.split(": ")[1] for l in input.splitlines()
    }
    game_powers: List[int] = list()
    for set_id, game_set in game_sets.items():
        required: Dict[str, int] = {"red": 0, "green": 0, "blue": 0}
        for game in game_set.split("; "):
            for cube_count in game.split(", "):
                count, color = cube_count.split()
                required[color] = max(required[color], int(count))
        game_powers.append(required["red"] * required["blue"] * required["green"])
    return sum(game_powers)


def run():
    print(f"{_year} {_label} Example 1: {part01(INPUTS.get_example01())}")
    print(f"{_year} {_label} Part 1: {part01(INPUTS.get_part01())}")
    print(f"{_year} {_label} Example 2: {part02(INPUTS.get_example02())}")
    print(f"{_year} {_label} Part 2: {part02(INPUTS.get_part02())}")


if __name__ == "__main__":
    run()
