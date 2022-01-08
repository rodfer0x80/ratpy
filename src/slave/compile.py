#!/usr/bin/python3
import getpass


def setup():
    key = getpass.getpass("Encryption password: ")
    if len(key) < 1:
        print("Password must be set")
        exit(0)
    KEY = bytes(key, 'utf-8')
    master_hostname = input("Enter master hostname [10.10.10.10]: ")
    if master_hostname == "":
        master_hostname = "10.10.10.10"
    port = input("Enter master connection port [4444]: ")
    if master_port == "" or int(master_port) == 4444:
        master_port = 4444
    else:
        try:
            master_port = int(master_port)
        except:
            print("Invalid port type, must be integer")
            exit(0)
    return KEY, master_hostname, master_port
    

def edif_configs(KEY, master_hostname, master_port):
    with open("main.py", "r") as fp:
        code = fp.read()
    new_code = ""
    for line in code.split("\n"):
        if "KEY = " in line:
            line = f"KEY = \"{KEY}\""
        if "master_hostname = " in line:
            line = f"master_hostname = \"{master_hostname}\""
        if "master_port = " in line:
            line = f"master_port = {master_port}"
        new_code += f"{line}\n"
    with open("main.py.tmp", "w") as fp:
        fp.write(new_code)
    rename("main.py.tmp", "main.py")


if __name__ == '__main__':
    KEY, ip_addr, port = setup()
    edit_configs(KEY, ip_addr, port)
