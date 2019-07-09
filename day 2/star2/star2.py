def match_ends(words):
    count = 0
    for word in words:
        if len(word) > 2 and word[0] == word[-1]:
            count += 1
    print(count)


given_list = ["wow", "eye", "goag", "47", "yy"]
match_ends(given_list)
