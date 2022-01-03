key = bytearray(b'\x63\x72\x79\x70\x74\x6f\x70\x75\x6e\x6b\x73')

def xor(left_data, right_data):
    return bytearray(l^r for l, r in zip(*map(bytearray, [left_data, right_data])))

def encrypt(in_data, key):
    return xor(in_data.encode("utf-8"), key)

def decrypt(in_data, key):
    return xor(in_data, key).decode()
