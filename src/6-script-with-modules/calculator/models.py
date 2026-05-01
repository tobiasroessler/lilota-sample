from dataclasses import dataclass


@dataclass
class AddInput:
    a: int
    b: int


@dataclass
class AddOutput:
    sum: int
