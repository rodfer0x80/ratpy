import getpass


KEY = ""

master_hostname = "10.10.10.10"
master_port = 4444


def setup():
    global KEY, master_hostname, master_port
    key = getpass.getpass("Encryption password: ")
    if len(key) < 1:
        print("Password must be set")
        exit(0)
    KEY = bytes(key, 'utf-8')
    master_hostname = input("Enter master hostame [10.10.10.10]: ")
    if master_hostname == "":
        master_hostname = "0.0.0.0"
    master_port = input("Enter master connection port [4444]: ")
    if master_port == "" or int(master_port) == 4444:
        master_port = 4444
    else:
        try:
            master_port = int(master_port)
        except:
            print("Invalid port type, must be integer")
            exit(0)
