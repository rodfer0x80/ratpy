
class Obfuscator():
    def __init__(self):
        self.lib = ""
        self.main = ""
        self.script = ""
        self.shadowed = ""

    def shadow(self):
        self.shadow_imports()
        self.shadow_objects()
        self.shadow_vars()
        self.shadow_function()
    
    #def build_script(self):

    def obfuscate(self):
        self.build_lib()
        self.build_main()
        self.shadow()
        self.build_script()
        self.shadow()
