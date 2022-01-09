from hashlib import pbkdf2_hmac
from Crypto.Cipher import AES
from os import urandom


KEY = "secretkeyofsp"
IV_SIZE = 16    # 128 bit, fixed for the AES algorithm
KEY_SIZE = 32   # 256 bit meaning AES-256, can also be 128 or 192 bits
SALT_SIZE = 16  # This size is arbitrary


TEST_TOTAL = 2
TEST_COUNT = 0


def crypto_decrypt(ciphertext):
    passwd = KEY.encode('utf-8')
    salt = ciphertext[0:SALT_SIZE]
    derived = pbkdf2_hmac('sha256', passwd, salt, 100000,
                          dklen=IV_SIZE + KEY_SIZE)
    iv = derived[0:IV_SIZE]
    key = derived[IV_SIZE:]
    msg = AES.new(key, AES.MODE_CFB, iv).decrypt(ciphertext[SALT_SIZE:])
    return msg


def crypto_encrypt(text):
    passwd = KEY.encode('utf-8')
    salt = urandom(SALT_SIZE)
    derived = pbkdf2_hmac('sha256', passwd, salt, 100000,
                          dklen=IV_SIZE + KEY_SIZE)

    iv = derived[0:IV_SIZE]
    key = derived[IV_SIZE:]

    encrypted = salt + AES.new(key, AES.MODE_CFB, iv).encrypt(text)

    return encrypted


if __name__ == '__main__':
    msg1 = "test"
    msg2 = "testtesttesttesttesttesttesttest"
    cipher1 = crypto_encrypt(msg1.encode("utf-8"))
    cipher2 = crypto_encrypt(msg2.encode("utf-8"))
    if msg1 != crypto_decrypt(cipher1).decode("utf-8") or msg2 != crypto_decrypt(cipher2).decode("utf-8"):
        print("[x] encryption/decryption scheme not returning expected results")
    else:
        print("[*] encryption/decryption scheme seems to be working correctly")
