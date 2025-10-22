def fizzbuzz(param):
    result = str(param)
    result = rule_fizz(param, result, divider=3, transformed="Fizz")
    result = rule_buzz(param, result, divider=5, transformed="Buzz")
    result = rule_fizzbuzz(param, result, divider=15, transformed="FizzBuzz")
    return result


def rule_fizzbuzz(param, n: str, divider, transformed) -> str:
    return transformed if param % divider == 0 else n


def rule_buzz(param, n: str, divider, transformed):
    return transformed if param % divider == 0 else n


def rule_fizz(param, n, divider, transformed):
    return transformed if param % divider == 0 else n