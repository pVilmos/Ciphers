from Ciphers import Affine, Transposition, Multiplication, Caesar, Reverse, Vigenere, Substitution
from datetime import datetime
import re
import sys

arg_line = " ".join(sys.argv[1:])

USAGE = (
    f"Usage: python {sys.argv[0]} <OPTION> <FILE>"
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
    f"""
    ^
        (--(?P<HELP>help).*)|
        (-c\s(?P<CIP>\w+){1}\s)?
        (-m\s(?P<METHOD>{1}\w+))?
        (-k\s(?P<KEYS>\w+)?)?
        (?P<FILE>\w+\.txt)?
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

def write_key_file(filename, mode, *keys):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    with open('follow.txt', 'a') as writer:
        writer.write(dt_string + " " + filename + " " + mode + " " + " ".join(keys) + "\n")

class CipherMachine:
    def code_text(self, cipher, text):
        cipher.generate_key()
        cipher.message = text
        cipher.modify_string()
        return cipher.message

if (__name__ == "__main__"):
    m = re.search(args_pattern, arg_line)

    #wrong input
    if m == None:
        print(USAGE)

    elif m.group("HELP") != None:
        print(re.match(args_pattern, arg_line))
        print(m.group("HELP"))
        print(HELP)

    elif m.group("FILE") != None:

        try:
            cip = m.group("CIP").split()[0]
        except:
            cip = "vig"

        try:
            method = m.group("METHOD").split()[0]
        except:
            method = "enc"

        try:
            f = read_file(m.group("FILE"))
            fname = m.group("FILE")

            cipherMachine = CipherMachine()

            if cip == "vig":
                vig = Vigenere()
                if method == "enc":
                    content = cipherMachine.code_text(vig, f)
                else:
                    vig.key = m.group("KEYS")[0]
                write_key_file(fname, cip, vig.key)
                write_file(fname, content)

            elif cip == "aff":
                aff = Affine()
                content = cipherMachine.code_text(aff, f)
                write_key_file(fname, cip, aff.key1, aff.key2)
                write_file(fname, content)
            else:
                print(f"No {m.group('ENC')} mode.")

        except:
            print(f'No {fname} exists.')
