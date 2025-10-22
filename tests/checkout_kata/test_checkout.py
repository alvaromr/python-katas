from pythonkatas.checkout_kata.Checkout import Checkout


def test_no_items() -> None:
    checkout = Checkout()
    assert 0 == checkout.total