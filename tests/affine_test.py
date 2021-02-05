import sys, random, math

sys.path.insert(1, '../ciphers')
sys.path.insert(1, '../deciphers')

from affine_cipher import encrypt_message_affine
from affine_decipher import decrypt_message_affine, inverse_mod_add, inverse_mod_mult
from constants import CHARACHTERS, LENGTH, TEXT_LIMIT, TEST_ROUNDS

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def is_relative_prime(length, key):
    if gcd(length, key) == 1:
        return True
    else:
        return False

for i in range(0, TEST_ROUNDS):

    text = ""

    #generate random text length
    text_length = math.ceil(TEXT_LIMIT*random.random())

    #generate random text
    for j in range(0, text_length):
        pos = math.floor(LENGTH*random.random())
        text += CHARACHTERS[pos]

    #generate keys for the cipher
    while True:
        key_mult = math.floor(LENGTH*random.random())
        if is_relative_prime(key_mult, LENGTH):
            break

    key_add = math.floor(LENGTH*random.random())

    #Test
    if decrypt_message_affine(encrypt_message_affine(text, key_mult, key_add, CHARACHTERS, LENGTH), key_mult, key_add, CHARACHTERS, LENGTH) == text:
        print(True)
    else:
        print(False)
