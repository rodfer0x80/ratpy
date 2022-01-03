from socket import socket, SOL_SOCKET, SO_REUSEADDR
from socket import error as socket_error
from sys import stderr, exit
from os import system


def create_socket():
    try:
        socketObj = socket()
        socketObj.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    except socket_error:
        stderr.write("[x] Error creating socket object\n")
        exit(0)
    return socketObj


def socket_bind(socketObj, ip_addr, port):
    try:
        system("clear")
        print("[*] Listening on port %d" % port)
        socketObj.bind((ip_addr, port))
        socketObj.listen(5)
    except socket_error:
        stderr.write("[x] Error binding socket object")
        socketObj = socket_bind(ip_addr, port)
    return socketObj


def socket_accept(socketObj):
    try:
        conn, addr = socketObj.accept()
        conn.setblocking(1) # no timeout
        print("[+] Connection estabilished with %s:%d\n\n\n" % (addr[0], addr[1]))
    except socket_error:
        stderr.write("[x] Error connecting to slave\n")
    return conn, addr


def estabilish_connection(ip_addr, port):
    socketObj = create_socket()
    socketObj = socket_bind(socketObj, ip_addr, port)
    conn, addr = socket_accept(socketObj)
    return conn, addr