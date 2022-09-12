#! python3
# By Victour Bue

import requests, os


def prompt():
    print("""
    This program will take a url and download the data from that url into a .txt file.
    Please enter a URL or just press enter to exit the program.
    """)
    URL = input()
    print()
    if not URL:
        return URL
    try:
        res = requests.get(URL)
        res.raise_for_status()
        return res
    except Exception as exc:
        print(f"There was a problem: {exc}")
        print("Please try again.")
        return prompt()

def save_file(res):
    filename = input("What would you like to name this file? \n")
    with open(f"{filename}.txt", "wb") as playFile:
        for chunk in res.iter_content(100_000):
            playFile.write(chunk)    
    print(f"File Saved @ {os.getcwd()}")

def main():
    res = prompt()
    if (not res):
        return
    save_file(res)
    return main()


main()