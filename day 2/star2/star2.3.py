
def get_last(tuple):
    return tuple[-1]


def sort_last(tuples):

    tuples.sort(key=get_last)
    print(tuples)


given_list = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
sort_last(given_list)
