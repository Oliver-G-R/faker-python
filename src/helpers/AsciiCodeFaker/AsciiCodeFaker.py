import os
from colorama import init, Fore


def AsciiCodeFaker():
    init(autoreset=True)
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, "fakertxtConsole.txt")

    with open(my_file, "r") as f:
        for line in f:
            print(Fore.RED + line)
