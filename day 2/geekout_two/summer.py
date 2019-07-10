import time
start = time.time()


def summer(list):
    sum = 0 if type(list[0]) is int else ""
    for word in list:
        sum += word
    print(sum)


summer([2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4,
        2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, ])

end = time.time()
print(end - start)
