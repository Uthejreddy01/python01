def climbStairs(n):
    if n == 1:
        return 1
        dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
print(climbStairs(2))  # Output: 2
print(climbStairs(3))  # Output: 3
print(climbStairs(4))  # Output: 5
print(climbStairs(1))  # Output: 1
print(climbStairs(5))  # Output: 8