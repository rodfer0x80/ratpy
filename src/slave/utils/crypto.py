from hashlib import pbkdf2_hmac
from Crypto.Cipher import AES
from os import urandom


IV_SIZE = 16    # 128 bit, fixed for the AES algorithm
KEY_SIZE = 32   # 256 bit meaning AES-256, can also be 128 or 192 bits
SALT_SIZE = 16  # This size is arbitrary


def decrypt(encrypted, KEY):
    global IV_SIZE, SALT_SIZE, KEY_SIZE
    salt = encrypted[0:SALT_SIZE]

    derived = pbkdf2_hmac('sha256', KEY, salt, 100000,
                              dklen=IV_SIZE + KEY_SIZE)

    iv = derived[0:IV_SIZE]
    key = derived[IV_SIZE:]


    msg = AES.new(key, AES.MODE_CFB, iv).decrypt(encrypted[SALT_SIZE:])

    return msg

def encrypt(msg, KEY):
    global IV_SIZE, SALT_SIZE, KEY_SIZE
    salt = urandom(SALT_SIZE)

    derived = pbkdf2_hmac('sha256', KEY, salt, 100000,
                              dklen=IV_SIZE + KEY_SIZE)

    iv = derived[0:IV_SIZE]
    key = derived[IV_SIZE:]

    encrypted = salt + AES.new(key, AES.MODE_CFB, iv).encrypt(msg)

    return encrypted
