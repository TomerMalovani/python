def sum(nums, n):
    if n == len(nums):
        return 0
    return nums[n] + sum(nums, n+1)


print(sum([1, 2, 3, 4, 5], 0))
