def remove_adjacent(nums):
    next_to, temp_list = "", nums[:]
    for num in nums:
        if num == next_to:
            temp_index = temp_list.index(num)
            temp_list.pop(temp_index)
        else:
            next_to = num
    nums = temp_list[:]
    print(nums)


given_list = [1, 2, 2, 3, 3, 1, 2, 4, 7, 7]
remove_adjacent(given_list)
