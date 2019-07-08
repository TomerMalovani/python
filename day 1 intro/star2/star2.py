sum = 0
print("type a five digit number please")
number = input()
print("you wrote " + str(number))
for e in range(len(number)):
    print(number[e], end=",")
    sum += int(number[e])

print(" ")
print("this is the sum: ", end=str(sum))
