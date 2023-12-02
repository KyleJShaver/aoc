from dataclasses import dataclass
from typing import Optional


@dataclass
class Inputs:
    example01: str
    part01: str
    example02: Optional[str] = None
    part02: Optional[str] = None

    def get_example01(self):
        return self.example01

    def get_example02(self):
        return self.example02 or self.example01

    def get_part01(self):
        return self.part01

    def get_part02(self):
        return self.part02 or self.part01
