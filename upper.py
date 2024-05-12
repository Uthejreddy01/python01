def countCharacters():
    uppercase_count = 0
    lowercase_count = 0
    number_count = 0
    print("Enter * to exit...")
    while True:
        char = input("Enter any character: ")
        if char == '*':
            break
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            number_count += 1
    print(f"Total count of lowercase: {lowercase_count}")
    print(f"Total count of uppercase: {uppercase_count}")
    print(f"Total count of numbers: {number_count}")
countCharacters()