class Flight:
    def __init__(self, origin, dest, day, price):
        self.origin = origin
        self.dest = dest
        self.day = day
        self.price = price

    def __str__(self):
        return f"{self.origin} {self.dest} {self.day} {self.price}"
