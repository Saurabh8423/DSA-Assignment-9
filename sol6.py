def isBadVersion(version):
    return version >= 4
def first_bad_version(n):
    left, right = 1, n

    while left < right:
        mid = left + (right - left) // 2

        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left

# Given input
n = 5

# Function call
result = first_bad_version(n)

# Output
print(result)  
