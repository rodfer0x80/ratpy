from sys import argv, stderr

class CLI():

    def __init__(self):
        self.get_configs()

    def get_mod_args(self):
        argVector = ["master_hostname", "master_port"]
        argCount = len(argVector) + 1 # progname
        return argCount, argVector

    def get_args(self):
        self.master_hostname = argv[1]
        self.master_port = int(argv[2])

    def invalid_args_errMsg(self, argVector):
        args = ""
        for arg in argVector:
            args += " <" + arg + ">"
        errMsg = "Usage ./" + argv[0] + args
        errMsg += "\n"
        return errMsg

    def check_args(self, argCount, argVector):
        if len(argv) != argCount:
            errMsg = self.invalid_args_errMsg(argVector)
            stderr.write(errMsg)
            exit(0)
        else:
            return 0

    def get_configs(self):
        argCount, argVector = self.get_mod_args()
        if self.check_args(argCount, argVector) == 0:
            self.get_args()
