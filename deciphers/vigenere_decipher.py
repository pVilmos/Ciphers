CHARACHTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LENGTH = len(CHARACHTERS)

def decrypt_message_vigenere(message, dec_word):
    dec_message = ''


    number_list = []
    for i in range(0, len(dec_word)):
        if dec_word[i] in CHARACHTERS:
            number_list.append(CHARACHTERS.index(dec_word[i]))
        else:
            number_list.append(0)

    for i in range(0, len(message)):
        if message[i] in CHARACHTERS:
            dec_message = dec_message + CHARACHTERS[(CHARACHTERS.index(message[i]) - number_list[i % len(dec_word)]) % LENGTH]
        else:
            dec_message += message[i]
    return dec_message

if (__name__=="__main__"):
    message = input()
    dec_word = input()
    print(decrypt_message_vigenere(message, dec_word))
