import os
import hashlib 
from Crypto.Cipher import AES

def padding(text):
    plength = 16 - (len(text) % 16)
    ptext = text + bytes([plength] * plength)
    return ptext

def unpadding(text):
    plength=text[-1]
    return text[:-plength]


def aes_encrypt (infile,outfile,key):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(infile,"rb") as i:
        with open(outfile,"wb") as o:
            text=i.read()
            o.write(cipher.encrypt(padding(text)))

def aes_decrypt(outfile,infile,key):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(infile,"rb") as i:
        with open(outfile,"wb") as o:
            text=i.read()
            o.write(unpadding(cipher.decrypt(text)))

key = b"1234123412341234"

#aes_encrypt ("a:/workflows/workflows 001 - ainshmas/ainshams 051 - computer and network security/projects/phase2/decrypt.txt","a:/workflows/workflows 001 - ainshmas/ainshams 051 - computer and network security/projects/phase2/encrypt.txt",key)
aes_decrypt ("a:/workflows/workflows 001 - ainshmas/ainshams 051 - computer and network security/projects/phase2/decrypt.txt","a:/workflows/workflows 001 - ainshmas/ainshams 051 - computer and network security/projects/phase2/encrypt.txt",key)