import sys, random, math

sys.path.insert(1, '../ciphers')
sys.path.insert(1, '../deciphers')

from substitution_cipher import encrypt_message_substitution, generate_encryption_table
from substitution_decipher import decrypt_message_substitution

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
        pos = math.ceil(LENGTH*random.random())-1
        text += CHARACHTERS[pos]

    #generate new alphabet for the cipher
    enc_alphabet = generate_encryption_table(CHARACHTERS)

    #Test
    if decrypt_message_substitution(encrypt_message_substitution(text, CHARACHTERS, enc_alphabet), enc_alphabet, CHARACHTERS) == text:
        print(True)
    else:
        print(False)