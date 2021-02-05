#for more information on the theory visit:https://en.wikipedia.org/wiki/Affine_cipher

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def is_relative_prime(length, key):
    if gcd(length, key) == 1:
        return True
    else:
        return False

def affine_decipher_input(message, enc_table_length):
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


#we need to calculate the inverse of the multiplicative key in the finite
#ring of Z/mZ
def inverse_mod_mult(key_mult, mod):

    #I will use Euler's totient function for calculation (though other methods exist)

    #the totient function
    phi = 1

    #the totient function calculates the number of relative primes to key_mult below key_mult
    for i in range(2, mod):
        if is_relative_prime(mod, i):
            phi += 1
    return key_mult**(phi-1) % mod

#now we calulcate the additive part of the inverse affine function
def inverse_mod_add(key_mult, key_add, mod):

    inv = inverse_mod_mult(key_mult, mod)

    return (inv*key_add % mod)


def decrypt_message_affine(message, key_mult, key_add, enc_table, enc_table_length):
    decrypted_message = ""
    message_length = len(message)

    #calc inverses
    key_mult_inv = inverse_mod_mult(key_mult, enc_table_length)
    key_add_inv = inverse_mod_add(key_mult, key_add, enc_table_length)

    for i in range(0, message_length):
        if message[i] in enc_table:

            #the same formula for the affine function
            new_letter = enc_table[((enc_table.index(message[i]))*key_mult_inv - key_add_inv) % enc_table_length]

            decrypted_message = decrypted_message + new_letter

        #leave charachter alone if not in table
        else:
            decrypted_message = decrypted_message + message[i]

    return decrypted_message


if(__name__=="__main__"):
    message = input()
    keys = affine_decipher_input(message, LENGTH)
    print(decrypt_message_affine(message, keys[0], keys[1], CHARACHTERS, LENGTH))
