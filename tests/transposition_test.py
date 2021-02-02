import sys, random, math

#adding ciphers and deciphers directorys to the default path

sys.path.insert(1, '../ciphers')
sys.path.insert(1, '../deciphers')

#importing encrypting/decrypting algos
from transposition_cipher import encrypt_message_transposition
from transposition_decipher import decrypt_message_transposition


CHARACHTERS = "ABCDEFGHIJKLMNOPQRSTUVWXZabcdefghijklmnopqrstuvwxy0123456789 ,;.?!:"
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

    #generate random key for the cipher
    key = math.ceil(text_length/2*random.random())

    #Test
    if decrypt_message_transposition(encrypt_message_transposition(text, key), key) == text:
        print(True)
    else:
        print(False)
