import copy

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
    
    def forward_checking(self, var_index, flight, domains):
        if var_index == self.num_vars - 1:
            return True

        min_stay, max_stay = self.stays[var_index]
        next_domain = domains[var_index + 1]

        filtered_domain = []
        for f in next_domain:
            diff = f.day - flight.day
            if min_stay <= diff <= max_stay:
                filtered_domain.append(f)

        if not filtered_domain:
            return False  

        domains[var_index + 1] = filtered_domain
        return True

    def total_cost(self):
        return sum(f.price for f in self.assignment if f)

    def backtracking_search(self, var_index, domains):
        if var_index == self.num_vars:
            total = self.total_cost()
            return self.min_price <= total <= self.max_price

        for flight in domains[var_index]:
            if self.is_consistent(var_index, flight):
                self.assignment[var_index] = flight

                new_domains = copy.deepcopy(domains)

                if self.forward_checking(var_index, flight, new_domains):
                    if self.backtracking_search(var_index + 1, new_domains):
                        return True

                self.assignment[var_index] = None
                self.backtracks += 1

        return False