import os
from class_data.User import User

options = {"usrs"}

while True:
    os.system("clear")
    print("=== Select generate data ===")
    for option in options:
        print(f"- [{option}]")

    op = input(":> ").lower()

    if op in options:
        os.system("clear")
        if op == "usrs":
            user = User()
            user.menu()
            break

    else:
        print("Invalid option")

