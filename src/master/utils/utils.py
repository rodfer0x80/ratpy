from subprocess import call
from os import name


def clear():
    # check and make call for specific operating system
    _ = call('clear' if name =='posix' else 'cls')
