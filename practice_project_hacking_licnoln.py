ciphertext = """THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT WHY AND IF FILLS IT YOU GET THEY NEPTUNE THE 
TRIBUNE PLEASE ARE THEM CAN UP"""


COLS = 4

ROWS = 6

key = """-1 2 -3 4 """

def main():
    # split elements into words, not letters
    cipherlist = list(ciphertext.split())
    validate_col_row(cipherlist)
    key_int = key_to_int(key)
    translation_matrix = build_matrix(key_int, cipherlist)
    plaintext = decrypt(translation_matrix)

    print(ciphertext)
    print(f"\nPlaintext {plaintext}\n")
    print(*build_matrix(key_int, cipherlist), sep="\n")


def validate_col_row(cipherlist):
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher):
        if len_cipher % i == 0:
            factors.append(i)
    if ROWS * COLS != len_cipher:
        print("\nError - Input colum & rows not factors of length of cipher!")

def key_to_int(key):
    key_int = [int(i) for i in key.split()]
    key_int_lo = min(key_int)
    key_int_hi = max(key_int)
    if len(key_int) != COLS or key_int_lo < -COLS or key_int_hi > COLS or 0 in key_int:
        print("\nError")
    else:
        return key_int

def build_matrix(key_int, cipherlist):
    """Turn every n items in a list into a new item in a list of lists."""
    translation_matrix = [None] * COLS
    start = 0
    stop = ROWS
    for k in key_int:
        if k < 0:  # read bottom-to-top of column
            col_items = cipherlist[start:stop]
        elif k > 0:  # read top-to-bottom of columnn
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[abs(k) - 1] = col_items
        start += ROWS
        stop += ROWS
    return translation_matrix

def decrypt(translation_matrix):
    """Loop through nested lists popping off last item to a string."""
    plaintext = ''
    for i in range(ROWS):
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            plaintext += word + ' '
    return plaintext

if __name__ == "__main__":
    main()