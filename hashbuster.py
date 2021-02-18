#!/usr/bin/python
from getpass import getpass
from os import system

system('clear')

# colors

red = "\033[91;1m"
green = "\033[92;1m"
yellow = "\033[93;1m"
blue = "\033[94;1m"

# banner

print(green +
'''
┌───────────────────────────────┐
│╻ ╻┏━┓┏━┓╻ ╻ ┏┓ ╻ ╻┏━┓╺┳╸┏━╸┏━┓│
│┣━┫┣━┫┗━┓┣━┫ ┣┻┓┃ ┃┗━┓ ┃ ┣╸ ┣┳┛│
│╹ ╹╹ ╹┗━┛╹ ╹ ┗━┛┗━┛┗━┛ ╹ ┗━╸╹┗╸│
└───────────────────────────────┘
''')

# Option manu

print(yellow + ' [1] Hash Generator ')
print(yellow + ' [2] Md5 BruteForce')
print(yellow + ' [3] Sha1 BruteForce')
print(yellow + ' [4] Sha224 BruteForce')
print(yellow + ' [5] Sha256 BruteForce')
print(yellow + ' [6] Sha512 BruteForce')

input = input(blue +"\nSelect Option : ")
print('')

# Input options

if (input =='1' or input =='01'):
    system('python modules/hasher.py')
elif (input =='2' or input =='02'):
    system('python modules/md5_brute.py')
elif (input =='3' or input =='03'):
    system('python modules/sha1_brute.py')
elif (input =='4' or input =='04'):
    system('python modules/sha224_brute.py')
elif (input =='5' or input =='05'):
    system('python modules/sha256_brute.py')
elif (input =='6' or input =='06'):
    system('python modules/sha512_brute.py')
else:
    print(red + '[!] Invalid Option, Exiting...')
    exit()

