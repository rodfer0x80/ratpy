#!/usr/bin/python3

from threadpool.threadpool import threadpool_run


def main():
    global KEY
    key = getpass.getpass("Encryption Password >>> ")
    KEY = bytes(key, 'utf-8')
    threadpool_run()
    return 0
    

if __name__ == "__main__":
    main()
