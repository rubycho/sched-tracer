CAPTURE_DIR = './captures'
NO_SUDO = False

# helpers
def print_info(str):
    print("[INFO] {}".format(str))

def print_warn(str):
    print("[WARN] {}".format(str))

def print_error(str):
    print("[ERROR] {}".format(str))

def sudo(str):
    if NO_SUDO:
        return str
    return "sudo {}".format(str)
