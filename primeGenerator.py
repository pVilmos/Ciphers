import random

def RabinMillerPrimality(number):
    if number % 2 == 0 or number == 1:
        return False
    count = number-1
    t=0
    while count % 2 == 0:
        count = count//2
        t += 1

    for trials in range(5):
        a = random.randrange(2, number-1)
        v = pow(a, count, number)
        if v != 1:
            i = 0
            while v != number - 1:
                if i == t-1:
                    return False
                else:
                    i = i+1
                    v = (v**2)%number
    return True

def generateLargePrime(keysize=1024):
    while True:
        num = random.randrange(2**(keysize-1), 2**keysize)
        if RabinMillerPrimality(num):
            return num

if __name__=="__main__":
    print(generateLargePrime())