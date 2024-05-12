def countSortedVowelStrings(n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    dp = [[0] * 5 for _ in range(n)]
    for i in range(5):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(5):
            dp[i][j] = sum(dp[i - 1][:j + 1])
    return sum(dp[-1])
test_cases = [1, 2, 33, -5, 10]
for n in test_cases:
    print(f"n = {n}, Output: {countSortedVowelStrings(n)}")