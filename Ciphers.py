from CipherObject import Cipher
import math, random

class Affine(Cipher):

    def __init__(self, name="affine", key0=1, key1=0,
                invkey0=1, invkey1=0, message="", mode="enc"):
        super().__init__(name, mode)
        self.key0 = key0
        self.key1 = key1
        self.invkey0 = invkey0
        self.invkey1 = invkey1

        self.message = message

    #we need to calculate the inverse of the multiplicative key in the finite
    #ring of Z/mZ
    def inverse_mult(self):

        #Euler's totient function for calculation (though other methods exist)

        #the totient function
        phi = 1

        #the totient function calculates the number of relative primes to key_mult below key_mult
        for i in range(2, self.LENGTH):
            if self.is_relative_prime(self.LENGTH, i):
                phi += 1
        self.invkey0 = self.key0**(phi-1) % self.LENGTH

    def gcd(self, a, b):

        while a != 0:
            a, b = b % a, a
        return b

    def is_relative_prime(self, key, length):

        if self.gcd(length, key) == 1:
            return True
        else:
            return False


    def generate_key(self):
        while True:
            key_mult = math.floor(self.LENGTH*random.random())

            if self.is_relative_prime(key_mult, self.LENGTH):
                self.key0 = key_mult
                self.inverse_mult()
                break

        self.key1 = math.floor(self.LENGTH*random.random())
        self.invkey1 = -self.key1

    def change_mode(self, mode):
        self.mode = mode

    def add_key(self, key0, key1):
        if is_relative_prime(key0, self.LENGTH):
            self.key0 = key0
            self.inverse_mult()
        else:
            self.key0 = 1
            self.invkey0 = 1

        if key1 < self.LENGTH:
            self.key1 = key1
            self.invkey1 = -key1
        else:
            self.key1 = 0
            self.invkey1 = 0

    def get_key(self):
        pass

    def modify_string(self, message, mode):
        mod_message = ""
        length = len(message)
        for i in range(0, length):

            if message[i] in self.CHARACHTERS:
                if mode == "enc":
                    new_letter = self.CHARACHTERS[
                        ((self.CHARACHTERS.index(message[i]))*self.key0 + self.key1) % self.LENGTH
                        ]
                    mod_message += new_letter
                elif mode == "dec":
                    new_letter = self.CHARACHTERS[
                        ((self.CHARACHTERS.index(message[i]))*self.invkey0 + self.invkey1*self.invkey0) % self.LENGTH
                        ]
                    mod_message += new_letter
            else:
                mod_message += message[i]

        self.message = mod_message

    def encrypt_file(self, file):
        pass

##-------------------------------------------------------##
##-------------------------------------------------------##
##-------------------------------------------------------##


class Multiplication(Affine):

    def __init__(self):
        super().__init__(name="multiplication")
        self.key = self.key0

    def add_key(self, key):
        self.key = key

    def generate_key(self):
        super().generate_key()
        self.key1 = 0
        self.invkey1 = 0

##-------------------------------------------------------##
##-------------------------------------------------------##
##-------------------------------------------------------##

class Caesar(Affine):
    def __init__(self):
        super().__init__(name="caesar")
        self.key = self.key1

    def generate_key(self):
        super().generate_key()
        self.key0 = 1
        self.invkey0 = 1

    def add_key(self, key):
        self.key = key

##-------------------------------------------------------##
##-------------------------------------------------------##
##-------------------------------------------------------##


class Reverse(Cipher):
    def __init__(self, message=""):
        super().__init__(name="reverse")
        self.message = message

    def modify_string(self, message):
        self.message = message[::-1]

##-------------------------------------------------------##
##-------------------------------------------------------##
##-------------------------------------------------------##

class Transposition(Cipher):
    def __init__(self,key=0, mode="enc"):
        super().__init__(name="transposition")
        self.mode = mode
        self.key = key

    def generate_key(self):
        key_limit = math.ceil(len(self.message)/2)
        self.key = math.ceil(key_limit*random.random())

    def modify_string(self):
        message = ""
        if self.mode == "enc":
            for i in range(0, self.key):
                for j in range(i, len(self.message), self.key):
                    message += self.message[j]
            self.message = message

        elif self.mode == "dec":
            limit = len(self.message)
            columns = math.ceil(limit/self.key)
            difference = self.key - (columns*self.key - limit)
            decryption_table = [""] * columns

            c_column = 0
            for i in range(0, limit):
                if c_column == columns-1:
                    if len(decryption_table[c_column]) < difference:
                        decryption_table[c_column] += self.message[i]
                        c_column = 0
                    else:
                        c_column = 0
                        decryption_table[c_column] += self.message[i]
                        c_column += 1
                else:
                    decryption_table[c_column] += self.message[i]
                    c_column += 1


            self.message = ''.join(decryption_table)

##-------------------------------------------------------##
##-------------------------------------------------------##
##-------------------------------------------------------##

class Vigenere(Cipher):
    def __init__(self, key="A"):
        super().__init__(name="vigenere")
        self.key = key

    def generate_key(self):
        word = ""
        #generate word length between 10 and 20
        length = math.floor(10*random.random()) + 10

        for j in range(0, length):
            pos = math.floor(self.LENGTH*random.random())
            word += self.CHARACHTERS[pos]

        self.key = word

    def modify_string(self):
        message = ""
        #making the letters to corresponding numbers in self.key
        if self.mode == "enc":
            number_list = []
            for i in range(0, len(self.key)):
                if self.key[i] in self.CHARACHTERS:
                    number_list.append(self.CHARACHTERS.index(self.key[i]))
                else:
                    number_list.append(0)

            for i in range(0, len(self.message)):
                if self.message[i] in self.CHARACHTERS:
                    message = message + self.CHARACHTERS[(self.CHARACHTERS.index(self.message[i]) + number_list[i % len(self.key)]) % self.LENGTH]
                else:
                    message += self.message[i]
            self.message = message
        elif self.mode == "dec":

            number_list = []
            for i in range(0, len(self.key)):
                if self.key[i] in self.CHARACHTERS:
                    number_list.append(self.CHARACHTERS.index(self.key[i]))
                else:
                    number_list.append(0)

            for i in range(0, len(self.message)):
                if self.message[i] in self.CHARACHTERS:
                    message = message + self.CHARACHTERS[(self.CHARACHTERS.index(self.message[i]) - number_list[i % len(self.key)]) % self.LENGTH]
                else:
                    message += self.message[i]
            self.message = message

##-------------------------------------------------------##
##-------------------------------------------------------##
##-------------------------------------------------------##

class Substitution(Cipher):
    def __init__(self):
        super().__init__(name="substitution")
        self.key = self.CHARACHTERS

    def generate_key(self):

        encryption_table = ""
        #change type of alphabet
        alphabet = list(self.CHARACHTERS)

        #loop through the encryption table
        for i in range(self.LENGTH, 0, -1):

            #pick out randomly a charachter from the alphabet
            pos = math.floor(i*random.random())
            encryption_table += alphabet[pos]

            #take out the last element from the alphabet
            #this is needed to select randomly from the remaining charachters
            #and avoiding duplicates in the new table
            alphabet.pop(pos)
        self.key = encryption_table

    def modify_string(self):
        message = ""
        if self.mode == "enc":

            #looping through the message
            for letter in self.message:
                if letter not in self.CHARACHTERS:
                    message += letter


                #leaving the the charachters the same that are not in the charachters
                else:
                    message += self.key[self.CHARACHTERS.index(letter)]

            self.message = message

        elif self.mode == "dec":

            #looping through the message
            for letter in self.message:

                if letter not in self.CHARACHTERS:
                    message += letter

                #leaving the the charachters the same that are not in the alphabet
                else:
                    message += self.CHARACHTERS[self.key.index(letter)]
            self.message = message

class PublicKeyCipher