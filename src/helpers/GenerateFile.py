import json
import os

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
            try:
                os.system("clear")
                print("Type of file to generate: ")
                for menuT in menuTypeFile:
                    print(f"- {menuT}")

                self.file_type = input(":> ").lower()

                if self.file_type in menuTypeFile:
                    print("Name of file: ")
                    self.file_name = input(":> ")
                    self.generate_file()
                    break
                else:
                    print("Tipo de archivo no soportado")
            except ValueError:
                print("Tipo de archivo no soportado")

    def generate_file(self):
        """
            Genera un archivo json o txt.
        """
        if self.file_type == "json":
            self.generate_json()
        elif self.file_type == "txt":
            self.generate_txt()
        else:
            print("Tipo de archivo no soportado")

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

