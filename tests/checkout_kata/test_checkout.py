from pythonkatas.checkout_kata.Checkout import Checkout


def test_no_items() -> None:
    checkout = Checkout()
    assert 0 == checkout.total

def test_scan_one_a() -> None:
    checkout = Checkout()
    checkout.scan('A')
    assert 50 == checkout.total

def test_scan_two_a() -> None:
    checkout = Checkout()
    checkout.scan('A')
    checkout.scan('A')
    assert 100 == checkout.total

def test_scan_three_a() -> None:
    checkout = Checkout()
    checkout.scan('A')
    checkout.scan('A')
    checkout.scan('A')
    assert 130 == checkout.total
