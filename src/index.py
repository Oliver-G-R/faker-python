import os
from class_data.User import User
from helpers.AsciiCodeFaker.AsciiCodeFaker import AsciiCodeFaker as ACF
from colorama import Fore

options = {"usrs"}

while True:
    os.system("clear")

    ACF()

    print(Fore.GREEN + "\nWelcome to the FakerPy Console!\n")

    for option in options:
        print(Fore.RED + f"\n- [{option}]\n")

    op = input(Fore.LIGHTBLACK_EX + ":> ").lower()

    if op in options:
        os.system("clear")
        if op == "usrs":
            user = User()
            user.menu()
            break

    else:
        print("Invalid option")

