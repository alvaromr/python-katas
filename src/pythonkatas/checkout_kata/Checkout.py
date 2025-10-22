class Checkout:
    def __init__(self):
        self.total = 0
        self.scan_count = 0

    def scan(self, code):
        self.scan_count += 1
        self.total = 50 * self.scan_count - 20 * (self.scan_count // 3)
