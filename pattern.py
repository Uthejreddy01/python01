def print_pattern(starting_number, max_lines):
    if max_lines <= 0:
        print("Max number of lines should be greater than 0.")
        return
  
    current_number = starting_number
    for i in range(1, max_lines + 1):
        line = ""
        for j in range(i):
            line += f"{current_number:.1f} "
            current_number += 0.1
        print(line.strip())
starting_number = float(input("Enter the starting number: "))
max_lines = int(input("Max number of lines printed: "))
print_pattern(starting_number, max_lines)