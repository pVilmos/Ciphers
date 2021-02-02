from math import ceil
from ciphers.transposition_cipher import encrypt_message_transposition as e_tr
from ciphers.caesar_cipher import encrypt_message_caesar as e_ca
from ciphers.multiplication_cipher import multiplication_cipher_input as mult_input, encrypt_message_multiplication as e_mult
from ciphers.affine_cipher import affine_cipher_input as aff_input, encrypt_message_affine as e_aff
from static.crypto_functions import ENCRYPTION_TABLE as enc_table, ENCRYPTION_TABLE_LENGTH as enc_table_length

while True:
    print("Choose what kind of encryption method you want to use: ")
    enc_type = input("\n (0) Caesar \n (1) Tranposition \n (2) Multiplication \n (3) Affine \n")
    message = input("Enter message: \n")
    if enc_type == "0":
        print(e_ca(message))

    elif enc_type == "1":
        message_length = len(message)
        key_limit = ceil(message_length/2)
        print(e_tr(message, message_length, key_limit))

    elif enc_type == "2":
        secret_keys = mult_input(message)
        print(e_mult(message, secret_key))

    elif enc_type == "3":
        secret_keys = aff_input(message, enc_table_length)
        print(e_aff(message, secret_keys[0], secret_keys[1], enc_table, enc_table_length))

    decide = input(" \n (e) exit \n or continue...")

    if decide == "e" or decide == "ex" or decide == "exi" or decide == "exit":
        break
    else:
        pass

print("Thank you!")
