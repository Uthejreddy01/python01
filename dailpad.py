def letterCombinations(digits):
    if not digits:
        return []
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    def backtrack(combination, next_digits):
        if not next_digits:
            result.append(combination)
        else:
            for letter in mapping[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])
    result = []
    backtrack('', digits)
    return result
test_cases = ["23", "", "2", "9", "87"]
for digits in test_cases:
    print(f"Input: digits = \"{digits}\"")
    print("Output:", letterCombinations(digits))