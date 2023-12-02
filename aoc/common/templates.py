import os
import sys
from string import Template

inputs_template: Template = Template(
    '''from aoc.common.inputs import Inputs

INPUTS = Inputs(
    example01="""
""",
    example02="""
""",
    part01="""
""",
)'''
)

solution_template: Template = Template(
    """from typing import Dict, List, Optional

from aoc.y$year.d$day.inputs import INPUTS

_year = $year
_label = "Day $day"


def part01(input: str):
    return input


def part02(input: str):
    return input


def run():
    print(f"{_year} {_label} Example 1: {part01(INPUTS.get_example01())}")
    print(f"{_year} {_label} Part 1: {part01(INPUTS.get_part01())}")
    print(f"{_year} {_label} Example 2: {part02(INPUTS.get_example02())}")
    print(f"{_year} {_label} Part 2: {part02(INPUTS.get_part02())}")


if __name__ == "__main__":
    run()
"""
)


def new_files(root: str, year: int, day: int):
    sep = os.path.sep
    if root.endswith(os.path.sep):
        root = root[:-1]
    year_path = sep.join((root, "aoc", f"y{year}"))
    zero_padded_day = f"{day:02}"
    day_path = sep.join((year_path, f"d{zero_padded_day}"))
    if not os.path.exists(year_path):
        os.mkdir(year_path)
        with open(sep.join((year_path, "__init__.py")), "w") as f:
            pass
    if not os.path.exists(day_path):
        os.mkdir(day_path)
    with open(sep.join((day_path, "__init__.py")), "w") as f:
        pass
    with open(sep.join((day_path, "inputs.py")), "w") as f:
        f.write(inputs_template.safe_substitute())
    with open(sep.join((day_path, "solution.py")), "w") as f:
        f.write(solution_template.safe_substitute(year=year, day=zero_padded_day))


if __name__ == "__main__":
    year = 2023
    day = 3
    if len(sys.argv) == 3:
        year = int(sys.argv[1])
        day = int(sys.argv[2])
    new_files(".", year, day)
