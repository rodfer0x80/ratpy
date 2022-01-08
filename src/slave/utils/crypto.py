def xor(left_data, right_data):
    return bytearray(l^r for l, r in zip(*map(bytearray, [left_data, right_data])))

def encrypt(in_data):
    global KEY
    return xor(in_data.encode("utf-8"), KEY)

def decrypt(in_data):
    global KEY
    return xor(in_data, KEY).decode()
