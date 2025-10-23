from pythonkatas.checkout_kata.fizzbuzz import fizzbuzz


def test_number() -> None:
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(4) == "4"

def test_fizz() -> None:
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(13) == "Fizz"

def test_buzz() -> None:
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(52) == "Buzz"

def test_fizzbuzz() -> None:
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(51) == "FizzBuzz"

def test_wozz():
    assert fizzbuzz(7) == "Wozz"
    assert fizzbuzz(71) == "Wozz"

def test_buzzwozz():
    assert fizzbuzz(70) == "BuzzWozz"
    assert fizzbuzz(140) == "BuzzWozz"

def test_fizzbuzzwozz():
    assert fizzbuzz(75) == "FizzBuzzWozz"
    assert fizzbuzz(375) == "FizzBuzzWozz"