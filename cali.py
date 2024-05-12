def calculate(s):
    stack = []
    num = 0
    sign = '+'
    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        if (not s[i].isdigit() and s[i] != ' ') or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] *= num
            elif sign == '/':
                stack[-1] = int(stack[-1] / num)
            sign = s[i]
            num = 0
    return sum(stack)
test_cases = ["3+2*2", " 3/2 ", " 3+5 / 2 ", "-1+5", "2+3+5"]
for s in test_cases:
    print(f"Input: s = \"{s}\"")
    print("Output:", calculate(s))