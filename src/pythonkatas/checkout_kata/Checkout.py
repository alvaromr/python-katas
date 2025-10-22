def discounted_price_rule(code, base_price, discount_amount, discount_per):
    def discounted_price_for(codes) -> int:
        scan_count = codes.count(code)
        total_base = base_price * scan_count
        discount = discount_amount * (scan_count // discount_per)
        return total_base - discount
    return discounted_price_for

class Checkout:
    def __init__(self, price_rules):
        self.total = 0
        self.price_rules = price_rules
        self.codes = list()

    def scan(self, code):
        self.codes.append(code)
        self.total = sum(f(self.codes) for f in self.price_rules)



