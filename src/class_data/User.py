import os
from colorama.ansi import Fore
from faker import Faker
from helpers.AsciiCodeFaker.AsciiCodeFaker import AsciiCodeFaker as ACF
from helpers.GenerateFile import GenerateFile
from models.userModel import modelUser

fake = Faker()

options = {"1", "2", "3"}


class User:
    def __init__(self):
        self.users = []
        self.emails = []
        self.passwords = []

    def showDataGenerated(self, data):
        os.system("clear")
        ACF()
        print(Fore.GREEN + "\n=== Data generated ===\n")

        if isinstance(data[0], dict):
            for i in data:
                for key in i:
                    print(Fore.RED + key, ":", i[key])
                print(Fore.GREEN + "\n===============\n")
        else:
            for user in data:
                print(Fore.RED + user)
                print(Fore.GREEN + "\n===============\n")

    def questSaveInFile(self, data):
        print(Fore.GREEN + "\nDo you want to save the file? [s][n]\n")
        option = input(Fore.LIGHTBLACK_EX + ":> ").lower()
        if option == "s":
            gFile = GenerateFile(data)
            gFile.menu()
        os.system("clear")

    def menu(self):
        tryAgain = True
        optionTrAgain = {"y", "n"}
        while tryAgain:
            while True:
                os.system("clear")
                ACF()
                print(
                    Fore.RED
                    + """
                        1. Generate Fast User
                        2. Generate Email
                        3. Generate Password
                    """
                )

                op = input(Fore.LIGHTBLACK_EX + ":> ")

                if op in options:
                    if op == "1":
                        self.generateFastUser()
                    elif op == "2":
                        self.generateEmail()
                    elif op == "3":
                        self.generatePassword()
                    break

            print(Fore.GREEN + "\nDo you want to try again? [s][n]\n")
            tryAgain = input(Fore.LIGHTBLACK_EX + ":> ").lower()

            if tryAgain in optionTrAgain:
                if tryAgain == "s":
                    tryAgain = True
                elif tryAgain == "n":
                    tryAgain = False
                break

    def generateFastUser(self):
        print(Fore.GREEN + "\nHow many users do you want to generate?\n")
        amount = int(input(Fore.LIGHTBLACK_EX + ":> "))

        for user in range(amount):
            self.users.append(modelUser())

        self.showDataGenerated(self.users)
        self.questSaveInFile(self.users)
        self.users.clear()

    def validateNUmber(self):
        try:
            number = int(input(Fore.LIGHTBLACK_EX + ":> "))
            return number
        except ValueError:
            return False

    def generateEmail(self):
        while True:
            print(Fore.GREEN + "\nHow many emails do you want to generate?\n")
            amount = self.validateNUmber()
            if amount:
                for email in range(amount):
                    self.emails.append(fake.free_email())

                self.showDataGenerated(self.emails)
                self.questSaveInFile(self.emails)
                self.emails.clear()
                break

    def generatePassword(self):
        while True:
            print(Fore.GREEN + "\nHow many passwords do you want to generate?\n")
            amount = self.validateNUmber()
            if amount:
                print(
                    Fore.GREEN
                    + "\nDo you want to complete some password options? [s][n]\n"
                )
                op = input(Fore.LIGHTBLACK_EX + ":> ").lower()

                if op == "s":
                    print(Fore.GREEN + "\nLength\n")
                    length = int(input(Fore.LIGHTBLACK_EX + ":> "))

                    print(Fore.GREEN + "\nSpecial characters: [s][n]\n")
                    special_chars = input(Fore.LIGHTBLACK_EX + ":> ").lower() == "s"

                    print(Fore.GREEN + "\nDigits: [s][n]\n")
                    digits = input(Fore.LIGHTBLACK_EX + ":> ").lower() == "s"

                    print(Fore.GREEN + "\nUpper case: [s][n]\n")
                    upper_case = input(Fore.LIGHTBLACK_EX + ":> ").lower() == "s"

                    print(Fore.GREEN + "\nLower case: [s][n]\n")
                    lower_case = input(Fore.LIGHTBLACK_EX + ":> ").lower() == "s"

                    for password in range(amount):
                        self.passwords.append(
                            fake.password(
                                length=length,
                                special_chars=special_chars,
                                digits=digits,
                                upper_case=upper_case,
                                lower_case=lower_case,
                            )
                        )

                    self.showDataGenerated(self.passwords)
                    self.questSaveInFile(self.passwords)
                    self.passwords.clear()
                    break
                else:
                    for password in range(amount):
                        self.passwords.append(fake.password())
                    self.showDataGenerated(self.passwords)
                    self.questSaveInFile(self.passwords)
                    self.passwords.clear()
                    break
