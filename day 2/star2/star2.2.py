def front_x(words):
    words_temp = words[:]
    for word in words:
        if not(word.startswith("x")):
            words_temp.remove(word)
            words_temp.append(word)
    words = words_temp[:]
    print(words)


given_list = ["disisit", "hey", "yo", "google", "x_47", "xtrans"]
front_x(given_list)
