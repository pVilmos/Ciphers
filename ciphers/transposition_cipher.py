from math import ceil
import random

#Common sense is not so common.
def transposition_cipher_input(message):
    key_limit = ceil(len(message)/2)
    while True:
        secret = input("Add a secret key (integer between 1 and " + str(key_limit) + "):\n")
        try:
            secret_key = int(secret)
            if secret_key < 1 or secret_key > key_limit:
                print("Please enter an integer between 1 and " + str(key_limit) + ":\n")
            else:
                break
        except:
            print("Please enter an integer: \n")
    return secret_key

def generate_key_transposition(message):
    key_limit = ceil(len(message)/2)

    return ceil(key_limit*random.random())


def encrypt_message_transposition(message, secret_key):
    encrypted_message = ""
    for i in range(0, secret_key):
        for j in range(i, len(message), secret_key):
            encrypted_message = encrypted_message + message[j]
    return encrypted_message

if __name__ == '__main__':
    print("This a Transposition cipher. \nPlease enter a message:")

    message = input()
    print(generate_key_transposition(message))
    key_limit = transposition_cipher_input(message)

    print(encrypt_message_transposition(message, key_limit))
