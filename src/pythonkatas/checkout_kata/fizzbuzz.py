def fizzbuzz(number: int):
    result = ""

    rules = [
        lambda n, r: fizzbuzz_rule(n, 3, "Fizz"),
        lambda n, r: fizzbuzz_rule(n, 5, "Buzz"),
        lambda n, r: default_rule(n, r),
    ]
    for rule in rules:
        result += rule(number, result)
    return result


def default_rule(number: int, result: str) -> str:
    return str(number) if result == "" else ""


def fizzbuzz_rule(number: int, divider: int, transformed: str) -> str:
    return transformed if number % divider == 0 or str(divider) in str(number) else ""