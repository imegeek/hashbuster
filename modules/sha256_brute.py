#!/usr/bin/python


#colours
red = "\033[91;1m"
green = "\033[92;1m"
yellow = "\033[93;1m"
blue = "\033[94;1m"


from urllib.request import urlopen
import hashlib


sha256hash = input("[#] Enter The Sha256 Hash Value : ")
url = str(input("[*] Enter The Hash Password Raw Link : "))
passlist = str(urlopen(url).read (), 'utf-8')
for password in passlist.split('\n'):
    hashgess = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
    if hashgess == sha256hash:
        print(green + "[*] The Password Is: " + str(password))
        quit()
    else:
        print(red + "[-] The Password Guess" + str(password) + "Does Not Match, Trying New...")
print("Password is not in password list")
