quote, VOWELS = "some people drink from the fountain of knowledge, others just gargle.", "aeiou"
list = []
for counter, char in enumerate(quote):
    if char in VOWELS:
        list.append(counter)
print(list)
