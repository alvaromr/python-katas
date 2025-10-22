def fizzbuzz(param):
    result = str(param)
    if param % 3 == 0:
        result = "Fizz"
    if param % 5 == 0:
        result = "Buzz"
    if param % 15 == 0:
        result = "FizzBuzz"
    return result