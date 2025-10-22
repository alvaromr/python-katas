from pythonkatas.checkout_kata.Checkout import Checkout, PriceRule


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
    PriceRule("A", 50, 20, 3),
    PriceRule("B", 30, 15, 2),
    PriceRule("C", 20, 0, 1),
    PriceRule("D", 15, 0, 1),
]

def price(codes):
    checkout = Checkout(price_rules)
    for code in codes:
        checkout.scan(code)
    return checkout.total