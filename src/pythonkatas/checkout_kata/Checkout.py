
fs = [
    lambda codes: discounted_price_for(codes, code="A", base_price=50, discount_amount=20, discount_per=3),
    lambda codes: discounted_price_for(codes, code="B", base_price=30, discount_amount=15, discount_per=2),
    lambda codes: discounted_price_for(codes, code="C", base_price=20, discount_amount=0, discount_per=1),
    lambda codes: discounted_price_for(codes, code="D", base_price=15, discount_amount=0, discount_per=1),
]

class Checkout:
    def __init__(self):
        self.total = 0
        self.codes = list()

    def scan(self, code):
        self.codes.append(code)
        self.total = sum(f(self.codes) for f in fs)


def discounted_price_for(codes, code, base_price, discount_amount, discount_per) -> int:
    scan_count = codes.count(code)
    base_price = base_price * scan_count
    discount = discount_amount * (scan_count // discount_per)
    return base_price - discount
