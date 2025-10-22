class Checkout:
    def __init__(self):
        self.total = 0

def test_no_items() -> None:
    checkout = Checkout()
    assert 0 == checkout.total