def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        count += 1 if num == candidate else -1

    
    for num in nums:
        if num == candidate:
            count += 1

    return candidate if count > len(nums) // 2 else None

# Test case
nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(majority_element(nums))  
