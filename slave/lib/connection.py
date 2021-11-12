from socket import socket, AF_INET, SOCK_STREAM
from socket import error as socket_error
from sys import exit
from os import fork


def connect_master(master_hostname, master_port):
    pid = fork()
    if pid == 0:
        pid2 = fork()
        if pid2 == 0:
            try:
                conn = socket(AF_INET, SOCK_STREAM)
                conn.connect((master_hostname, master_port))
            except socket_error:
                # error creating socket or connecting
                #connect_master(master_hostname, master_port)
                exit(0)
        else:
            exit(0)
    else:
        exit(0)
    return conn
