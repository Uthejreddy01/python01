from math import comb
def generate_pascal_triangle(rows):
    triangle = [[comb(i, j) for j in range(i + 1)] for i in range(rows)]
    return triangle
def sum_elements_in_row(triangle, row_num):
    row_sum = sum(triangle[row_num])
    return row_sum
rows = int(input("Enter the number of rows: "))
row_num = int(input("Enter the row number: "))
pascal_triangle = generate_pascal_triangle(rows)
for row in pascal_triangle:
    print(" ".join(map(str, row)).center(80))
row_sum = sum_elements_in_row(pascal_triangle, row_num)
print(f"\nSum of elements in {row_num}th row: {row_sum}")