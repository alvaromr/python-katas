def fizzbuzz(param):
    if param % 3 == 0:
        return "Fizz"
    if param % 5 == 0:
        return "Buzz"
    else:
        return str(param)