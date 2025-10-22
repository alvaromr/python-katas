class Checkout:
    def __init__(self):
        self.total = 0
        self.codes = list()

    def scan(self, code):
        self.codes.append(code)
        self.total = 0

        a_price = self.price_a(code="A", base_price=50, discount_amount=20, discount_per=3)
        self.total += a_price

        a_price = self.price_a(code="B", base_price=30, discount_amount=15, discount_per=2)
        self.total += a_price

    def price_a(self, code, base_price, discount_amount, discount_per) -> int:
        scan_count = self.codes.count(code)
        base_price = base_price * scan_count
        discount = discount_amount * (scan_count // discount_per)
        return base_price - discount
