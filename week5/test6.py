from sys import argv
from shutil import copyfile

try:
    original_file = argv[1]
    filename, ext = original_file.split('.')
    backup_file = (f"{filename}_backup.{ext}")

    copyfile(original_file, backup_file)

except IndexError:
    print("Please provide the filename")

except FileNotFoundError:
    print(f"{original_file} cannot be found.")

except ValueError:
    print("File extension cannot be found.")