"""Decrypt a path through a Union Route Cipher.


Designed for whole-word transposition ciphers with variable rows & columns.
Assumes encryption began at either top or bottom of a column.
Key indicates the order to read columns and the direction to traverse.
Negative column numbers mean start at bottom and read up.
Positive column numbers means start at top & read down.
Example below is for 4x4 matrix with key -1 2 -3 4.
Note "0" is not allowed.
Arrows show encryption route; for negative key values read UP.
  1   2   3   4
 ___ ___ ___ ___
| ^ | | | ^ | | | MESSAGE IS WRITTEN
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | ACROSS EACH ROW
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | IN THIS MANNER
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | LAST ROW IS FILLED WITH DUMMY WORDS
|_|_|_v_|_|_|_v_|
START        END
Required inputs - a text message, # of columns, # of rows, key string
Prints translated plaintext
"""

import sys

#=======================================================================================================================
# USER INPUT:

# the sring to ve decrypted (type or paste between triple-quotes):
ciphertext = """16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"""

# Number of colums in the transposition matrix:
COLS = 4

# number of rows in the transpositin matric:
ROWS = 5

# Key with spaces between numbers; negative to read UP colum (ex = -1 2 -3 4):
key = """ -1 2 -3 4 """

# END OF USER INPUT - DO NOT EDIT VELOW THIS LINE!
#=======================================================================================================================





def main():
    """Run program in print decrypted plaintext."""
    print(f"\nCiphertext {ciphertext}")
    print(f"\nTrying {COLS} columns")
    print(f"\nTrying {ROWS} rows")
    print(f"\nTrying {key} key")

    # split elements into words, not letters
    cipherlist = list(ciphertext.split())
    validate_col_row(cipherlist)
    key_int = key_to_int(key)
    translation_matrix = build_matrix(key_int, cipherlist)
    plaintext = decrypt(translation_matrix)

    print(f"Plaintext {plaintext}")

def validate_col_row(cipherlist):
    """Check that input columns & rows are valid vs. message length."""
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher):  # range exclude 1-column ciphers
        if len_cipher % i == 0:
            factors.append(i)
    print(f"\nLength of cipher = {len_cipher}")
    print(f"Acceptable column/row values include: {factors}")
    print()
    if ROWS * COLS != len_cipher:
        print("\nError - Input columns & rows ont factors of length "
              "of cipher. Terminating program.", file=sys.stderr)
        sys.exit(1)

def key_to_int(key):
    """Turn lwy into list of integers & check validity"""
    key_int = [int(i) for i in key.split()]
    key_int_lo = min(key_int)
    key_int_hi = max(key_int)
    if len(key_int) != COLS or key_int_lo < -COLS or key_int_hi > COLS or 0 in key_int_hi:
        print("\nError - Problem with key. Terminating.", file=sys.stderr)
        sys.exit(1)
    else:
        return key_int