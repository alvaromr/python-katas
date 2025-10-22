def fizzbuzz(param):
    result = str(param)
    result = "Fizz" if param % 3 == 0 else result
    result = "Buzz" if param % 5 == 0 else result
    result = "FizzBuzz" if param % 15 == 0 else result
    return result
