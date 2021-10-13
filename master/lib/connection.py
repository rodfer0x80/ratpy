from socket import socket, SOL_SOCKET, SO_REUSEADDR
from socket import error as socket_error
from sys import stderr, exit
from os import system

class Connection():

    def __init__(self, ip_addr, port):
        self.ip_addr = ip_addr
        self.port = port

    def create_socket(self):
        try:
            self.socketObj = socket()
            self.socketObj.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        except socket_error:
            stderr.write("[x] Error creating socket object\n")
            exit(0)

    def socket_bind(self):
        try:
            system("clear")
            print("[*] Listening on port %d" % self.port)
            self.socketObj.bind((self.ip_addr, self.port))
            self.socketObj.listen(20)
        except socket_error:
            stderr.write("[x] Error binding socket object")
            #exit(0)
            self.socket_bind()

    def socket_accept(self):
        try:
            conn, addr = self.socketObj.accept()
            conn.setblocking(1) # no timeout

            #system("clear")
            print("[+] Connection estabilished with %s:%d\n\n\n" % (addr[0], addr[1]))
        except socket_error:
            stderr.write("[x] Error connecting to slave\n")
            #exit(0)
        return conn, addr

    def connect(self):
        self.create_socket()
        self.socket_bind()
        conn, addr = self.socket_accept()
        return conn, addr