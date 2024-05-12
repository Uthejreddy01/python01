def addBinary(a, b):
    carry = 0
    result = []
    i, j = len(a) - 1, len(b) - 1
    while i >= 0 or j >= 0:
        sum_bits = carry
        if i >= 0:
            sum_bits += ord(a[i]) - 48
            i -= 1
        if j >= 0:
            sum_bits += ord(b[j]) - 48
            j -= 1
        result.append(str(sum_bits % 2))
        carry = sum_bits // 2
    if carry:
        result.append(str(carry))
    return ''.join(result[::-1])
test_cases = [("11", "1"), ("1010", "1011"), ("1111", "1010"), ("101101", "1100"), ("1011", "1111")]
for a, b in test_cases:
    print(f"Input: a = \"{a}\", b = \"{b}\"")
    print("Output:", addBinary(a, b))