class Checkout:
    def __init__(self):
        self.total = 0

    def scan(self, code):
        self.total += 50
        if self.total == 150:
            self.total -= 20
