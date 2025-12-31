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

    
    def is_consistent(self, var_index, flight):
        if var_index == 0:
            return True

        prev_flight = self.assignment[var_index - 1]
        min_stay, max_stay = self.stays[var_index - 1]

        diff = flight.day - prev_flight.day
        return min_stay <= diff <= max_stay

   