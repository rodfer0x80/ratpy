import threading
from queue import Queue
from sys import exit
from time import sleep

from utils.args import get_args
from utils.connection import estabilish_connection
from interface.menu import main_menu


n_threads = 2
jobs = [1, 2]
queue = Queue()

addrs = []
cons = []

ip_addr, port, shell_port = get_args()


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


def threadpool_run():
    create_threads()
    create_jobs()