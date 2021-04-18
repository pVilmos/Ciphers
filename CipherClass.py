import math, random
from abc import ABC, abstractmethod

class Cipher(ABC):
    CHARACHTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    LENGTH = len(CHARACHTERS)

    #initialize the name/type of the cipher
    #mode can be enc or dec
    #option can be
    def __init__(self, name, message="", mode="enc"):
        self.name = name
        self.mode = mode
        self.message = message


    def __str__(self):
        return f"<Object Cipher>"

    # method for taking in the file and converting it
    def modify_string(self, string):
        pass

    # method for taking in the file and converting it
    def modify_file(self, file):
        pass

    #add key manually
    def add_key(self):
        pass

    #generate key randomly
    def generate_key(self):
        pass
