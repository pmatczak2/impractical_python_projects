
r"""Decrypt a Civil War 'rail fence' type cipher.
This is for a "2-rail" fence cipher for short messages
Example plaintext:  'Buy more Maine potatoes'
Rail fence style:  B Y O E A N P T T E
                    U M R M I E O A O S
Read zig-zag:      \/\/\/\/\/\/\/\/\/\/
Ciphertext:  BYOEA NPTTE UMRMI EOSOS
"""
import math
import itertools

#------------------------------------------------------------------------------
# USER INPUT:

# the string to be decrypted (paste between quotes):
ciphertext = """LTSRS OETEI EADET NETEH DOTER EEUCO SVRHR VRNRS UDRHS AEFHT ES
"""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#------------------------------------------------------------------------------

def main():
    """Run program to secrypt 2-rail fence cipher"""
    message = prep_cipgertext(ciphertext)
    row1, row2 = split_rails(message)
    decrypt(row1, row2)

def prep_cipgertext(ciphertext):
    """Remove whitespace."""
    message = "".join(ciphertext.split())
    print(f"\nciphertext = {ciphertext}")
    return message

def split_rails(message):
    """Split mesage in tow, always rounding UP for 1st row."""
    row_1_len = math.ceil(len(message)/2)
    row1 = (message[:row_1_len]).lower()
    row2 = (message[row_1_len:]).lower()
    return row1, row2

