def fizzbuzz(param):
    result = ""

    rules = [
        lambda p, n: fizzbuzz_rule(p, divider=3, transformed="Fizz"),
        lambda p, n: fizzbuzz_rule(p, divider=5, transformed="Buzz"),
    ]
    for rule in rules:
        result += rule(param, result)
    return result if result != "" else str(param)


def fizzbuzz_rule(param: int, divider, transformed) -> str:
    return transformed if param % divider == 0 or str(divider) in str(param) else ""