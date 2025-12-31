from input import read_input, build_domains
from csp import CSPSolver

def main():
    MinPrice, MaxPrice, cities, stays, flights = read_input()
    domains = build_domains(cities, flights)

    solver = CSPSolver(domains, stays, MinPrice, MaxPrice)
    success = solver.solve()

    if not success:
        print("No Solution")
        return

    total = 0
    for f in solver.assignment:
        print(f)
        total += f.price

    print(f"Total Cost: {total}")
    print(f"Backtracks: {solver.backtracks}")
    print(f"Time: {solver.end_time - solver.start_time:.4f} seconds")

if __name__ == "__main__":
    main()