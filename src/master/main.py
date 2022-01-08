#!/usr/bin/python3

from threadpool.threadpool import threadpool_run
from utils.configs import *


if __name__ == "__main__":
    global KEY
    setup()
    threadpool_run()
