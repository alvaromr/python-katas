from typing import Sequence
from pydantic import BaseModel

class Rule(BaseModel):
    divisor: int
    word: str

    def apply(self, number: int) -> str:
        return self.word if number % self.divisor == 0 or str(self.divisor) in str(number) else ""

default_rules: Sequence[Rule] = (
    Rule(divisor=3, word="Fizz"),
    Rule(divisor=5, word="Buzz"),
    Rule(divisor=7, word="Wozz"),
)

def fizzbuzz(number: int, rules: Sequence[Rule] = default_rules):
    result = ""
    for rule in rules:
        result += rule.apply(number)
    return result if result != "" else str(number)

