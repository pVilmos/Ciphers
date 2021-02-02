from crypto_functions import gcd, is_relative_prime
def main():
    print("This is a multiplication cipher.")
    message = input("Enter messsage:\n")
    secret_key = multiplication_cipher_input(message)
    print("Your message is " + str(encrypt_message_multiplication(message, secret_key)))



def multiplication_cipher_input(message):
    message_length = len(message)
    print("Valid keys: \n")

    #printing valid keys
    for i in range(0, message_length):
        if is_relative_prime(message_length, i):
            print(i)
        else:
            pass

    while True:

        try:
            secret_key = int(input("Enter key: "))
            if is_relative_prime(message_length, secret_key):
                break
            else:
                print("Please enter a number from the list.")

        except:
            print("Please enter a number from the list.")
    return secret_key

def encrypt_message_multiplication(message, key):
    enc_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.:,;!?+-() "
    enc_table_length = len(enc_table)
    encrypted_message = ""
    message_length = len(message)
    for i in range(0, message_length):
        if message[i] in enc_table:
            new_letter = enc_table[message.index(message[i])*key % enc_table_length]
            encrypted_message = encrypted_message + new_letter
        else:
            encrypted_message = encrypted_message + message[i]

    return encrypted_message

if __name__ == "__main__":
    main()
