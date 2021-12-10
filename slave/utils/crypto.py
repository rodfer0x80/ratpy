from hashlib import pbkdf2_hmac
from os import urandom
from sys import stderr, exit


# locally import this so it can be written in the obfuscated script
from Crypto.Cipher import AES


def crypto_run(crypt, text):
    password = b'highly secure encryption password'    
    IV_SIZE = 16    # 128 bit, fixed for the AES algorithm
    KEY_SIZE = 32   # 256 bit meaning AES-256, can also be 128 or 192 bits
    SALT_SIZE = 16  # This size is arbitrary

    if crypt == "encrypt":
        crypt_text = crypto_encrypt(password, text, IV_SIZE, KEY_SIZE, SALT_SIZE)
    elif crypt == "decrypt":
        crypt_text = crypto_decrypt(password, text, IV_SIZE, KEY_SIZE, SALT_SIZE)
    else:
        stderr.write("\n[x] Unknown cryptographic operation")
        exit(0)
    return crypt_text   


def crypto_decrypt(password, text, IV_SIZE, KEY_SIZE, SALT_SIZE):
    salt = text[0:SALT_SIZE]
    derived = pbkdf2_hmac('sha256', password, salt, 100000,
                                dklen=IV_SIZE + KEY_SIZE)
    iv = derived[0:IV_SIZE]
    key = derived[IV_SIZE:]
    plain_text = AES.new(key, AES.MODE_CFB, iv).decrypt(text[SALT_SIZE:])
    return plain_text


def crypto_encrypt(password, text, IV_SIZE, KEY_SIZE, SALT_SIZE):
    salt = urandom(SALT_SIZE)
    derived = pbkdf2_hmac('sha256', password, salt, 100000,
                                dklen=IV_SIZE + KEY_SIZE)
    iv = derived[0:IV_SIZE]
    key = derived[IV_SIZE:]
    encrypted = salt + AES.new(key, AES.MODE_CFB, iv).encrypt(text)
    return encrypted