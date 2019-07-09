def linear_merge(list1, list2):
    temp_list = (list1[:]+list2[:])
    temp_list.sort()
    print(temp_list)


linear_merge([2, 3, 4, 5], [1, 7, 8, 9])
