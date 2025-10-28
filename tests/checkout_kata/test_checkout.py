from pythonkatas.checkout_kata.Checkout import Checkout, PriceRule, build_price_rules


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
    PriceRule(code="A", base_price=50, discount_amount=20,discount_per= 3),
    PriceRule(code="B", base_price=30, discount_amount=15,discount_per= 2),
    PriceRule(code="C", base_price=20, discount_amount=0, discount_per=1),
    PriceRule(code="D", base_price=15, discount_amount=0, discount_per=1),
]

def test_build_price_rules():
    assert build_price_rules('') == []
    assert build_price_rules('A costs 50 and you get 3 for 130\nB is 30 but you can get 15 discount for the second\nC costs 20\nDcosts 15') == price_rules
    assert build_price_rules('A costs 50, but if you buy 3 you save 20\nB costs 30, but the second one has a 15 discount\nC costs 20\nD costs 15') == price_rules
    assert build_price_rules('A costs 50, but if you buy 3 you save 40% in the last item\nB costs 30, but the second one has a 15 discount\nC costs 20\nD costs C minus 5') == price_rules
    assert build_price_rules(
"""
Item   Unit      Special
       Price     Price
--------------------------
  A     50       3 for 130
  B     30       2 for 45
  C     20
  D     15
"""
    ) == price_rules

def price(codes):
    checkout = Checkout(price_rules)
    for code in codes:
        checkout.scan(code)
    return checkout.total