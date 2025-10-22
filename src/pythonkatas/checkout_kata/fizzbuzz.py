def fizzbuzz(param):
    result = str(param)
    result = rule(result, divider=15, transformed="FizzBuzz")
    result = rule(result, divider=3, transformed="Fizz")
    result = rule(result, divider=5, transformed="Buzz")
    return result


def rule(param: str, divider, transformed) -> str:
    return transformed if param.isdigit() and int(param) % divider == 0 else param