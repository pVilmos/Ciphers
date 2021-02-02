message = input("Please enter the message to be decyphered: \n")

secret_key_trial = 1

letters = []
for i in range(97, 123):
    letters.append(chr(i))

decrypted_letters = []
for i in range(0, 26):
    decrypted_letters.append(chr((i+secret_key_trial)%26 + 97))

print("Which one looks right? (Enter 0 if it is correct 1 otherwise) \n")

for i in range(0, 25):
    decrypted_message = ""

    for j in range(0, len(message)):
        letter = message[j]
        if letter.lower() not in letters:
            decrypted_message = decrypted_message + letter
        else:
            if letter not in letters:
                enc_letter = letters[decrypted_letters.index(letter.lower())]
                decrypted_message = decrypted_message + enc_letter.upper()
            else:
                enc_letter = letters[decrypted_letters.index(letter)]
                decrypted_message = decrypted_message + enc_letter

    print(decrypted_message + "")
    response = input()
    print("\n")
    if response == "1":
        print("This is your decrypted message.")
        break
    elif response == "0":
        secret_key_trial += 1
        for j in range(0, 26):
            decrypted_letters[j] = chr((j+secret_key_trial)%26 + 97)

if response == "0":
    print("This message was not crypted with caesar.")
