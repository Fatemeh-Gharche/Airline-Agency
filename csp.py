class CSPSolver:
    def __init__(self, domains, stays, min_price, max_price):
        self.domains = domains
        self.stays = stays
        self.min_price = min_price
        self.max_price = max_price

        self.num_vars = len(domains)
        self.assignment = [None] * self.num_vars

        self.backtracks = 0
        self.start_time = None
        self.end_time = None

