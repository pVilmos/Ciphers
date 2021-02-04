import hashlib
import sys

def sha1sum(filename: str) -> str:
    hash = hashlib.sha1()
    with open(filename, mode="rb") as f:
        hash.update(f.read())
    return hash.hexdigest()

for arg in sys.argv[1:]:
    print(f"{sha1sum(arg)}  {arg}")
