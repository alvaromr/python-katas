def fizzbuzz(param):
    result = str(param)
    result = rule(param, result, divider=3, transformed="Fizz")
    result = rule(param, result, divider=5, transformed="Buzz")
    result = rule(param, result, divider=15, transformed="FizzBuzz")
    return result


def rule(param, n: str, divider, transformed) -> str:
    return transformed if param % divider == 0 else n