from itertools import permutations
from random import random
from math import floor

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
ALPHABET_LENGTH = len(ALPHABET)

def encrypt_message_substitution(message, alphabet, encryption_table):
    encrypted_message = ""

    #looping through the message
    for letter in message:
        if letter not in alphabet:
            encrypted_message += letter


        #leaving the the charachters the same that are not in the alphabet
        else:
            encrypted_message += encryption_table[alphabet.index(letter)]

    return encrypted_message

def generate_encryption_table(alphabet):
    encryption_table = ""
    #change type of alphabet
    alphabet = list(ALPHABET)

    #loop through the encryption table
    for i in range(ALPHABET_LENGTH, 0, -1):

        #pick out randomly a charachter from the alphabet
        pos = floor(i*random())
        encryption_table += alphabet[pos]

        #take out the last element from the alphabet
        #this is needed to select randomly from the remaining charachters
        #and avoiding duplicates in the new table
        alphabet.pop(pos)
    return encryption_table


if(__name__=="__main__"):
    message = input()

    print(encrypt_message_substitution(message, ALPHABET, encryption_table))
