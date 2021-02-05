import math, random
from constants import LENGTH, CHARACHTERS

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def is_relative_prime(length, key):
    if gcd(length, key) == 1:
        return True
    else:
        return False

def affine_cipher_input(message, enc_table_length):
    print("Valid first keys: \n")

    #printing valid keys
    for i in range(0, enc_table_length):
        if is_relative_prime(enc_table_length, i):
            print(i)
        else:
            pass
    while True:
        try:
            key_mult = int(input("Enter first key:\n"))
            if is_relative_prime(enc_table_length, key_mult) and key_mult >=0 and key_mult < enc_table_length:
                break
            else:
                print("Enter a number from the list.")

        except:
            print("Enter a number form the list.")

    print("Valid second keys: 0-" + str(enc_table_length))
    while True:
        try:
            key_add = int(input("Enter second key:"))
            if key_add > -1 and key_add < enc_table_length:
                break
            else:
                print("Enter a valid number.")
                pass
        except:
            print("Enter a valid number.")

    return key_mult, key_add

def generate_keys_affine(length):
    while True:
        key_mult = math.floor(length*random.random())
        if is_relative_prime(key_mult, length):
            break

    key_add = math.floor(length*random.random())

    return key_mult, key_add

def encrypt_message_affine(message, key_mult, key_add, enc_table, enc_table_length):
    encrypted_message = ""
    length = len(message)
    for i in range(0, length):
        if message[i] in enc_table:
            new_letter = enc_table[((enc_table.index(message[i]))*key_mult + key_add) % enc_table_length]
            encrypted_message = encrypted_message + new_letter
        else:
            encrypted_message = encrypted_message + message[i]

    return encrypted_message

if (__name__ == "__main__"):
    print("This is an affine cipher.")
    message = input("Please enter a message: \n")
    keys = affine_cipher_input(message, LENGTH)
    print(encrypt_message_affine(message, keys[0], keys[1], CHARACHTERS, LENGTH))

    generate_keys_affine(LENGTH)
