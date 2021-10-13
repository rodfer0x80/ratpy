from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from socket import error as socket_error
from sys import stderr, exit
from os import system

class Connection():

    def __init__(self, ip_addr, port):
        self.ip_addr = ip_addr
        self.port = port
        try:
            self.socketObj = socket(AF_INET, SOCK_STREAM)
            self.socketObj.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        except socket_error:
            stderr.write("[x] Error creating socket object\n")
            exit(0)

    def socket_bind(self):
        try:
            self.socketObj.bind((self.ip_addr, self.port))
        except socket_error:
            stderr.write("[x] Error binding socket object")
            exit(0)

    def socket_listen(self, n=20):
        try:
            #system("clear")
            print("[*] Listening on port %d" % self.port)
            self.socketObj.listen(n)
        except socket_error:
            stderr.write("[x] Error broadcasting server\n")
            exit(0)

    def socket_accept(self):
        try:
            self.conn, self.addr = self.socketObj.accept()
            self.conn.setblocking(1) # no timeout

            #system("clear")
            print("[+] Connection estabilished with %s:%d\n\n\n" % (self.addr[0], self.addr[1]))
        except socket_error:
            stderr.write("[x] Error connecting to slave\n")
            exit(0)

    def connect(self):
        self.socket_bind()
        self.socket_listen()
        self.socket_accept()
        return self.conn, self.addr