import sys, random, math

sys.path.insert(1, '../ciphers')
sys.path.insert(1, '../deciphers')

from reverse_cipher import reverse

CHARACHTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
LENGTH = len(CHARACHTERS)

#limit for the test text length
TEXT_LIMIT = 100

TEST_ROUNDS = 50

#Only for epicness
input("Start testing...")

for i in range(0, TEST_ROUNDS):

    text = ""

    #generate random text length
    text_length = math.ceil(TEXT_LIMIT*random.random())

    #generate random text
    for j in range(0, text_length):
        pos = math.ceil(LENGTH*random.random())-1
        text += CHARACHTERS[pos]

    #Test
    if reverse(reverse(text)) == text:
        print(True)
    else:
        print(False)
