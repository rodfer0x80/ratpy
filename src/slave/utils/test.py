import getpass


def xor(left_data, right_data):
    return bytearray(l^r for l, r in zip(*map(bytearray, [left_data, right_data])))


def encrypt(in_data):
    global KEY
    return xor(in_data.encode("utf-8"), KEY)


def decrypt(in_data):
    global KEY
    return xor(in_data, KEY).decode()


if __name__ == "__main__":
    global KEY
    KEY = getpass.getpass("passwd: ")
    KEY = KEY.encode("utf-8")

    msg = "hello world"
    print("msg: ", msg)
    
    cypher = encrypt(msg)
    print("cypher: ", str(cypher))
    
    txt_msg = decrypt(cypher)
    print("txt_msg: ", txt_msg)
