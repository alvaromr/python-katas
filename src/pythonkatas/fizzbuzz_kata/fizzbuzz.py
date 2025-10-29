from abc import ABC, abstractmethod
from typing import Sequence


def fizzbuzz(number: int):
    rules: Sequence[Rule] = [
        WordRule(3, "Fizz"),
        WordRule(5, "Buzz"),
        WordRule(7, "Wozz"),
        DefaultRule(),
    ]
    result = ""
    for rule in rules:
        result += rule.apply(number, result)
    return result

class Rule(ABC):
    @abstractmethod
    def apply(self, number: int, result: str) -> str:
        pass

class WordRule(Rule):
    def __init__(self, number: int, word: str) -> None:
        self.number = number
        self.word = word

    def apply(self, number: int, result: str) -> str:
        return self.word if number % self.number == 0 or str(self.number) in str(number) else ""

class DefaultRule(Rule):
    def apply(self, number: int, result: str) -> str:
        return str(number) if result == "" else ""
