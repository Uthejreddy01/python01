def isMirrorNumber(num_str):
    # Remove non-digit characters from the input string
    num_str = ''.join(filter(str.isdigit, num_str))
    reversed_num_str = num_str[::-1]
    if num_str == reversed_num_str:
        return True
    else:
        return False
test_cases = [
    "Sell123",
    "5489236",
    "Abc-abc",
    "%$$$$^&",
    "-123456"
]
for num_str in test_cases:
    if isMirrorNumber(num_str):
        print(f"The number '{num_str}' can be reversed to a mirror number.")
    else:
        print(f"The number '{num_str}' cannot be reversed to a mirror number.")