ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"



# split elements into words, not letters
chiperlist = list(ciphertext.split())

# initialize variables
COLS = 4
ROWS = 5
key = '-1 2 -3 4'  # neg number means read UP column vs. DOWN
translation_matrix = [None] * COLS
plaintext = ''
start = 0
stop = ROWS

# Turn key_int into list of integers:
key_int = [int(i) for i in key.split()]

# turn columns into items in list of lists:
for k in key_int:
    if k < 0:  # reading bottom-to-top of column
        col_items = chiperlist[start:stop]
    elif k > 0:  # reading top-to-bottom of column
        col_items = list((reversed(chiperlist[start:stop]))) # why is this a list?
    translation_matrix[abs(k) - 1] = col_items
    start += ROWS
    stop += ROWS

print(f"\nchiphertext = {ciphertext}")
print(f"\ntranslation =", *translation_matrix, sep="\n")
print(f"\nkey length = {len(key_int)}")

# loop through nested lists popping off last item to new list:
for i in range(ROWS):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plaintext += word + ' '

print(f"plaintext = {plaintext}")

""""""