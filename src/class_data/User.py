import json
import os
from faker import Faker
from helpers.GenerateFile import GenerateFile
from models.userModel import modelUser

fake = Faker()

options = {"1", "2", "3"}


class User:
    def __init__(self):
        self.users = []
        self.emails = []
        self.passwords = []

    def questSaveInFile(self, data):
        print("Do you want to save the file? [s][n]")
        option = input(":> ").lower()
        if option == "s":
            gFile = GenerateFile(data)
            gFile.menu()

    def menu(self):
        tryAgain = True
        print("=== Generate users ===")
        while tryAgain:
            while True:
                os.system("clear")
                print(
                    """
                        1. Generate Fast User
                        2. Generate Email
                        3. Generate Password
                    """
                )

                op = input(":> ")

                if op in options:
                    if op == "1":
                        self.generateFaztUser()
                    elif op == "2":
                        self.generateEmail()
                    elif op == "3":
                        self.generatePassword()
                    break

            tryAgain = input("Do you want to try again? (y/n) ")

            if tryAgain == "y":
                tryAgain = True
            else:
                tryAgain = False

    def generateFastUser(self):
        print("How many users do you want to generate?")
        amount = int(input(":> "))

        for user in range(amount):
            self.users.append(modelUser())

        print(json.dumps(self.users, sort_keys=False, indent=4))
        self.questSaveInFile(self.users)
        self.users.clear()

    def generateEmail(self):
        print("How many emails do you want to generate?")
        amount = int(input(":> "))
        for email in range(amount):
            self.emails.append(fake.email())

        print(self.emails)
        self.questSaveInFile(self.emails)
        self.emails.clear()

    def generatePassword(self):
        print("How many passwords do you want to generate?")
        amount = int(input(":> "))

        print("Do you want to complete some password options? [s][n] ")
        op = input(":> ").lower()

        if op == "s":
            print("Length: ")
            length = int(input(":> "))

            print("Special characters: [s][n]")
            special_chars = input(":> ").lower() == "s"

            print("Digits: [s][n]")
            digits = input(":> ").lower() == "s"

            print("Upper case: [s][n]")
            upper_case = input(":> ").lower() == "s"

            print("Lower case: [s][n]")
            lower_case = input(":> ").lower() == "s"

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
            print(self.passwords)
            self.questSaveInFile(self.passwords)
            self.passwords.clear()
        else:
            for password in range(amount):
                self.passwords.append(fake.password())
            print(self.passwords)
            self.questSaveInFile(self.passwords)
            self.passwords.clear()
