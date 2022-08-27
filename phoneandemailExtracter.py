#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
# by Victour Bue

import pyperclip, re

def prompt():
    # Explain program and get consent or exit
    print('''
    This program will take the contents of your clipboard and search for all phone numbers and email address. 
    It will then paste only those values back into the clipboard
    ''')
    consent = input("Would you like to do that? yes/no \n")
    consent_lower = consent.lower()
    
    if consent_lower == "no" or consent_lower == "yes":
        return consent_lower
    else:
        print("")
        print("Please enter yes or no.")
        return prompt()


def getText():
    text = pyperclip.paste()
    return text

def findPhoneandEmails(text):
    #create two regexes, one for phone numbers and another for emails
    phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?
        (\s|-|\.)?
        (\d{3})
        (\s|-|\.)
        (\d{4})
        (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

    emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+
        @
        [a-zA-Z0-9.-]+
        (\.[a-zA-Z]{2,4})        
    )''', re.VERBOSE)

    # Find all matches, not just the first match of both regexes
    matches = []
    for groups in phoneRegex.findall(text):
        phoneNum = "-".join([groups[1], groups[3], groups[5]])
        if groups[8] != "":
            phoneNum += " x" + groups[8]
        matches.append(phoneNum)
    for groups in emailRegex.findall(text):
        matches.append(groups[0])

    return matches


def pasteText(matches):
    # Neatly format the matched strings into a single string to paste
    # Paste Text to the clipboard
    # Display some kind of message if no matches were found in the text.
    if len(matches) > 0:
        pyperclip.copy("\n".join(matches))
        print("")
        print("Copied to clipboard!")
        print("\n".join(matches))
        print("")
    else:
        print("")
        print("No phone numbers or email addressed detected.")


def main():
    if prompt() == "no":
        return

    clipboard_text = getText()
    filtered_text = findPhoneandEmails(clipboard_text)
    pasteText(filtered_text)
    main()


main()