#!/bin/usr/python3

from lib.threadpool import Threadpool

def main():
    threadpool = Threadpool()
    threadpool.run_app()
    return 0
    

if __name__ == "__main__":
    main()
