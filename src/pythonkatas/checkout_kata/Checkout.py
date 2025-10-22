class PriceRule:
    def __init__(self, code, base_price, discount_amount, discount_per):
        self.code = code
        self.base_price = base_price
        self.discount_amount = discount_amount
        self.discount_per = discount_per

    def apply(self, codes) -> int:
        scan_count = codes.count(self.code)
        total_base = self.base_price * scan_count
        discount = self.discount_amount * (scan_count // self.discount_per)
        return total_base - discount


class Checkout:
    def __init__(self, price_rules):
        self.total = 0
        self.price_rules = price_rules
        self.codes = list()

    def scan(self, code):
        self.codes.append(code)
        self.total = sum(rule.apply(self.codes) for rule in self.price_rules)



