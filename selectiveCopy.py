#! python3
# By Victour Bue

# Selective Copy
# A program that walks through a folder tree and searches for files with a
# certain file extension (such as .pdf or .jpg). Copy these files from whatever location
# they are in to a new folder.

import os, shutil, pathlib

def prompt():
    print("""
    
    Selective Copy
    This program will walk through a folder tree and search for files with a certain file extension,
    It will then copy these files from whatever location they are in to a new folder.
    
    """)
    response = input("Would you like to do that? ")
    if response.lower() == "yes" or response.lower() =="no":
        return response.lower()
    else:
        print("Please type either yes or no.")
        return prompt()


def getDirectory():
    print("")
    print("Which directory tree would you like to copy?")
    response = input()
    if not os.path.exists(response):
        print("That directory doesn't exist? Please try again.")
        return getDirectory()
    else:
        return response


def getExtension():
    print("")
    print("Which extension would you like to copy?")
    response = input()
    if response[0] != ".":
        response = "." + response
    return response


def copyFiles(folder, ext):

    number = 1

    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Scanning: {foldername}")
        os.chdir(pathlib.Path(__file__).parent.resolve())
        if not os.path.exists(f"{os.getcwd()}\\backups"):
           os.makedirs(f"{os.getcwd()}\\backups")

        for filename in filenames:
            if ext == os.path.splitext(filename)[1]:
                shutil.copyfile(os.path.join(foldername, filename), f"{os.getcwd()}\\backups\{filename}")
                print(f"file copied to: {os.getcwd()}\\backups\{filename}")


def main():
    if prompt() == "no":
        return

    directory = getDirectory()
    extension = getExtension()
    copyFiles(directory, extension)

    return main()


main()
