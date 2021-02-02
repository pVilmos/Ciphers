import sys, random, math

sys.path.insert(1, '../ciphers')
sys.path.insert(1, '../deciphers')

from vigenere_cipher import encrypt_message_vigenere
from vigenere_decipher import decrypt_message_vigenere


CHARACHTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
LENGTH = len(CHARACHTERS)

#limit for the test text length
TEXT_LIMIT = 100

TEST_ROUNDS = 50

WORD_LIMIT = 20
#Only for epicness
input("Start testing...")

for i in range(0, TEST_ROUNDS):

    text = ""
    word = ""

    #generate random text length
    text_length = math.ceil(TEXT_LIMIT*random.random())

    #generate random word length
    word_length = math.ceil(WORD_LIMIT*random.random())

    #generate random text
    for j in range(0, text_length):
        pos = math.floor(LENGTH*random.random())
        text += CHARACHTERS[pos]

    #generate random text
    for j in range(0, word_length):
        pos = math.floor(LENGTH*random.random())
        word += CHARACHTERS[pos]


    #Test
    if decrypt_message_vigenere(encrypt_message_vigenere(text, word), word) == text:
        print(True)
    else:
        print(False)
