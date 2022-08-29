#! python3
# Regex Search - A program that opens all .txt files in a folder and searches for any line 
# that matches a user-supplied regular expression.
# By Victour Bue

import re, os

def prompt():
    print("\n This program opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. \n")
    response = input("Would you like to do this? ")
    if response.lower() == "yes" or response.lower() == "no":
        return response
    else:
        print("I only understand yes or no, please try again.")
        return prompt()


def getDirectory():
    print("Which directory would you like to search?")
    dir = input()
    if not os.path.exists(dir):
        print("I'm sorry but that directory does not exist. ")
        print("Please try again. ")
        return getDirectory()
    elif not os.listdir(dir) :
        print("There are no items in that directory. ")
        print("Please try again. ")
        return getDirectory()
    else:
        return dir
        

def getRegex():
    print("Please enter the regular expression that you would like to search. ")
    regex = input()
    try:
        pattern = re.compile(regex)
        return pattern
    except re.error:
        print("That is not a valid regular expression. ")
        return getRegex()
      

def search(dir, reg):
    files = os.listdir(dir)
    for file in files:
        print(f"working on {os.path.join(dir, file)}")
        print("")
        if os.path.isfile(os.path.join(dir, file)):
            ext = os.path.splitext(file)[1]
            if ext == ".txt":
                openedFile = open(os.path.join(dir, file))
                number_of_matches = 0
                for line in openedFile.readlines():
                    if reg.search(line):
                        number_of_matches += 1
                        print(f""" "{line.strip()}" """)
                print(str(number_of_matches) + " Matches Found")
                print("")
                openedFile.close()
            else:
                print("That is not a .txt file, I'm skipping it. ")
                print("")
        else:
            print("That is not a file, I'm skipping it. ")
            print("")


def main():
    if prompt() == "no":
        return

    searchDir = getDirectory()
    pattern = getRegex()
    search(searchDir, pattern)

    return main()


main()