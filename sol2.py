def search_range(nums, target):
    def find_leftmost_index():
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] == target else -1

    def find_rightmost_index():
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        return left if nums[left] == target else -1

    left_index = find_leftmost_index()
    right_index = find_rightmost_index()

    return [left_index, right_index]

# Test case
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(search_range(nums, target))  

