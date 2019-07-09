def check_sum(given_list):
    sum = 0
    for number in given_list:
        print(type(number))
        if type(number) is int:
            sum += number
    print(sum)


da_list = ["tomer", 31, "47", 16]
check_sum(da_list)

