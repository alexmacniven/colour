from colorama import init, Fore, Style

# Initialise colorama.
init()

# Colour mappings.
colours = {
    'BLACK':   Fore.BLACK,
    'RED':     Fore.RED,
    'GREEN':   Fore.GREEN,
    'YELLOW':  Fore.YELLOW,
    'BLUE':    Fore.BLUE,
    'MAGENTA': Fore.MAGENTA,    
    'CYAN':    Fore.CYAN,
    'WHITE':   Fore.WHITE
}

def normal(s, c):
    return "{}{}{}".format(colours[c], s, Fore.RESET)

def bold(s, c=None):
    if c:
        return "{}{}{}{}".format(
            colours[c], Style.BRIGHT, s, Style.RESET_ALL
        )
    else:
        return "{}{}{}".format(Style.BRIGHT, s, Style.RESET_ALL)
