def piglatin(word):
    vowels = list("aeiou")
    constants = list("BCDFGHJKLMNPQRSTVWXYZ")

    if word[0] in vowels:
        word = word + "ay"
    else:
        for counter, letter in enumerate(list(word)):
            if letter in vowels:
                word = word[counter:] + word[:counter] + "ay"
                break
    return word


print(piglatin("atr"))
print(piglatin("together"))