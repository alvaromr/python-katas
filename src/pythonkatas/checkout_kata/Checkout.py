class Checkout:
    def __init__(self):
        self.total = 0
        self.scan_count = 0

    def scan(self, code):
        self.scan_count += 1
        base_price = 50 * self.scan_count
        discount = 20 * (self.scan_count // 3)
        self.total = base_price - discount
