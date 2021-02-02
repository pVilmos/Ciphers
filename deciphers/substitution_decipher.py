#note that this code is basically ../ciphers/substitution_cipher.py
#This reason for making another file is purely for
from itertools import permutations
from random import random
from math import floor

#alphabet
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
ALPHABET_LENGTH = len(ALPHABET)

def decrypt_message_substitution(message, alphabet, decryption_table):
    decrypted_message = ""

    #looping through the message
    for letter in message:

        if letter not in alphabet:
            decrypted_message += letter

        #leaving the the charachters the same that are not in the alphabet
        else:
            decrypted_message += decryption_table[alphabet.index(letter)]
    return decrypted_message

if(__name__=="__main__"):
    message = input()

    print(encrypt_message_substitution(message, ALPHABET, encryption_table))
