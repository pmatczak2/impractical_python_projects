word_list = ["the", "a", "is", "forever", "i", "b", "x", "y", "thing"]
clean_word_list = []

premissible = ("a", "i")

for word in word_list:
    if len(word) > 1:
        clean_word_list.append(word)
    elif len(word) == 1 and word in premissible:
        clean_word_list.append(word)
    else:
        continue

print(f"{clean_word_list}")
