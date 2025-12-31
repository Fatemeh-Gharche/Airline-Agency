from Flight import Flight

def read_input():
    M = int(input())

    MinPrice, MaxPrice = map(int, input().split())

    cities = input().split()

    stays_input = list(map(int, input().split()))
    stays = []
    for i in range(0, len(stays_input), 2):
        stays.append((stays_input[i], stays_input[i+1]))

    flights = []
    for _ in range(M):
        o, d, day, price = input().split()
        flights.append(Flight(o, d, int(day), int(price)))

    return MinPrice, MaxPrice, cities, stays, flights


def build_domains(cities, flights):
    num_vars = len(cities) - 1
    domains = [[] for _ in range(num_vars)]

    for i in range(num_vars):
        for f in flights:
            if f.origin == cities[i] and f.dest == cities[i+1]:
                domains[i].append(f)

    return domains
