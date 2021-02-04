# python enc.py <option> <argument>
#default arg one-pad cipher and writes to a file the modified file, the type of encoding and the required keys
#OPTIONS:
#-n --nowrite doesn't write to file, this should require a confirmation
#--name to name the created file default is <filename>_encrypted
#-a -affine for affine cipher optional arguments: key_mult, key_add
#-c --caesar for caesar cipher optional arg: key
#-m --multiplication for multiplication cipher optional arg: key
#-r --reverse no arg
#-s --substitution no arg
#-t --transposition arg
#-v --vigenere arg string
#-m --mode option

import review
import sys
from ciphers import affine_cipher as a, caesar_cipher as c, multiplication_cipher as m, reverse_cipher as r
from ciphers import substitution_cipher as s, transposition_cipher as t, vigenere_cipher as v

enc_type = ""

arg_line = " ".join(sys.argv[1:])

USAGE = (
    f"Usage: {sys.argv[0]} <-n <nowrite>> <OPTION1> <file>"
)

args_pattern = re.compile(
    r"""
    ^
    (
        (--(?P<HELP>help).*)|
        (-m\s(?P<ENC>\w))?
        (?<FILE>\w){1}


    )
""",
    re.VERBOSE,
)

def parse(arg_line: str) -> Dict[str, str]:




def read_file(filename):
    with open(filename, mode='r') as f:
        return f.read()

def write_key_file():
    pass

if (__name__ == "__main__"):
