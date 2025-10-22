from pythonkatas.checkout_kata.Checkout import Checkout


def test_no_items() -> None:
    assert 0 == price("")


def test_scan_one_a() -> None:
    assert 50 == price("A")


def test_scan_two_a() -> None:
    assert 100 == price("AA")


def test_scan_three_a() -> None:
    assert 130 == price("AAA")


def price(codes):
    checkout = Checkout()
    for code in codes:
        checkout.scan(code)
    return checkout.total