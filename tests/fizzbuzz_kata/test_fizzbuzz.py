import pytest

from pythonkatas.fizzbuzz_kata.fizzbuzz import fizzbuzz


@pytest.mark.parametrize("number", [1, 2, 4])
def test_number(number) -> None:
    assert fizzbuzz(number) == str(number)

@pytest.mark.parametrize("number", [3, 6, 9, 13, 23, 31])
def test_fizz(number) -> None:
    assert fizzbuzz(number) == "Fizz"

@pytest.mark.parametrize("number", [5, 10, 52])
def test_buzz(number) -> None:
    assert fizzbuzz(number) == "Buzz"

@pytest.mark.parametrize("number", [15, 51])
def test_fizzbuzz(number) -> None:
    assert fizzbuzz(number) == "FizzBuzz"

@pytest.mark.parametrize("number", [7, 71])
def test_wozz(number):
    assert fizzbuzz(number) == "Wozz"

@pytest.mark.parametrize("number", [70, 140])
def test_buzzwozz(number):
    assert fizzbuzz(number) == "BuzzWozz"

@pytest.mark.parametrize("number", [75, 375])
def test_fizzbuzzwozz(number):
    assert fizzbuzz(number) == "FizzBuzzWozz"