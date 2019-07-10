def max(list, x):
    if x == len(list):
        return 0
    y = max(list, x+1)
    if list[x] > y:
        return list[x]
    return y


print(max([1, 47, 2, 3, 45], 0))
