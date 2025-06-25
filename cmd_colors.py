def red(text): return f"\033[31m{text}\033[0m"
def green(text): return f"\033[32m{text}\033[0m"
def yellow(text): return f"\033[33m{text}\033[0m"
def blue(text): return f"\033[34m{text}\033[0m"
def magenta(text): return f"\033[35m{text}\033[0m"
def cyan(text): return f"\033[36m{text}\033[0m"
def white(text): return f"\033[37m{text}\033[0m"
def black(text): return f"\033[30m{text}\033[0m"
def bright_red(text): return f"\033[91m{text}\033[0m"

def bright_green_start():
     return "\033[92m "
def bright_green_end():
    return "\033[0m"

def bright_green(text): return f"\033[92m{text}\033[0m"


def bright_yellow(text): return f"\033[93m{text}\033[0m"
def bright_blue(text): return f"\033[94m{text}\033[0m"
def bright_magenta(text): return f"\033[95m{text}\033[0m"
def bright_cyan(text): return f"\033[96m{text}\033[0m"
def bright_white(text): return f"\033[97m{text}\033[0m"
def bold(text): return f"\033[1m{text}\033[0m"
def underline(text): return f"\033[4m{text}\033[0m"
def reversed_color(text): return f"\033[7m{text}\033[0m"
def dim(text): return f"\033[2m{text}\033[0m"
def italic(text): return f"\033[3m{text}\033[0m" 
def light_gray(text): 
    return f"\033[38;5;250m{text}\033[0m"

def orange_bold(text):
    return f"\033[38;5;208m\033[1m{text}\033[0m"

