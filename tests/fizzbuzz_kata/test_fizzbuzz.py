from pythonkatas.checkout_kata.fizzbuzz import fizzbuzz


def test_one() -> None:
    assert fizzbuzz(1) == "1"

def test_two() -> None:
    assert fizzbuzz(2) == "2"

def test_three() -> None:
    assert fizzbuzz(3) == "Fizz"

def test_four() -> None:
    assert fizzbuzz(4) == "4"

def test_five() -> None:
    assert fizzbuzz(5) == "Buzz"