from blessed import Terminal
from pyfiglet import Figlet


def init_menu():
    term = Terminal()
    #print(term.home + term.clear + term.move_y(term.height //2))
    print_title(term)
    print(term.black_on_darkgreen(term.center('Press any key to continue.')))


def print_title(term):
    title = Figlet(font='slant')
    ascii_art = title.renderText('PyStatus').splitlines()
    for line in ascii_art:
        print(term.center(line))