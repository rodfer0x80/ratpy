from hashlib import pbkdf2_hmac
from os import urandom
# pip install cryptodome
from Crypto.Cipher import AES

class Crypto():
    def __init__(self):
        # password
        self.password = b'highly secure encryption password'
        # --
        self.IV_SIZE = 16    # 128 bit, fixed for the AES algorithm
        self.KEY_SIZE = 32   # 256 bit meaning AES-256, can also be 128 or 192 bits
        self.SALT_SIZE = 16  # This size is arbitrary
        
    def decrypt(self, encrypted):
        salt = encrypted[0:self.SALT_SIZE]

        derived = pbkdf2_hmac('sha256', self.password, salt, 100000,
                                dklen=self.IV_SIZE + self.KEY_SIZE)

        iv = derived[0:self.IV_SIZE]
        key = derived[self.IV_SIZE:]


        plain_text = AES.new(key, AES.MODE_CFB, iv).decrypt(encrypted[self.SALT_SIZE:])

        return plain_text

    def encrypt(self, plain_text):
        salt = urandom(self.SALT_SIZE)

        derived = pbkdf2_hmac('sha256', self.password, salt, 100000,
                                dklen=self.IV_SIZE + self.KEY_SIZE)

        iv = derived[0:self.IV_SIZE]
        key = derived[self.IV_SIZE:]

        encrypted = salt + AES.new(key, AES.MODE_CFB, iv).encrypt(plain_text)

        return encrypted