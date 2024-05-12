def numSquares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case: 0 requires 0 perfect squares
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    return dp[n]
test_cases = [12, 13, 1, 4, 3]
for n in test_cases:
    print(f"Input: n = {n}")
    print("Output:", numSquares(n))