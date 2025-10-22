class Checkout:
    def __init__(self):
        self.total = 0
        self.codes = list()

    def scan(self, code):
        self.codes.append(code)
        self.total = 0

        a_price = self.price_a("A")
        self.total += a_price

        a_price = self.price_b("B")
        self.total += a_price

    def price_b(self, code) -> int:
        scan_count = self.codes.count(code)
        base_price = 30 * scan_count
        discount = 15 * (scan_count // 2)
        return base_price - discount

    def price_a(self, code) -> int:
        scan_count = self.codes.count(code)
        base_price = 50 * scan_count
        discount = 20 * (scan_count // 3)
        return base_price - discount
