from constants import CHARACHTERS, LENGTH
import math
import random

def generate_key_caesar(length):
    return math.ceil(length*random.random())

def encrypt_message_caesar(message, key, charachters, length):
    encrypted_message = ""
    for i in message:
        if i in charachters:
            encrypted_message += charachters[(charachters.index(i) + key)%length]
        else:
            encrypted_message += i

    return encrypted_message

if __name__ == "__main__":
    print("This a Caesar cipher.")

    key = generate_key_caesar(LENGTH)

    message = input("Enter the message: \n")

    print("\n" + encrypt_message_caesar(message, key, CHARACHTERS, LENGTH))
