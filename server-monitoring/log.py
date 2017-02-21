from sys import stdout

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BUTTON_GREY = '\x1b[0;30;47m'
    BUTTON_RED = '\x1b[0;37;41m'
    BUTTON_GREEN = '\x1b[0;37;42m'
    BUTTON_RED_DISABLED = '\x1b[2;31;41m'
    BUTTON_GREEN_DISABLED = '\x1b[2;32;42m'

def colorText( color, string):
    return color + string + Colors.RESET

def printStatusText( succesfull) :
    if succesfull :
        stdout.write(colorText(Colors.BUTTON_GREEN, "  OK  "))
        stdout.write(colorText(Colors.BUTTON_RED_DISABLED, " NOK "))
    else :
        stdout.write(colorText(Colors.BUTTON_GREEN_DISABLED, "  OK  "))
        stdout.write(colorText(Colors.BUTTON_RED, " NOK "))
