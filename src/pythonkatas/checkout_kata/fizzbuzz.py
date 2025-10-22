def fizzbuzz(param):
    if param % 15 == 0:
        return "FizzBuzz"
    if param % 3 == 0:
        return "Fizz"
    if param % 5 == 0:
        return "Buzz"
    else:
        return str(param)