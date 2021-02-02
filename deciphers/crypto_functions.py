ENCRYPTION_TABLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
ENCRYPTION_TABLE_LENGTH = len(ENCRYPTION_TABLE)

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def is_relative_prime(length, key):
    if gcd(length, key) == 1:
        return True
    else:
        return False
