def fizzbuzz(param):
    result = str(param)
    result = rule_fizz(param, result)
    result = rule_buzz(param, result)
    result = rule_fizzbuzz(param, result)
    return result


def rule_fizzbuzz(param, result: str) -> str:
    return "FizzBuzz" if param % 15 == 0 else result


def rule_buzz(param, result: str):
    return "Buzz" if param % 5 == 0 else result


def rule_fizz(param, result):
    return "Fizz" if param % 3 == 0 else result