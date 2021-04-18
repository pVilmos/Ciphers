# File Encrypting program in Python

## Quick how to use:

Type 'python cipher.py [-c <Cipher>] [-m <Method>] [-k <Keys>] (-s <STRING>)/(-f <FILE>)' into your command line, where <Cipher> can be any the following:

vig, aff, mult, cas, rev, sub

vig for the vigenere cipher

aff for the affine cipher
mult for the multiplication cipher
sub for the substitution cipher
cas for the caesar cipher
rev for the reverse cipher

The command makes a new file and updates the follow file. (This is where you can keep track of the history

RSA and transposition ciphers are still in progress

##Examples

>python cipher.py -c rev -s Hello how are you?
?uoy era woh olleH

>python cipher.py -c aff -m enc -k 35 13 -s Hello, how are you today?
35 13
yXIIJ YJd nKX vJL cJonv?

>python cipher.py -c aff -m dec -k 35 13 -s yXIIJ YJd nKX vJL cJonv?
35 13
Hello, how are you today?

>more example.txt
This is a test.
Hopefully works.
>python cipher.py -c vig -m enc -f example.txt
dgAliKNQGxNl
>more example.txt
wNid sF g GPVZ.
pyCulryWb wZZuF.
>python cipher.py -c vig -m dec -k dgAliKNQGxNl -f example.txt
>more example.txt
This is a test.
Hopefully works.