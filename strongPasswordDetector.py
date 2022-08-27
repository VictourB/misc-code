#! python3
# strongPasswordDetector.py - Determines whether or not passwords are secure.
# By Victour Bue

# A program that uses regular expressions to make sure the password string it is
# passed is strong. A strong password is defined as one that is at least eight characters
# long, contains both uppercase and lowercase characters, and has at least one digit.

import re

def prompt():
    print("")
    print('''
    This software will tell you whether or not the inputted password is secure.

    A secure password is defined by being at least eight characters long, 
    containing both uppercase and lowercase characters, and has at least one digit.
    ''')
    password = input("Please enter a password or just 'Enter' to exit: ")
    return password

def analysePassword(text):
    length_regex = re.compile(".{8,}")
    lowercase_regex = re.compile("[a-z]+")
    uppercase_regex = re.compile("[A-Z]+")
    digit_regex = re.compile("[\d]+")

    regex_list = [length_regex,lowercase_regex,uppercase_regex,digit_regex]

    regex_count = 0
    for regex in regex_list:
        if regex.search(text) is None:
            print("")
            print("Sorry but that password isn't secure enough...")
            break
        else:
            regex_count += 1
            continue
    if regex_count == 4:
        print("")
        print("That is a good and secure password in my book!")
        
def main():
    password = prompt()
    if not password:
        return

    analysePassword(password)
    return main()

main()

