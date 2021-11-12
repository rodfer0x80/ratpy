#!/bin/usr/python3

from lib.args import *
from lib.connection import *
from lib.menu import *

def main():
    cons = []
    addrs = []
    ip_addr, port, shell_port = get_args()
    conn, addr = estabilish_connection(ip_addr, port)
    cons.append(conn)
    addrs.append(addr)
    main_menu(cons, addrs, ip_addr, port, shell_port)
    return 0
    

if __name__ == "__main__":
    main()
