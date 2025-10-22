class Checkout:
    def __init__(self):
        self.total = 0
        self.scan_count = 0
        self.codes = list()

    def scan(self, code):
        self.codes.append(code)
        self.scan_count = self.codes.count(code)
        base_price = 50 * self.scan_count
        discount = 20 * (self.scan_count // 3)
        self.total = base_price - discount
