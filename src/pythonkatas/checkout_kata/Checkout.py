def discounted_price_rule(code, base_price, discount_amount, discount_per):
    def discounted_price_for(codes) -> int:
        scan_count = codes.count(code)
        total_base = base_price * scan_count
        discount = discount_amount * (scan_count // discount_per)
        return total_base - discount
    return discounted_price_for

price_rules = [
    discounted_price_rule(code="A", base_price=50, discount_amount=20, discount_per=3),
    discounted_price_rule(code="B", base_price=30, discount_amount=15, discount_per=2),
    discounted_price_rule(code="C", base_price=20, discount_amount=0, discount_per=1),
    discounted_price_rule(code="D", base_price=15, discount_amount=0, discount_per=1),
]

class Checkout:
    def __init__(self):
        self.total = 0
        self.price_rules = price_rules
        self.codes = list()

    def scan(self, code):
        self.codes.append(code)
        self.total = sum(f(self.codes) for f in self.price_rules)



