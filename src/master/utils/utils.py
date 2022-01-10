from subprocess import call


def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name =='posix' else 'cls')
