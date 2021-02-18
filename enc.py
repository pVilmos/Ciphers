import re
import sys
from ciphers import affine_cipher as a, caesar_cipher as c, multiplication_cipher as mu, reverse_cipher as r
from ciphers import substitution_cipher as s, transposition_cipher as t, vigenere_cipher as v
from datetime import datetime
from constants import CHARACHTERS, LENGTH

arg_line = " ".join(sys.argv[1:])

USAGE = (
    f"Usage: {sys.argv[0]} -m <OPTION> <FILE>"
)

HELP = (
    f"""
    Syntax:
        python {sys.argv[0]} -m <OPTION> <FILE>

    options:
        -m vig, aff, mul, ca, rev, sub, tra

    """
)

args_pattern = re.compile(
    r"""
    ^
    (
        (--(?P<HELP>help).*)|
        (-m\s(?P<ENC>\w+){1}\s)?
        (?P<FILE>[\w\.]+){1}
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

def write_key_file(filename, mode, *keys):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    with open('follow.txt', 'a') as writer:
        writer.write(dt_string + " " + filename + " " + mode + " " + " ".join(keys) + "\n")

if (__name__ == "__main__"):
    m = re.search(args_pattern, arg_line)

    #wrong input
    if m == None:
        print(USAGE)

    #help input
    elif m.group("HELP") != None:
        print(re.match(args_pattern, arg_line))
        print(m.group("HELP"))
        print(HELP)

    elif m.group("FILE") != None:

        #Check for mode
        try:
            mode = m.group("ENC").split()[0]
        #if type is None then the default is vig
        except:
            mode = "vig"


        try:
            # This is the main part
            # Handling all the different enc types
            f = read_file(m.group("FILE"))

            new_file_name = "en_" + m.group("FILE")


            if mode == "vig":

                #12 can be modified to taste
                key = v.generate_key_vigenere(12)
                content = v.encrypt_message_vigenere(f, key)
                write_key_file(m.group("FILE"), mode, key)
                write_file(new_file_name, content)

            elif mode == "aff":

                keys = a.generate_keys_affine(LENGTH)
                content = a.encrypt_message_affine(f, keys[0], keys[1], CHARACHTERS, LENGTH)
                write_key_file(m.group("FILE"), mode, str(keys[0]), str(keys[1]))
                write_file(new_file_name, content)

            elif mode == "rev":

                content = r.reverse(f)
                write_key_file(m.group("FILE"), mode)
                write_file(new_file_name, content)

            elif mode == "ca":
                key = c.generate_key_caesar(LENGTH)
                content = c.encrypt_message_caesar(f, key, CHARACHTERS, LENGTH)
                write_key_file(m.group("FILE"), mode, str(key))
                write_file(new_file_name, content)

            elif mode == "sub":
                key = s.generate_encryption_table(CHARACHTERS)
                content = s.encrypt_message_substitution(f, CHARACHTERS, key)
                write_key_file(m.group("FILE"), mode, key)
                write_file(new_file_name, content)


            #not stabile
            elif mode == "tra":
                key = t.generate_key_transposition(f)
                content = t.encrypt_message_transposition(f, key)
                write_key_file(m.group("FILE"), mode, str(key))
                write_file(new_file_name, content)

            elif mode == "mul":
                key = mu.generate_key_multiplication(LENGTH)
                content = mu.encrypt_message_multiplication(f, key, CHARACHTERS, LENGTH)
                write_key_file(m.group("FILE"), mode, str(key))
                write_file(new_file_name, content)

            else:
                print(f"No {m.group('ENC')} mode.")
        #handling nonexistence of file
        except:
            print(f'No {m.group("FILE")} exists.')
