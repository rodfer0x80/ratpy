from sys import argv, exit, stderr


def get_mod_args():
    argVector = ["master_hostname", "master_port"]
    argCount = len(argVector) + 1 # progname
    return argCount, argVector

def get_configs():
    master_hostname = argv[1]
    master_port = int(argv[2])
    return master_hostname, master_port

def invalid_args_errMsg(argVector):
    args = ""
    for arg in argVector:
        args += " <" + arg + ">"
    errMsg = "Usage ./" + argv[0] + args
    errMsg += "\n"
    return errMsg


def check_args(argCount, argVector):
    if len(argv) != argCount:
        errMsg = invalid_args_errMsg(argVector)
        stderr.write(errMsg)
        exit(0)
    else:
        return 0

def get_args():
    argCount, argVector = get_mod_args()
    if check_args(argCount, argVector) == 0:
        return get_configs()