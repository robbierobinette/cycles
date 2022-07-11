import math

def cycles(n: int):
    outcomes = math.pow(2, (n * (n - 1)) / 2)
    orderings = math.factorial(n)
    return outcomes - orderings

for n in range(3,11):
    outcomes = math.pow(2, (n * (n - 1)) / 2)
    orderings = math.factorial(n)
    sub_cycles = n * cycles(n - 1)
    non_top_cycles = orderings + sub_cycles

    print("N %2d outcomes %15d orderings %10d percentage %9.6f%%  sub_cycles %14d non-top percentage %9.6f%%" %
          (n, outcomes, orderings, 100 * orderings / outcomes, non_top_cycles, (100 * (non_top_cycles / outcomes))))
