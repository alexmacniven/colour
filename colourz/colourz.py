from colorama import init, Fore, Style

# Initialise colorama.
init()

# Colour mappings.
colours = {
    'RED': Fore.RED,
    'GREEN': Fore.GREEN,
    'CYAN': Fore.CYAN,
    'BLUE': Fore.BLUE
}

class Colourz(object):
    """The Colour class."""

    @staticmethod
    def normal(s, c):
        return "{}{}{}".format(colours[c], s, Fore.RESET)

    @staticmethod
    def bold(s, c=None):
        if c:
            return "{}{}{}{}".format(
                colours[c], Style.BRIGHT, s, Style.RESET_ALL
            )
        else:
            return "{}{}{}".format(Style.BRIGHT, s, Style.RESET_ALL)