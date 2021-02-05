from constants import CHARACHTERS, LENGTH

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def is_relative_prime(length, key):
    if gcd(length, key) == 1:
        return True
    else:
        return False


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


def generate_key_multiplication(length):
    while True:
        key_mult = math.floor(length*random.random())
        if is_relative_prime(key_mult, length):
            break

    return key_mult

def encrypt_message_multiplication(message, key, charachters, length):
    encrypted_message = ""
    message_length = len(message)
    for i in range(0, message_length):
        if message[i] in charachters:
            new_letter = charachters[message.index(message[i])*key % length]
            encrypted_message = encrypted_message + new_letter
        else:
            encrypted_message = encrypted_message + message[i]

    return encrypted_message

if __name__ == "__main__":
    print("This is a multiplication cipher.")
    message = input("Enter messsage:\n")
    secret_key = multiplication_cipher_input(message)
    print("Your message is " + str(encrypt_message_multiplication(message, secret_key, CHARACHTERS, LENGTH)))
