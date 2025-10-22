def fizzbuzz(param):
    result = str(param)

    rules = [
        lambda n: division_rule(n, divider=15, transformed="FizzBuzz"),
        lambda n: division_rule(n, divider=3, transformed="Fizz"),
        lambda n: division_rule(n, divider=5, transformed="Buzz"),
        lambda n: digit_rule(n, digit=3, transformed="Fizz")
    ]
    for rule in rules:
        result = rule(result)
    return result


def division_rule(param: str, divider, transformed) -> str:
    return transformed if param.isdigit() and int(param) % divider == 0 else param

def digit_rule(param: str, digit, transformed) -> str:
    return transformed if param.isdigit() and str(digit) in param else param