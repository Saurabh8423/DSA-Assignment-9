def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        sum_two = numbers[left] + numbers[right]

        if sum_two == target:
            return [left + 1, right + 1]  # Adjusting for 1-based indexing

        if sum_two < target:
            left += 1
        else:
            right -= 1

    # If no solution is found, return an empty list or raise an exception.
    return []

# Test case
numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))  
