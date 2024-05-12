def max_area(height):
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
print(max_area([1, 5, 4, 3]))  # Output: 6
print(max_area([3, 1, 2, 4, 5]))  # Output: 12
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Output: 49
print(max_area([1, 1]))  # Output: 1
print(max_area([7, 3]))  # Output: 3