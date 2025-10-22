from pythonkatas.checkout_kata.fizzbuzz import fizzbuzz


def test_number() -> None:
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(4) == "4"

def test_three() -> None:
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(13) == "Fizz"

def test_five() -> None:
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(52) == "Buzz"

def test_fifteen() -> None:
    assert fizzbuzz(15) == "FizzBuzz"