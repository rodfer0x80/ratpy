from hashlib import pbkdf2_hmac
from Crypto.Cipher import AES


def decrypt(encrypted):
    global KEY
    salt = encrypted[0:SALT_SIZE]

    derived = pbkdf2_hmac('sha256', KEY, salt, 100000,
                              dklen=IV_SIZE + KEY_SIZE)

    iv = derived[0:IV_SIZE]
    key = derived[IV_SIZE:]


    msg = AES.new(key, AES.MODE_CFB, iv).decrypt(encrypted[SALT_SIZE:])

    return msg

def encrypt(msg):
    global KEY
    salt = urandom(SALT_SIZE)

    derived = pbkdf2_hmac('sha256', KEY, salt, 100000,
                              dklen=IV_SIZE + KEY_SIZE)

    iv = derived[0:IV_SIZE]
    key = derived[IV_SIZE:]

    encrypted = salt + AES.new(key, AES.MODE_CFB, iv).encrypt(msg)

    return encrypted
