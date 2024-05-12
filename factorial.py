import math
def factorial(n):
    return math.factorial(n)
def count_factors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count
test_cases = [6,0, -5, 1, 20, 3]
for n in test_cases:
    if n < 0:
        print(f"Invalid input: {n}")
    else:
        print(f"{n} Factorial: {factorial(n)}")
        print(f"Number of factors for {n}: {count_factors(n)}")