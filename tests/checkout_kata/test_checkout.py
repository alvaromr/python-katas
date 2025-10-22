from pythonkatas.checkout_kata.Checkout import Checkout, discounted_price_rule


def test_no_items() -> None:
    assert 0 == price("")


def test_scan_a() -> None:
    assert 50 == price("A")
    assert 100 == price("AA")
    assert 130 == price("AAA")
    assert 180 == price("AAAA")
    assert 230 == price("AAAAA")
    assert 260 == price("AAAAAA")


def test_scan_b() -> None:
    assert 30 == price("B")
    assert 45 == price("BB")
    assert 75 == price("BBB")


def test_scan_c() -> None:
    assert 20 == price("C")
    assert 40 == price("CC")
    assert 60 == price("CCC")

def test_scan_d() -> None:
    assert 15 == price("D")
    assert 30 == price("DD")
    assert 45 == price("DDD")

def test_totals():
    assert   0 == price("")
    assert  50 == price("A")
    assert  80 == price("AB")
    assert 115 == price("CDBA")

    assert 100 == price("AA")
    assert 130 == price("AAA")
    assert 180 == price("AAAA")
    assert 230 == price("AAAAA")
    assert 260 == price("AAAAAA")

    assert 160 == price("AAAB")
    assert 175 == price("AAABB")
    assert 190 == price("AAABBD")
    assert 190 == price("DABABA")

price_rules = [
    discounted_price_rule(code="A", base_price=50, discount_amount=20, discount_per=3),
    discounted_price_rule(code="B", base_price=30, discount_amount=15, discount_per=2),
    discounted_price_rule(code="C", base_price=20, discount_amount=0, discount_per=1),
    discounted_price_rule(code="D", base_price=15, discount_amount=0, discount_per=1),
]

def price(codes):
    checkout = Checkout(price_rules)
    for code in codes:
        checkout.scan(code)
    return checkout.total