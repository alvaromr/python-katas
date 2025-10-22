def fizzbuzz(param):
    result = str(param)

    rules = [
        lambda n: rule(n, divider=15, transformed="FizzBuzz"),
        lambda n: rule(n, divider=3, transformed="Fizz"),
        lambda n: rule(n, divider=5, transformed="Buzz")
    ]
    for r in rules:
        result = r(result)
    return result


def rule(param: str, divider, transformed) -> str:
    return transformed if param.isdigit() and int(param) % divider == 0 else param