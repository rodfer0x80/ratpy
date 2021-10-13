from time import sleep
from os import system

class Menu():
    def __init__(self, cons, addrs, ip_addr, port, shell_port):
        self.cons = cons 
        self.addrs = addrs
        self.ip_addr = ip_addr
        self.port = port 
        self.shell_port = shell_port

    
    def display_menu(self):
        print("==== Backdoor Main Menu ====")
        print("     ==================     ")
        print("l  --  list connections")
        print("x  --  execute backdoor")
        print("q  --  quit program")

    def wait_cmd(self):
        cmd = ""
        while cmd == "":
            cmd = input(">>> ")
        return cmd

    def list_connections(self):
            i = 0
            for addr in self.addrs:
                i += 1
                print("%d  --  %s  --  %d" % (i, addr[0], addr[1]))

    def execute_backdoor(self):
        self.list_connections()
        self.wait_cmd()
        con = self.cons[cmd]
        backdoor = Backdoor(con, self.ip_addr, self.port, self.shell_port)
        backdoor.cmd_shell()
            
    def execute_cmd(self, cmd):
        if cmd == "q":
            exit(0)
        elif cmd == "l":
            print("connections")
        elif cmd == "x":
            self.execute_backdoor()
        else:
            print("[x] Invalid command")
            sleep(0.5)
            self.main_menu()

    def main_menu(self):
        #system("clear")
        self.display_menu()
        cmd = self.wait_cmd()
        self.execute_cmd(cmd)