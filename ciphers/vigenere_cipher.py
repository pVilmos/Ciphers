CHARACHTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LENGTH = len(CHARACHTERS)

def encrypt_message_vigenere(message, enc_word):

    enc_message = ""
    #making the letters to corresponding numbers in enc_word

    number_list = []
    for i in range(0, len(enc_word)):
        if enc_word[i] in CHARACHTERS:
            number_list.append(CHARACHTERS.index(enc_word[i]))
        else:
            number_list.append(0)

    for i in range(0, len(message)):
        if message[i] in CHARACHTERS:
            enc_message = enc_message + CHARACHTERS[(CHARACHTERS.index(message[i]) + number_list[i % len(enc_word)]) % LENGTH]
        else:
            enc_message += message[i]
    return enc_message

if (__name__=="__main__"):
    message = input()
    enc_word = input()
    print(encrypt_message_vigenere(message, enc_word))
