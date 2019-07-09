quote = "some people drink from the fountain of knowledge, others just gargle."
VOWELS = "aeiou"
list = []
for counter, char in enumerate(quote):
    if char in VOWELS:
        list.append(counter)

print(list)
