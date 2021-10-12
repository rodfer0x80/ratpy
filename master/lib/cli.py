from sys import argv, exit, stderr

class CLI():
    def __init__(self):
        self.get_configs()
    
    def get_mod_args(self):
        self.argVector = ["ip_addr", "port", "shell_port"]
        self.argCount = len(self.argVector)

    def get_args(self):
        self.ip_addr = argv[1]
        self.port = int(argv[2])
        self.shell_port = int(argv[3])

    def invalid_args_errMsg(self):
        args = ""
        for arg in self.argVector:
            args += " <" + arg + ">"
        errMsg = "Usage ./" + argv[0] + args + "\n"
        return errMsg


    def check_args(self):
        if len(argv) != self.argCount+1:
            errMsg = self.invalid_args_errMsg()
            stderr.write(errMsg)
            return 1
        else:
            return 0


    def get_configs(self):
        self.get_mod_args()
        if self.check_args() == 0:
            self.get_args()
