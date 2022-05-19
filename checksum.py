import hashlib as hl
import binascii as ba
import os

def checksum(filename):
    try:
        with open(f"{filename}", "rb") as f:
            file = f.read(131072)
            sha1 = hl.sha1(file).hexdigest()
            sha256 = hl.sha256(file).hexdigest()
            sha512 = hl.sha512(file).hexdigest()
            md5 = hl.md5(file).hexdigest()
            crc32 = (ba.crc32(file))
            print(f'''Checksums for "{filename}":\nSHA1: {sha1}\nSHA256: {sha256}'''
            f"\nSHA512: {sha512}\nMD5: {md5}\nCRC32: {crc32 & 0xFFFFFFFF:08x}")
    except FileNotFoundError:
        print(f'''"{filename}" isn't a file.''')
def ask():
    option = input("Do you want to calculate the checksum of a file? (Y/N): ")
    if option.upper() == 'Y':
        file = input("What's the file you want to check out? ")
        checksum(file)
    elif option.upper() == 'N':
        print("You're a boring guy.\n")
        bye = input("Press the Enter key to exit\n")
        if bye == '( ͡° ͜ʖ ͡°)':
            os._exit(0)
        else:
            os._exit(0)
    else:
        print("Couldn't hear you.")
while True:
    ask()