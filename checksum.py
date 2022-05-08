import hashlib
import binascii
import os

def checksum(filename):
    BUFFER_SIZE = 65536
    try:
        with open(f"{filename}", "rb") as f:
            file = f.read(BUFFER_SIZE)
            sha1 = hashlib.sha1(file).hexdigest()
            sha256 = hashlib.sha256(file).hexdigest()
            sha512 = hashlib.sha512(file).hexdigest()
            md5 = hashlib.md5(file).hexdigest()
            crc32 = binascii.crc32(file)
            print(f"SHA1: {sha1}\nSHA256: {sha256}\nSHA512: {sha512}\nMD5: {md5}\nCRC32: {crc32 & 0xFFFFFFFF:08x}")
    except FileNotFoundError:
        print(f"{filename} isn't a file.")
def ask():
    option = input("Do you want to calculate the checksum of a file? (Y/N): ")
    if option.upper() == 'Y':
        file = input("What's the file you want to check out? ")
        checksum(file)
    elif option.upper() == 'N':
        print("You're a boring guy.")
        bye = input("Press any key to exit...")
        if bye == '¯\_(ツ)_/¯':
            quit()
        else:
            quit()
    else:
        print("Couldn't hear you.")
while True:
    ask()
