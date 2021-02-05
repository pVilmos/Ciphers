from itertools import permutations
from random import random
from math import floor

CHARACHTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
LENGTH = len(CHARACHTERS)

def encrypt_message_substitution(message, charachters, encryption_table):
    encrypted_message = ""

    #looping through the message
    for letter in message:
        if letter not in charachters:
            encrypted_message += letter


        #leaving the the charachters the same that are not in the charachters
        else:
            encrypted_message += encryption_table[charachters.index(letter)]

    return encrypted_message

def generate_encryption_table(charachters):
    encryption_table = ""
    #change type of alphabet
    alphabet = list(charachters)

    #loop through the encryption table
    for i in range(LENGTH, 0, -1):

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
    print(encrypt_message_substitution(message, CHARACHTERS, encryption_table))
