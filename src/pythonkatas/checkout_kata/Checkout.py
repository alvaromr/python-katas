class Checkout:
    def __init__(self):
        self.total = 0
        self.codes = list()

    def scan(self, code):
        self.codes.append(code)
        self.total = 0

        scan_count = self.codes.count("A")
        base_price = 50 * scan_count
        discount = 20 * (scan_count // 3)
        self.total += base_price - discount

        scan_count = self.codes.count("B")
        base_price = 30 * scan_count
        discount = 15 * (scan_count // 2)
        self.total += base_price - discount
