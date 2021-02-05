from math import ceil

def decrypt_message_transposition(message, key):
    limit = len(message)
    columns = ceil(limit/key)
    difference = key - (columns*key - limit)
    decryption_table = [""] * columns

    c_column = 0
    for i in range(0, limit):
        if c_column == columns-1:
            if len(decryption_table[c_column]) < difference:
                decryption_table[c_column] += message[i]
                c_column = 0
            else:
                c_column = 0
                decryption_table[c_column] += message[i]
                c_column += 1
        else:
            decryption_table[c_column] += message[i]
            c_column += 1


    return ''.join(decryption_table)

if(__name__ == "__main__"):
    message = input("Enter message to be decrypted: \n")
    key = input("ENter key:")
    print(decrypt_message_transposition(message, key))
