import json
import os

from colorama.ansi import Fore

from helpers.AsciiCodeFaker.AsciiCodeFaker import AsciiCodeFaker as ACF

menuTypeFile = {"json", "txt"}


class GenerateFile:
    def __init__(self, list_obj):
        self.list_obj = list_obj
        self.file_name = "file_name"
        self.file_type = "txt"

    def menu(self):
        """
            Menu para elegir el tipo de archivo que se quiere generar.
        """

        while True:
            os.system("clear")
            ACF()
            try:
                print(Fore.GREEN + "Type of file to generate\n")
                for menuT in menuTypeFile:
                    print(Fore.RED + f"- {menuT}\n")

                self.file_type = input(Fore.LIGHTBLACK_EX + ":> ").lower()

                if self.file_type in menuTypeFile:
                    print(Fore.GREEN + "\nName of file\n")
                    self.file_name = input(Fore.LIGHTBLACK_EX + ":> ")
                    self.generate_file()
                    break
                else:
                    print(Fore.GREEN + "\nTipo de archivo no soportado\n")
            except ValueError:
                print(Fore.GREEN + "\nTipo de archivo no soportado\n")

    def generate_file(self):
        """
            Genera un archivo json o txt.
        """
        if self.file_type == "json":
            self.generate_json()
        elif self.file_type == "txt":
            self.generate_txt()

    def generate_json(self):
        """
            Genera un archivo json.
        """
        with open(f"{self.file_name}.{self.file_type}", "w") as file:
            json.dump(self.list_obj, file, indent=4)

    def generate_txt(self):
        """
            Genera un archivo txt.
        """
        with open(f"{self.file_name}.{self.file_type}", "w") as file:
            for obj in self.list_obj:
                file.write(obj.__str__() + "\n")

