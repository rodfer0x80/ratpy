from sys import stderr, exit
from os import urandom

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# make diffie helman key exchange
# then use only one key for communication
def make_exchange():
    secret_code = "cryptopunks"
    key = RSA.generate(2048)
    encrypted_key = key.export_key(passphrase=secret_code, pkcs=8,
                              protection="scryptAndAES128-CBC")
    return encrypted_key


# encrypt data based on command if fail enter debug mode waiting for command
def crypto_debug(in_data, key):
    crypt = input("Enter 0 to encrypt or 1 to decrypt")
    if crypt == "0":
        out_data = crypto_encrypt(in_data, key)
    elif crypt == "1":
        out_data = crypto_decrypt(in_data, key)
    else:
        return crypto_debug(in_data, key)
    return out_data, key

def crypto_run(crypt, in_data, key):
    if crypt == "encrypt":
        out_data = crypto_encrypt(in_data, key)
    elif crypt == "decrypt":
        out_data = crypto_decrypt(in_data, key)
    else:
        sys.stderr.write("[x] Fatal encrypting data, wrong command")
        return crypto_debug(in_data, key)
    return out_data, key
