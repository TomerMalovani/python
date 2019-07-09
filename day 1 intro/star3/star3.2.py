def both_ends(s):
    if len(s) < 2:
        return " "
    e = (s[0:2] + s[-2::])
    return e


print(both_ends("r"))
