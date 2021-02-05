import sys, random, math

sys.path.insert(1, '../ciphers')
sys.path.insert(1, '../deciphers')

from reverse_cipher import reverse
from constants import CHARACHTERS, LENGTH, TEXT_LIMIT, TEST_ROUNDS

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
