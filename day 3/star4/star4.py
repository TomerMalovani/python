def Palindrome(word):
    x = False
    n = len(word)
    if n == 1:
        x = True
    if word[0] == word[n-1]:
        x = Palindrome(word[1:n-1])
    return x


print(Palindrome("16311"))
