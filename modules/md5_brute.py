#!/usr/bin/python
#colours
red = "\033[91;1m"
green = "\033[92;1m"
yellow = "\033[93;1m"
blue = "\033[94;1m"



from urllib.request import urlopen
import hashlib


md5hash = input("[#] Enter The Md5 Hash Value : ")
url = str(input("[*] Enter The Hash Password Raw Link : "))
passlist = str(urlopen(url).read (), 'utf-8')
for password in passlist.split('\n'):
    hashgess = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
    if hashgess == md5hash:
        print(green + "[*] The Password Is: " + str(password))
        quit()
    else:
        print(red + "[-] The Password Guess" + str(password) + "Does Not Match, Trying New...")
print("Password is not in password list")
