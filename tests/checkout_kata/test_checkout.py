class Checkout:
    pass


def test_no_items() -> None:
    checkout = Checkout()
    assert 0 == checkout.total