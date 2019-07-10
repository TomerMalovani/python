def Fibonacci(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    num = Fibonacci(x-1) + Fibonacci(x-2)
    return num


print(Fibonacci(6))
