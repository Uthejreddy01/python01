def findMinMaxSumDiff(elements, M, N):
    if len(elements) == 0 or M >= len(elements) or N >= len(elements):
        return None, None, None, None
    elements.sort()
    Mth_max = elements[-M - 1]
    Nth_min = elements[N - 1]
    Sum = Mth_max + Nth_min
    Diff = abs(Mth_max - Nth_min)
    return Mth_max, Nth_min, Sum, Diff
test_cases = [
    ([14, 16, 87, 36, 25, 89, 34], 1, 3),
    ([16, 16, 16, 16, 16], 0, 1),
    ([0, 0, 0, 0], 1, 2),
    ([-12, -78, -35, -42, -85], 3, 3),
    ([15, 19, 34, 56, 12], 6, 3),
    ([85, 45, 65, 75, 95], 5, 7)
]
for elements, M, N in test_cases:
    Mth_max, Nth_min, Sum, Diff = findMinMaxSumDiff(elements, M, N)
    if Mth_max is not None and Nth_min is not None and Sum is not None and Diff is not None:
        print(f"List of elements: {elements}")
        print(f"{M}th Maximum Number = {Mth_max}")
        print(f"{N}th Minimum Number = {Nth_min}")
        print(f"Sum = {Sum}")
        print(f"Difference = {Diff}")
        print()
    else:
        print("Invalid input or indices out of range.")