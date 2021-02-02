#This is a very basic Caesar cipher. It only permutes the letters and it doesn't take into account capital letters.
#Meaning if a -> f then A -> F.
#"a" in ASCII table is in decimal position 97.

def main():

    print("This a Caesar cipher.")

    message = input("Enter the message: \n")

    print("\n" + encrypt_message_caesar(message))
    
def encrypt_message_caesar(message):
    letters = []
    for i in range(97, 123):
        letters.append(chr(i))

    while True:
        secret = input("Add a secret key (integer between 1 and 25):")
        try:
            secret_key = int(secret)
            if secret_key < 1 or secret_key > 25:
                print("Please enter an integer between 1 and 25.")
            else:
                break
        except:
            print("Please enter an integer.")

    #create shifted list of letters

    shifted_letters = []
    for i in range(0, 26):
        shifted_letter = letters[(i + secret_key) % 26]
        shifted_letters.append(shifted_letter)

    #processing the message

    encrypted_message = ""

    for i in range(0, len(message)):
        letter = message[i]

        #branch for character not in alphabet
        if letter.lower() not in letters:
            encrypted_message = encrypted_message + letter

        #differentiate between lowercase vs. uppercase
        else:
            if letter not in letters:
                enc_letter = shifted_letters[letters.index(letter.lower())]
                encrypted_message = encrypted_message + enc_letter.upper()
            else:
                enc_letter = shifted_letters[letters.index(letter)]
                encrypted_message = encrypted_message + enc_letter
    return encrypted_message

if __name__ == "__main__":
    main()
