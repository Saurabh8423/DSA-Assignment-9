def count_inversions(nums):
    def merge_and_count(left, right):
        merged = []
        count = 0
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                count += len(left) - i

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, count

    if len(nums) <= 1:
        return nums, 0

    mid = len(nums) // 2
    left_half, left_count = count_inversions(nums[:mid])
    right_half, right_count = count_inversions(nums[mid:])
    merged_nums, merge_count = merge_and_count(left_half, right_half)

    return merged_nums, left_count + right_count + merge_count

# Test case
arr = [2, 4, 1, 3, 5]
print(count_inversions(arr)[1])  
