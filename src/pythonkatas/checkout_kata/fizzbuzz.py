def fizzbuzz(param):
    result = str(param)

    rules = [
        lambda n: fizzbuzz_rule(n, divider=15, transformed="FizzBuzz"),
        lambda n: fizzbuzz_rule(n, divider=3, transformed="Fizz"),
        lambda n: fizzbuzz_rule(n, divider=5, transformed="Buzz"),
    ]
    for rule in rules:
        result = rule(result)
    return result


def fizzbuzz_rule(param: str, divider, transformed) -> str:
    return transformed if param.isdigit() and int(param) % divider == 0 or str(divider) in param else param