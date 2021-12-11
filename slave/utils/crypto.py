from sys import stderr, exit
from os import urandom

from .aes import AES


def crypto_run(crypt, text):
    # key = b'F\xcc\x07\xac:?\xbc.\x12ZX\xec\xa8M>m'
    # aes = AES(key)

    # iv = urandom(16)
    # if crypt == "encrypt":
    #     crypt_text = aes.encrypt_cfb(text, iv)
    # elif crypt == "decrypt":
    #     crypt_text = aes.decrypt_cfb(text, iv)
    # else:
    #     stderr.write("\n[x] Unknown cryptographic operation")
    #     exit(0)
    crypt_text = text
    return crypt_text 
    