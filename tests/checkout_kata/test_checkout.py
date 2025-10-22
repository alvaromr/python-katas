from pythonkatas.checkout_kata.Checkout import Checkout


def test_no_items() -> None:
    assert 0 == price("")


def test_scan_a() -> None:
    assert 50 == price("A")
    assert 100 == price("AA")
    assert 130 == price("AAA")
    assert 180 == price("AAAA")
    assert 230 == price("AAAAA")
    assert 260 == price("AAAAAA")


def price(codes):
    checkout = Checkout()
    for code in codes:
        checkout.scan(code)
    return checkout.total