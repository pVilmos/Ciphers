import sys, random, math

sys.path.insert(1, '../ciphers')
sys.path.insert(1, '../deciphers')

from affine_cipher import encrypt_message_affine
from affine_decipher import decrypt_message_affine, inverse_mod_add, inverse_mod_mult
from crypto_functions import is_relative_prime


CHARACHTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
LENGTH = len(CHARACHTERS)

#limit for the test text length
TEXT_LIMIT = 100

TEST_ROUNDS = 50

#Only for epicness
input("Start testing...")

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
    print(text)
    print(encrypt_message_affine(text, key_mult, key_add, CHARACHTERS, LENGTH))
    print(decrypt_message_affine(encrypt_message_affine(text, key_mult, key_add, CHARACHTERS, LENGTH), key_mult, key_add, CHARACHTERS, LENGTH))
    if decrypt_message_affine(encrypt_message_affine(text, key_mult, key_add, CHARACHTERS, LENGTH), key_mult, key_add, CHARACHTERS, LENGTH) == text:
        print(True)
    else:
        print(False)
