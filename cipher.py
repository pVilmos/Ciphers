from Ciphers import Affine, Transposition, Multiplication, Caesar, Reverse, Vigenere, Substitution
from datetime import datetime
import re
import sys

arg_line = " ".join(sys.argv[1:])

USAGE = (
    f"Usage: python {sys.argv[0]} [-c <Cipher>] [-m <Method>] [-k <Keys>] (-s <STRING>)/(-f <FILE>)"
)

HELP = (
    f"""
    Syntax:
        python {sys.argv[0]} <OPTION> <FILE>

    options:
        -c, --cipher vig, aff, mul, ca, rev, sub, tra
        -m, --method enc dec

    """
)

args_pattern = re.compile(
    r"""
    ^
    (
        (--(?P<HELP>help).*)|
        (-c\s(?P<CIP>\w+){1}\s)?
        (-m\s(?P<METHOD>\w+){1}\s)?
        (-k\s((?P<KEYS>\S+){1}\s))?
        ((?P<OPTIONALKEY>\d+){1}\s)?
        (-f\s(?P<FILE>\w+\.txt)|(-s\s(?P<STRING>.+)))?
    )
    $
""",
    re.VERBOSE,
)

def read_file(filename):
    with open(filename, mode='r') as f:
        return f.read()

def write_file(filename, content):
    with open(filename, mode='w') as f:
        f.write(content)

def write_key_file(filename, name, mode, *keys):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    with open('follow.txt', 'a') as writer:
        writer.write(dt_string + " " + filename + " " + name + " " + mode + " " + " ".join(keys) + "\n")

if (__name__ == "__main__"):
    m = re.search(args_pattern, arg_line)
    '''
    print(m)
    print("cipher", m.group("CIP"))
    print("method", m.group("METHOD"))
    print("keys", m.group("KEYS"))
    print("optional", m.group("OPTIONALKEY"))
    print("file", m.group("FILE"))
    print("string", m.group("STRING"))
    '''

    #wrong input
    if m == None:
        print(USAGE)

    elif m.group("HELP") != None:
        print(re.match(args_pattern, arg_line))
        print(m.group("HELP"))
        print(HELP)

    elif m.group("FILE") != None or m.group("STRING") != None:

        cip = m.group("CIP")

        method = m.group("METHOD")
        if method != "enc" and method != "dec":
            method = "enc"

        keys = m.group("KEYS")

        fname = None

        if m.group("STRING"):
            message = m.group("STRING")
        else:
            message = read_file(m.group("FILE"))
            fname = m.group("FILE")


        if cip == "vig":
            vig = Vigenere()
            vig.mode = method
            vig.key = keys
            if not keys:
                vig.generate_key()
                print(vig.key)
            vig.message = message
            vig.modify_string()
            if fname:
                write_file(fname, vig.message)
                write_key_file(fname, vig.name, vig.mode, vig.key)
            else:
                print(vig.key)
                print(vig.message)


        elif cip == "aff":
            aff = Affine()
            aff.mode = method
            if not keys:
                aff.generate_key()
            else:
                aff.add_key(int(keys), int(m.group("OPTIONALKEY")))

            aff.message = message
            aff.modify_string(aff.message, aff.mode)
            if fname:
                write_file(fname, aff.message)
                write_key_file(fname, aff.name, aff.mode, keys, m.group("OPTIONALKEY"))

            else:
                print(aff.key0, aff.key1)
                print(aff.message)

        elif cip == "cas":
            caesar = Caesar()
            caesar.mode = method
            if not keys:
                caesar.generate_key()
            else:
                caesar.add_key(1, int(keys))


            caesar.message = message
            caesar.modify_string(caesar.message, caesar.mode)
            if fname:
                write_file(fname, caesar.message)
                write_key_file(fname, caesar.name, caesar.mode, str(caesar.key1))
            else:
                print(caesar.key1)
                print(caesar.message)

        elif cip == "mult":
            mult = Multiplication()
            mult.mode = method
            if not keys:
                mult.generate_key()
            else:
                mult.add_key(int(keys), 0)


            mult.message = message
            mult.modify_string(mult.message, mult.mode)
            if fname:
                write_file(fname, mult.message)
                write_key_file(fname, mult.name, mult.mode, str(mult.key0))
            else:
                print(mult.key0)
                print(mult.message)

        elif cip == "rev":
            rev = Reverse()
            rev.message = message
            rev.modify_string()
            if fname:
                write_file(fname, rev.message)
                write_key_file(fname, rev.name, "enc/dec")
            else:
                print(rev.message)
        

        elif cip == "trans":
            trans = Transposition()
            trans.mode = method
            trans.key = int(keys)
            trans.message = message
            if not keys:
                trans.generate_key()
            print(trans.key)
            trans.modify_string()
            if fname:
                write_file(fname, trans.message)
            else:
                print(trans.message)

        elif cip == "sub":
            sub = Substitution()
            sub.mode = method
            sub.message = message
            sub.key = keys
            if not keys:
                sub.generate_key()
            print(sub.key)
            sub.modify_string()
            if fname:
                write_file(fname, sub.message)
            else:
                print(sub.message)
        else:
            print(f"No {m.group('ENC')} mode.")

