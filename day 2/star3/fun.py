# def hey():
#     print("hey please type your name")
#     name = input("name: ")
#     print(f"hey {name} what is your favorite number?")
#     number = input("number: ")
#     if number == "47":
#         print("good")
#     else:
#         print("bad")


# hey()

def fact(x, n):

    if n == 0:
        return 1
    return x*fact(x, n-1)


print(fact(4, 2))
