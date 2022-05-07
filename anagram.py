# import load_dictionary
#
# word_list = load_dictionary.load('2of4brif.txt')
# anagrams = []
#
# # a word thats made up from letters form another word. exp(post, stop)
# for word in word_list:
#     if word == word_list and

words = ["post", "sopt", "xyz"]

palindrome = True
for word in words:
    if list(word).sort() == list(words[1]).sort():
        continue
    palindrome = False
    break
if palindrome:
    print("got one")