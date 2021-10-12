from sys import argv, stderr

class CLI():

    def __init__(self):
        self.get_configs()

    def get_mod_args(self):
        self.argVector = ["master_hostname", "master_port"]
        self.argCount = len(self.argVector) + 1

    def get_args(self):
        self.master_hostname = argv[1]
        self.master_port = int(argv[2])

    def invalid_args_errMsg(self):
        args = ""
        for arg in self.argVector:
            args += " <" + arg + ">"
        errMsg = "Usage ./" + argv[0] + args
        return errMsg

    def check_args(self):
        if len(argv) != self.argCount:
            errMsg = self.invalid_args_errMsg(self.argVector)
            stderr.write(errMsg)
            return 1
        else:
            return 0

    def get_configs(self):
        self.get_mod_args()
        if self.check_args() == 0:
            self.get_args()
