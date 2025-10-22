def fizzbuzz(param):
    result = ""

    rules = [
        lambda p, n: fizzbuzz_rule(p, divider=3, transformed="Fizz"),
        lambda p, n: fizzbuzz_rule(p, divider=5, transformed="Buzz"),
        lambda p, n: default_rule(param, result),
    ]
    for rule in rules:
        result += rule(param, result)
    return result


def default_rule(param, result: str) -> str:
    return str(param) if result == "" else ""


def fizzbuzz_rule(param: int, divider, transformed) -> str:
    return transformed if param % divider == 0 or str(divider) in str(param) else ""