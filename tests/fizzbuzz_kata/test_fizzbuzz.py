from pythonkatas.checkout_kata.fizzbuzz import fizzbuzz


def test_one() -> None:
    assert fizzbuzz(1) == "1"

def test_two() -> None:
    assert fizzbuzz(2) == "2"