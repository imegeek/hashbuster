#!/usr/bin/python
import hashlib

#colours
reset = "\033[0;1m"
green = "\033[92;1m"
yellow = "\033[93;1m"
blue = "\033[94;1m"

hashvalue = input('Enter a String Value : ')

hashobj1 = hashlib.md5()
hashobj1.update(hashvalue.encode())

hashobj2 = hashlib.sha1()
hashobj2.update(hashvalue.encode())

hashobj3 = hashlib.sha224()
hashobj3.update(hashvalue.encode())

hashobj4 = hashlib.sha256()
hashobj4.update(hashvalue.encode())

hashobj5 = hashlib.sha512()
hashobj5.update(hashvalue.encode())

print(reset +"\nMD5    : " + green
+ hashobj1.hexdigest()
+ reset +"\nSHA1   : " + blue
+ hashobj2.hexdigest()
+ reset +"\nSHA224 : " + yellow
+ hashobj3.hexdigest()
+ reset +"\nSHA256 : " + green
+ hashobj4.hexdigest()
+ reset +"\nSHA56  : " + blue
+ hashobj5.hexdigest()
)
print("")
