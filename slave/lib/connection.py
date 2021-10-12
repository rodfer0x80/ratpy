from socket import socket, AF_INET, SOCK_STREAM
from socket import error as socket_error
from sys import exit
from os import fork

class Connection():
    def __init__(self, master_hostname, master_port):
        self.master_hostname = master_hostname
        self.master_port = master_port

    def connect_master(self):
        pid = fork()
        if pid == 0:
            pid2 = fork()
            if pid2 == 0:
                try:
                    self.conn = socket(AF_INET, SOCK_STREAM)
                    self.conn.connect((self.master_hostname, self.master_port))
                except socket_error:
                    # error creating socket or connecting
                    self.connect_master()
                
            else:
                exit(0)
        else:
            exit(0)